# Multiple Disease Prediction App

## Overview

This project is a web-based application built using Python and Streamlit that allows users to predict the likelihood of having three different diseases: Diabetes, Heart Disease, and Parkinson's Disease. The application uses pre-trained machine learning models to provide predictions based on user input data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Diabetes Prediction**: Predicts the likelihood of diabetes based on user input data such as glucose level, blood pressure, insulin, etc.
- **Heart Disease Prediction**: Assesses the risk of heart disease using user data like age, cholesterol level, blood pressure, etc.
- **Parkinson's Disease Prediction**: Estimates the probability of Parkinson's disease based on voice measurements and other relevant data.
- **User-Friendly Interface**: Easy-to-use web application powered by Streamlit.
- **Real-Time Predictions**: Instant predictions as soon as the user inputs data.

## Technologies Used

- **Python**: Programming language used to implement the machine learning models and application logic.
- **Streamlit**: Framework used to build the web application interface.
- **Scikit-learn**: Library used to build and train the machine learning models.
- **Pandas**: Data manipulation and analysis library.
- **Numpy**: Library used for numerical computations.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/multiple-disease-prediction-app.git
    cd multiple-disease-prediction-app
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit App**:

    ```bash
    streamlit run app.py
    ```

5. **Open the Application**:
   After running the command above, Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser to access the application.

## Usage

1. **Diabetes Prediction**:
   - Navigate to the Diabetes Prediction section.
   - Input the required data (e.g., glucose level, blood pressure, etc.).
   - Click on the "Predict" button to see the results.

2. **Heart Disease Prediction**:
   - Navigate to the Heart Disease Prediction section.
   - Input the required data (e.g., age, cholesterol, blood pressure, etc.).
   - Click on the "Predict" button to see the results.

3. **Parkinson's Disease Prediction**:
   - Navigate to the Parkinson's Disease Prediction section.
   - Input the required data (e.g., voice measurements).
   - Click on the "Predict" button to see the results.

## Model Information

- **Diabetes Prediction Model**: Trained on the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
- **Heart Disease Prediction Model**: Trained on the [Cleveland Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease).
- **Parkinson's Disease Prediction Model**: Trained on the [Parkinson's dataset](https://archive.ics.uci.edu/ml/datasets/parkinsons).

The models are built using scikit-learn and have been tuned for accuracy using various machine learning algorithms.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-new-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The datasets used in this project are publicly available and were taken from [Kaggle](https://www.kaggle.com/) and the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).
- The project was inspired by various open-source projects and tutorials on machine learning.
