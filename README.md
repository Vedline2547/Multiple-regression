# Multiple Linear Regression

## Project Overview

This project demonstrates the implementation of **Multiple Linear Regression** using Python and Scikit-learn. It uses a synthetically generated dataset containing two independent features and one continuous target variable to train a regression model and evaluate its predictive performance.

The project also uses Plotly to create interactive 3D visualizations, making it easier to explore the relationship between the input features and the target variable.

## Objectives

- Generate synthetic regression data using Scikit-learn.
- Explore relationships between two independent variables and a continuous target.
- Visualize the dataset using interactive 3D scatter plots.
- Train a Multiple Linear Regression model.
- Evaluate model performance using standard regression metrics.
- Visualize actual versus predicted target values.
- Interpret the model's coefficients and intercept.

## Technologies Used

- **Python** — Core programming language.
- **Pandas** — Data organization and manipulation.
- **NumPy** — Numerical computations.
- **Scikit-learn** — Dataset generation, train-test splitting, model training, and evaluation.
- **Plotly Express** — Interactive data visualization.
- **Plotly Graph Objects** — Customizing interactive charts.

## Dataset

The dataset is generated using Scikit-learn's `make_regression()` function, so an external dataset is not required.

The dataset configuration includes:

- **Samples:** 100
- **Features:** 2
- **Informative features:** 2
- **Target variables:** 1
- **Noise:** 10
- **Random state:** 42

The dataset contains two input features, `feature1` and `feature2`, and one continuous target variable, `target`.

## Methodology

### 1. Data Generation

Synthetic data is generated using `make_regression()` to simulate a linear relationship between the input features and the target variable.

### 2. Data Preparation

The generated features and target values are organized into a Pandas DataFrame for easier inspection and visualization.

### 3. Exploratory Data Visualization

Plotly Express is used to create an interactive 3D scatter plot to explore the relationship between the two features and the target.

### 4. Train-Test Split

The dataset is divided into training and testing sets, with 80% used for training and 20% reserved for evaluation.

### 5. Model Training

A `LinearRegression` model is trained using the two input features to learn their relationship with the target variable.

### 6. Model Evaluation

The trained model generates predictions on the test set. Its performance is evaluated using:

- **Mean Absolute Error (MAE):** Measures the average absolute prediction error.
- **Mean Squared Error (MSE):** Measures the average squared prediction error.
- **Root Mean Squared Error (RMSE):** Measures prediction error in the target's original units.
- **R² Score:** Measures how well the model explains variation in the target values.

### 7. Prediction Visualization

An actual-versus-predicted scatter plot is used to compare model predictions with actual target values. A reference line represents perfect predictions.

## Model

The Multiple Linear Regression model estimates the target using two independent features:

\[
\hat{y} = \beta_0 + \beta_1x_1 + \beta_2x_2
\]

Where:

- \(\hat{y}\) is the predicted target.
- \(\beta_0\) is the intercept.
- \(\beta_1\) and \(\beta_2\) are the learned coefficients.
- \(x_1\) and \(x_2\) are the input features.

## Installation and Usage

### Prerequisites

Install Python 3.12 or another compatible Python version.

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/Multiple-regression.git
cd Multiple-re
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install pandas numpy scikit-learn plotly
```

### 4. Run the project

```bash
python main.py
```

The evaluation metrics will be printed in the terminal, and the interactive Plotly visualizations will open in your browser.

## Key Learning Outcomes

Through this project, I explored:

- The fundamentals of Multiple Linear Regression.
- Synthetic dataset generation for machine learning.
- Training and testing machine learning models.
- Regression evaluation metrics and their interpretation.
- Interactive 3D data visualization.
- Comparing actual values with model predictions.
- Understanding regression coefficients and the model intercept.

## Future Improvements

- Experiment with different noise levels and dataset sizes.
- Compare Multiple Linear Regression with other regression algorithms.
- Analyze residuals to identify patterns in prediction errors.
- Evaluate generalization using cross-validation.
- Apply the model to a real-world regression dataset.

## Author

**Vedline Ochieng**

Civil Engineering Student | Python Developer | Machine Learning Enthusiast

GitHub: [@Vedline2547](https://github.com/Vedline2547)

---

*This project is part of my ongoing journey in machine learning and data science.*
