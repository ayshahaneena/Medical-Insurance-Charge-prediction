# Medical Insurance Charge Prediction

## 📌 Project Overview
This project predicts medical insurance charges based on patient information such as age, BMI, smoking status, and other relevant features. The model is developed using machine learning techniques and deployed as an interactive **Streamlit web application** for easy access.

![alt text](https://bsmedia.business-standard.com/_media/bs/img/article/2023-08/22/full/1692692413-6198.jpg)


## Dataset
The dataset contains the following columns:

- Age: The age of the individual.
- Sex: The gender of the individual (male/female).
- BMI: The Body Mass Index.
- Children: The number of children/dependents covered by the insurance.
- Smoker: Whether the individual is a smoker (yes/no).
- Region: The region in which the individual resides (southwest, southeast, northwest).
- Charges: The medical insurance charges for the individual.
## Steps

- **Data Visualizations**: Provides interactive graphs and charts to uncover insights from the data.
- **Statistical Analysis**: Conducted statistical tests to uncover meaningful relationships between features and charges.
- **Data Preprocessing**: Handles missing values, encodes categorical variables, and scales features for model compatibility.
- **Machine Learning Model**: Built with **Gradient Boosting Regressor** to predict charges accurately.
- **Interactive UI**: Designed with **Streamlit** to provide an intuitive user experience for real-time predictions.

## 🔧 Tech Stack
- **Python**
- **Scikit-learn** (for machine learning)
- **Pandas & NumPy** (for data manipulation)
- **Matplotlib & Seaborn** (for visualizations)
- **Streamlit** (for building the web app)
- **GitHub** (for version control)

## 📂 Project Structure
```
Medical-Insurance-Charge-Prediction/
├── app.py    # Streamlit App
├── demo_app.mp4  # Demo video for the app
├── insurance.csv                   # Dataset
├── insurance_model.pkl             # Trained model
├── Medical_Insurance_Prediction.ipynb # Jupyter Notebook for analysis
├── requirements.txt                # Required Libraries
└── streamlit_img.png               # Image for Streamlit app
```


## 📊 Statistical Analysis
### 1. **Spearman's Rank Correlation (BMI and Charges)**
- **Null Hypothesis (H0)**: There is no correlation between BMI and charges.
- **Alternative Hypothesis (H1)**: There is a correlation between BMI and charges.
- **Spearman Correlation Coefficient**: 0.119
- **p-value**: 0.000012
- **Inference**: Since the p-value is less than 0.05, we reject the null hypothesis and conclude that there is a significant correlation between BMI and insurance charges.

### 2. **T-test (Smokers vs. Non-Smokers)**
- **Null Hypothesis (H0)**: The insurance charges for smokers and non-smokers are the same.
- **Alternative Hypothesis (H1)**: Smokers pay higher insurance charges than non-smokers.
- **T-statistics**: 32.593
- **p-value**: 0.000000
- **Inference**: With a p-value of 0, we reject the null hypothesis and conclude that smokers pay significantly higher charges than non-smokers.

## Machine Learning Model
Model: Gradient Boosting Regressor
The model was trained using Gradient Boosting Regressor and evaluated on various metrics to assess its performance. The following evaluation metrics were used:

- R² Score: 0.8795 (This indicates that the model explains approximately 87.95% of the variance in the charges data).
- RMSE (Root Mean Squared Error): 4324.47 (This is the average error between the predicted and actual values).
- MAE (Mean Absolute Error): 2400.73 (This represents the average absolute error between the predicted and actual values).
Model Evaluation Inference:
The model demonstrated high accuracy with an R² score close to 0.88, making it a strong predictor for insurance charges. The RMSE and MAE values suggest that the model's predictions are reasonably close to the actual values, ensuring reliability.


### 📜 License
This project is licensed under the MIT License.
