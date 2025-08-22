import { useState } from 'react';
import axios from 'axios';

const NewsChecker = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_URL = import.meta.env.PROD 
    ? '/api/predict' 
    : 'http://localhost:5000/api/predict';

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!text.trim()) {
      setError('Please enter some news text to analyze');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post(API_URL, {
        text: text.trim()
      }, {
        headers: {
          'Content-Type': 'application/json'
        },
        timeout: 10000
      });

      setResult(response.data);
    } catch (err) {
      console.error('API Error:', err);
      if (err.response?.data?.error) {
        setError(err.response.data.error);
      } else if (err.code === 'ECONNABORTED') {
        setError('Request timeout. Please try again.');
      } else {
        setError('Failed to analyze news. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setText('');
    setResult(null);
    setError('');
  };

  const getResultColor = (prediction) => {
    return prediction === 'Real' ? 'text-green-600' : 'text-red-600';
  };

  const getResultBgColor = (prediction) => {
    return prediction === 'Real' ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200';
  };

  const getConfidenceBarColor = (prediction) => {
    return prediction === 'Real' ? 'bg-green-500' : 'bg-red-500';
  };

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      <div className="card animate-fade-in">
        <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
          Analyze Soccer News
        </h2>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label htmlFor="newsText" className="block text-sm font-medium text-gray-700 mb-2">
              Paste your soccer news article here:
            </label>
            <textarea
              id="newsText"
              value={text}
              onChange={(e) => setText(e.target.value)}
              rows={8}
              className="w-full p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
              placeholder="Enter soccer news text here... (e.g., 'Lionel Messi signs new contract with PSG for €50 million per year')"
              disabled={loading}
            />
            <div className="mt-2 text-sm text-gray-500">
              {text.length}/10000 characters
            </div>
          </div>

          <div className="flex gap-4 justify-center">
            <button
              type="submit"
              disabled={loading || !text.trim()}
              className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {loading ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent"></div>
                  Analyzing...
                </>
              ) : (
                <>
                  🔍 Analyze News
                </>
              )}
            </button>
            
            {text && (
              <button
                type="button"
                onClick={handleClear}
                className="btn-secondary"
                disabled={loading}
              >
                Clear
              </button>
            )}
          </div>
        </form>

        {error && (
          <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg animate-slide-up">
            <p className="text-red-700">⚠️ {error}</p>
          </div>
        )}

        {result && (
          <div className={`mt-6 p-6 rounded-lg border-2 animate-slide-up ${getResultBgColor(result.prediction)}`}>
            <div className="text-center">
              <h3 className="text-2xl font-bold mb-4">
                {result.prediction === 'Real' ? '✅ Real News' : '🚫 Fake News'}
              </h3>
              
              <div className={`text-4xl font-bold mb-4 ${getResultColor(result.prediction)}`}>
                {result.prediction.toUpperCase()}
              </div>

              <div className="space-y-4">
                <div>
                  <div className="flex justify-between text-sm text-gray-600 mb-2">
                    <span>Confidence Level</span>
                    <span>{Math.round(result.confidence * 100)}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3">
                    <div
                      className={`h-3 rounded-full transition-all duration-500 ${getConfidenceBarColor(result.prediction)}`}
                      style={{ width: `${result.confidence * 100}%` }}
                    ></div>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div className="text-center">
                    <div className="text-gray-600">Real Probability</div>
                    <div className="font-bold text-green-600">
                      {Math.round(result.probabilities.real * 100)}%
                    </div>
                  </div>
                  <div className="text-center">
                    <div className="text-gray-600">Fake Probability</div>
                    <div className="font-bold text-red-600">
                      {Math.round(result.probabilities.fake * 100)}%
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default NewsChecker;