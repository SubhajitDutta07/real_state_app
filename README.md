# Real Estate Price Predictor & Market Analysis Platform

A comprehensive real estate analytics platform that provides accurate price predictions, property recommendations based on landmarks, and detailed market analysis for better investment decisions.

## 🏠 Overview

This application is a full-stack real estate solution that combines machine learning with practical features to help users make informed property decisions. The platform offers three main functionalities:

- **💰 Price Prediction**: Accurate property valuation using advanced ML models
- **📍 Smart Recommendations**: Property suggestions based on landmark proximity
- **📊 Market Analysis**: Comprehensive insights and trends for market awareness

## ✨ Features

### 🔮 Price Prediction
- Predict property prices based on various features
- Machine learning model trained on real estate data
- User-friendly interface for input parameters

### 🎯 Smart Recommendations
- Landmark-based property discovery
- Distance-based filtering (1km, 3km, 5km radii)
- Personalized suggestions matching user preferences

### 📈 Market Analysis
- Interactive charts and visualizations
- Market trend analysis
- Price distribution across locations
- Investment opportunity insights

## 🛠️ Tech Stack

### Machine Learning
- **Regression Models** (Random Forest, XGBoost, Linear Regression)
- **Feature Engineering**
- **Model Evaluation & Validation**


## 🚀 Installation

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/SubhajitDutta07/real_state_app.git
cd real_state_app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
streamlit run Home.py
