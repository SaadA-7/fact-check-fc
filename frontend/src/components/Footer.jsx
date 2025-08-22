const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-8 mt-12">
      <div className="container mx-auto px-4 text-center">
        <p className="text-gray-300 mb-4">
          Built with React, Flask, and Machine Learning
        </p>
        <div className="flex justify-center space-x-6 text-sm text-gray-400">
          <span>🤖 AI-Powered</span>
          <span>⚡ Fast Detection</span>
          <span>🎯 Accuracy tuning</span>
        </div>
        <p className="text-xs text-gray-500 mt-4">
          © 2025 Soccer Fact-Checker. Built for research & educational purposes.
        </p>
      </div>
    </footer>
  );
};

export default Footer;