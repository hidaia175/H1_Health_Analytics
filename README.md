<<<<<<< HEAD
# Project: Healthcare Insurance Cost Analysis

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

---

## Overview

**Healthcare Insurance Cost Analysis** is a comprehensive data analysis project designed to explore and visualise how personal attributes and geographic factors influence health insurance costs.  
The aim is to build predictive models that estimate healthcare expenses, uncover key cost drivers, and support data-driven decision-making for insurance providers.

---

## Dataset Content

**Source:** [Kaggle - Healthcare Insurance Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance)

The dataset contains demographic and lifestyle data for individuals, including personal attributes and regional information.  
It helps analyse how these factors affect medical insurance charges and supports the development of predictive models.

**Example Columns:**

- `age` – Age of the policyholder
- `sex` – Gender
- `bmi` – Body Mass Index (an indicator of weight relative to height)
- `children` – Number of dependents
- `smoker` – Smoking status (Yes/No)
- `region` – Residential region (northeast, northwest, southeast, southwest)
- `charges` – Medical insurance cost (target variable)

The dataset contains approximately 1,300 records and 7 columns.

---

## Business Requirements

The main business objectives are to:

1. **Analyse insurance charges** across demographic and lifestyle variables (age, gender, region, BMI, smoking status).
2. **Develop predictive models** that estimate individual healthcare expenses.
3. **Visualise patterns and correlations** between personal and regional factors.
4. **Provide insights and recommendations** for better cost estimation and policy planning.

---

## Hypotheses and Validation

| Hypothesis                                                    | Validation Approach                                                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------- |
| Smoking has a significant positive impact on insurance costs. | Compare average charges between smokers and non-smokers.            |
| Higher BMI values are associated with higher insurance costs. | Use scatter plots and correlation analysis between BMI and charges. |
| Age strongly correlates with medical expenses.                | Plot insurance charges by age and compute correlation coefficients. |
| Regional factors influence insurance costs.                   | Compare mean charges by region using bar charts.                    |

---

## Project Plan

### 1. ETL Pipeline

- **Extract:**  
  Load the dataset from the Kaggle source (CSV format).

- **Transform:**

  - Handle missing values and data inconsistencies.
  - Encode categorical variables (e.g., gender, region, smoker).
  - Create additional features such as BMI categories (Underweight, Normal, Overweight, Obese).
  - Normalise or scale features as needed for predictive models.

- **Load:**  
  Store the transformed data into a cleaned DataFrame suitable for analysis.

### 2. Analysis & Visualisation

- Conduct **descriptive statistics** (mean, median, standard deviation).
- Visualise **average charges** by age, BMI, gender, and region.
- Display **correlation heatmaps** to identify strong relationships.
- Build **predictive models** (e.g., Linear Regression, Random Forest).
- Visualise **predicted vs actual insurance costs** using scatter plots.
- Illustrate **regional cost variations** using bar charts or maps.

### 3. Documentation & Deployment

- Prepare full project documentation.
- Review, test, and deploy the final app version on **Heroku**.
- Push the final version to **GitHub** within the given timeframe.

---

## Mapping Business Requirements to Data Visualisations

| Business Requirement                                   | Visualisation Type                | Rationale                                                           |
| ------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------- |
| Analyse average insurance costs by demographic factors | Bar Charts                        | Show variation in average charges by age, gender, and region        |
| Identify correlation between variables                 | Heatmap                           | Display relationships between factors such as BMI, age, and charges |
| Predict insurance charges                              | Scatter Plot with Regression Line | Compare actual vs predicted charges                                 |
| Show regional impact                                   | Grouped Bar Chart or Map          | Visualise cost differences between regions                          |

---

## Analysis Techniques Used

### Data Analysis Methods:

- **Descriptive Analysis:** Summarise data and identify key trends.
- **Correlation Analysis:** Evaluate relationships among numerical features.
- **Predictive Analysis:** Use regression and ML models to forecast insurance charges.
- **Geographical Analysis:** Assess cost differences across regions.

### Structure:

1. Data exploration and cleaning.
2. Feature engineering and encoding.
3. Statistical and correlation analysis.
4. Predictive model building and evaluation.
5. Data visualisation and interpretation.

### Limitations and Alternatives:

- Dataset does not include health history or income data.  
  → Focus is limited to demographic and lifestyle factors.
- No time-series component for trend forecasting.  
  → Adapted to cross-sectional analysis using regression models.

### Use of Generative AI Tools:

Tools such as **ChatGPT** and **GitHub Copilot** were used to:

- Optimise code and improve readability.
- Suggest better visualisation techniques.
- Rephrase and structure documentation for clarity.

---

## Ethical Considerations

- **Data Privacy:** Dataset is anonymised; no identifiable information exists.
- **Bias Risks:** Smoking and BMI can introduce bias; results are presented transparently.
- **Fair Use:** Data used only for educational and analytical purposes.
- **Ethical Reporting:** Clear communication of limitations to avoid misinterpretation.

---

## Dashboard Design

### Planned Pages:

1. **Home Page:** Project overview and summary.
2. **Data Overview:** Key statistics, filters for gender, region, and smoking status.
3. **Visual Analysis:** Correlation heatmaps, scatter plots, bar charts.
4. **Predictive Model:** Interactive prediction of insurance costs based on user input.
5. **About/References:** Dataset and credits.

### Components:

- Buttons and filters for feature selection.
- Interactive charts built with Plotly or Seaborn.
- Input widgets for model predictions.
- KPI indicators for average charge, median BMI, etc.

### Communication:

Designed for both technical (data analysts) and non-technical (business users) audiences.  
Visuals are simple, colour-coded, and annotated for easy interpretation.

---

## Unfixed Bugs

- Occasional formatting issues in visualisations on mobile devices.
- Long loading times when rendering large plots.  
  These are minor and related to library performance limitations.

---

## Development Roadmap

### Challenges:

- Managing feature encoding and scaling consistently.
- Achieving accurate predictive models with limited data.

### Future Improvements:

- Add more health-related attributes (e.g., medical history, physical activity).
- Integrate time-series data for forecasting trends.
- Improve dashboard responsiveness and performance.
- Experiment with advanced models (e.g., XGBoost, Neural Networks).

---

## Deployment

### Heroku

**App Live Link:** [https://YOUR_APP_NAME.herokuapp.com/](https://YOUR_APP_NAME.herokuapp.com/)

**Deployment Steps:**

1. Log in to Heroku and create a new app.
2. Connect the app to your GitHub repository.
3. Select your deployment branch and click **Deploy Branch**.
4. Ensure that:
   - `runtime.txt` specifies a Heroku-supported Python version.
   - `requirements.txt` includes all necessary dependencies.
5. If slug size is too large, add unnecessary files to `.slugignore`.
6. Once deployed, click **Open App** to launch the dashboard.

---

## Main Data Analysis Libraries

| Library                  | Purpose                        | Example                                                |
| ------------------------ | ------------------------------ | ------------------------------------------------------ |
| **Pandas**               | Data manipulation & analysis   | `df.describe()`                                        |
| **NumPy**                | Mathematical operations        | `np.mean(df['charges'])`                               |
| **Matplotlib / Seaborn** | Static visualisations          | `sns.barplot(x='region', y='charges', data=df)`        |
| **Plotly**               | Interactive plots & dashboards | `px.scatter(df, x='bmi', y='charges', color='smoker')` |
| **Scikit-learn**         | Predictive modelling           | `LinearRegression().fit(X, y)`                         |
| **Streamlit / Dash**     | Dashboard development          | `st.line_chart(data)`                                  |

---

## Credits

### Content

- Dataset: [Healthcare Insurance Dataset – Kaggle](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance)
- Project Template: [Code Institute Data Analytics Template](https://github.com/Code-Institute-Solutions/da-README-template)
- Documentation assistance: ChatGPT and GitHub Copilot
- Icons: [Font Awesome](https://fontawesome.com/)

### Media

- Placeholder images and visuals: [Unsplash](https://unsplash.com/)

---

## Acknowledgements

Special thanks to **Code Institute mentors and peers** for guidance and constructive feedback throughout this project.  
Appreciation is also extended to the **Kaggle** community for providing high-quality open datasets used in this analysis.

---
=======
# H1_Health_Analytics
>>>>>>> a4ffbc969dfe178ff93204e3701ee7ac2117fb1c
