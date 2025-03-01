# Student Exam Performance Predictor

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://studentexamperfermance-f13e691190e1.herokuapp.com/)

## 📋 Overview

![](https://storage.googleapis.com/kaggle-datasets-images/4302880/7400136/2274c7efc02a775080a121160d222d8f/dataset-cover.jpg?t=2024-01-14-12-06-04)

This end-to-end machine learning project implements a predictive model that forecasts students' mathematics scores based on various demographic factors and performance in other subjects. The model aims to assist educators and students in understanding potential academic outcomes and identifying areas that may require additional support.

The project encompasses the complete machine learning engineering lifecycle from data ingestion to deployment in a production environment.

## ✨ Features

- Data ingestion pipeline from multiple sources
- Automated data preprocessing and transformation
- Machine learning model training and evaluation
- User-friendly web interface for making predictions
- Containerized deployment for scalability

## 🚀 Live Demo

You can interact with the deployed application here: [Student Exam Performance Predictor](https://studentexamperfermance-f13e691190e1.herokuapp.com/)

## 📸 Project Screenshot

![Application Screenshot](https://github.com/user-attachments/assets/c48c1704-be77-4d58-9658-1cabc9a114f3)

## 📝 Step-by-Step Development Process

### 1. Project Setup and Environment Configuration

1. **Created and configured the GitHub repository**
   - Set up version control structure
   - Added appropriate .gitignore file

2. **Set up isolated Python environment**
   ```bash
   conda create -p venv python==3.12.1 -y
   conda activate venv/
   ```

3. **Configured Git global settings**
   ```bash
   git config --global user.email "your-email@example.com"
   git config --global user.name "Your Name"
   ```

4. **Created project configuration files**
   - Created `setup.py` to define the project as a distributable package
   - Added `requirements.txt` to specify dependencies

### 2. Project Structure Implementation

1. **Created the source package structure**
   ```
   src/
   ├── __init__.py
   ├── components/
   │   ├── __init__.py
   │   ├── data_ingestion.py
   │   ├── data_transformation.py
   │   └── model_trainer.py
   ├── pipeline/
   │   ├── __init__.py
   │   ├── predict_pipeline.py
   │   └── train_pipeline.py
   ├── exception.py
   ├── logger.py
   └── utils.py
   ```

2. **Implemented core utility modules**
   - `exception.py`: Custom exception handling
   - `logger.py`: Configurable logging system
   - `utils.py`: Helper functions for common operations

### 3. Data Pipeline Development

1. **Created data ingestion component**
   - Implemented data loading from various sources
   - Added data validation and initial cleaning

2. **Built data transformation pipeline**
   - Feature engineering and preprocessing
   - Implemented encoding for categorical variables
   - Created standardization for numerical features
   - Developed pipeline serialization for consistency

### 4. Model Development

1. **Implemented model training module**
   - Evaluated multiple regression algorithms
   - Performed hyperparameter tuning
   - Applied cross-validation techniques
   - Selected optimal model based on performance metrics

2. **Created prediction pipeline**
   - Built inference system for making predictions
   - Implemented model loading and preprocessing consistency

### 5. Web Application Development

1. **Designed user interface**
   - Created intuitive form for input parameters
   - Implemented results visualization

2. **Integrated prediction backend**
   - Connected UI to prediction pipeline
   - Added error handling and input validation

### 6. Deployment Pipeline

**Deployed to cloud platform**

- Deployed to Heroku for public access
- Set up continuous integration/deployment

## 🔧 Technologies Used

- **Python**: Core programming language
- **Scikit-learn**: ML algorithms and pipelines
- **Pandas/NumPy**: Data manipulation
- **Flask**: Web application framework
- **Matplotlib/Seaborn**: Data visualization
- **Heroku**: Cloud deployment