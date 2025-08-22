# Soccer Fake News Detector 🔍⚽

An AI-powered web application that detects fake soccer news using machine learning and natural language processing.

## 🚀 Features

- **Real-time Analysis**: Instantly classify soccer news as real or fake
- **High Accuracy**: Uses TF-IDF vectorization and Logistic Regression
- **Modern UI**: Responsive design built with React and Tailwind CSS
- **Confidence Scoring**: Shows prediction confidence and probabilities
- **Fast & Reliable**: Deployed on Vercel for optimal performance

## 🛠️ Tech Stack

### Backend
- **Python 3.11**
- **Flask** - REST API framework
- **Scikit-learn** - Machine learning library
- **NLTK** - Natural language processing
- **Pandas** - Data manipulation

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### Deployment
- **Vercel** - Hosting platform

## 🏃‍♂️ Running Locally

### Prerequisites
- Python 3.11+
- Node.js 16+
- Git

### Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python model_trainer.py  # Train the model
python app.py  # Start Flask server
```

### Frontend Setup
```bash

cd frontend
npm install
npm run dev  # Start development server
```