# Soccer Fake News Detector 🔍⚽

An AI-powered web application that detects fake soccer news using machine learning and natural language processing.

**THIS PROJECT IS A PROTOTYPE AND FOR RESEARCH & EDUCATIONAL PURPOSES**
**Model Training to be updated via news datasets.**

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

## How it Works
1) Text Preprocessing: Cleans input text (remove URLs, punctuation, stopwords)
2) Feature Extraction: Converts text to numerical features using TF-IDF
3) Classification: Uses Logistic Regression to predict real/fake
4) Confidence Scoring: Returns prediction probabilities

## File structure
fact-check-fc/
├── backend/
│   ├── app.py              # Flask API
│   ├── model_trainer.py    # ML model training
│   ├── requirements.txt    # Python dependencies
│   └── *.pkl              # Trained models
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.jsx       # Main app component
│   │   └── main.jsx      # Entry point
│   ├── package.json      # Node dependencies
│   └── tailwind.config.js # Tailwind configuration
├── vercel.json           # Deployment configuration
└── README.md

## Deployment
Deployed via vercel and if you want to deploy your own locally:
The application is automatically deployed to Vercel when you push to the main branch.

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
This proect was for research and educational purposes during an internship with Elevvo.