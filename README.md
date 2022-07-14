# Overview
The objective of this machine learning classification problem is to develop and deploy a model that can make predictions on the heart condition of humans.
# Stack
- Python
- HTML
- Github
- Heroku

# Approaches applied in surmounting the problem include:
- Data gathering from kaggle.com
- Creation of a project directory and installation of a new virtual environment
- Loading of dataset into a DataFrame.
- Exploratory Data Analysis (**EDA**).
- Feature Engineering.
- Model development and fitting to data.
- Model Evaluation
- Development of a Flask App
- Deployment process on Github and Heroku cloud.

### 1. Data gathering: The process of data acquisition involves searching for and saving to the local drive a curated csv file uploaded on [Kaggle](kaggle.com) for solving problems of heart disease analytics.

### 2. Creation of a project directory and a new virtual virtual environment.
The purpose of this exercise is to create a separate folder for every file attached to this project and to avoid using a cluttered environment for the installation of dependencies.
A run through the processes:
- ##### launching the command prompt on the windows device and running the following commands
- mkdir (Name of Directory) **this creates a new project directory**
- CD (Name of Directory)    **this opens the directory**
- pip install virtualenv    **this installs a new environment into the directory**
- python -m venv (name of environment)    **this nitialises the virtual environment**
- name of environment\Scripts\activate.bat    **this activates the virtual environment**
- pip intall (dependencies)
### 3. Loading of dataset into a DataFrame was achieved using pandas library that simplifies tabular data and its manipualtions.
### 4. EDA steps include:
- Data description and NAN values examination
- Data visualization and analysis
### 5. Feature Engineering processes include:
- OneHotEncoding of categorical values
- Feature scaling using StandardScaler
- Data splitting
### 6. Model development was initiated with an object of XGBoost classification algorithm fitted on the training data and used for pediction of the test data.
### 7. Model evaluation metrics includes:
- Accuracy
- Precision
- Recall
### 8. Development of a web application ensued using a **Flask** application with two rendered **HTML** file stored as static files.
### 9. App deployment was achieved using the following steps:
- Generation of a requirement.txt file for storage of dependencies
- Creation of a procfile to define the app file for Heroku cloud.
- Committing files as a [repository](https://github.com/ChidexCJ/heart_flask_app) on github.
- App hosting on Heroku.
# Summary
Project was succesfully delivered with a few hitches encountered most notably, in the area of deployment on heroku which was unsually incompatible for direct upload from github.
- app: [heart disease predictor](app4heart.herokuapp.com)
