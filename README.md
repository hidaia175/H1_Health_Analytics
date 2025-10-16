## 🧩 Project Management (Day 1)

During the first day, the following setup and management steps were completed:

1. **Project Idea**

   - The selected project is _Healthcare Insurance Cost Analysis_.
   - The goal is to explore how personal and regional factors influence healthcare insurance charges and to prepare data for predictive analysis.

2. **Repository Setup**

   - A GitHub repository was created named **`H1_Health_Analytics`**.
   - The main folders and files included:
     - `data/` → for storing datasets
     - `notebooks/` → for Jupyter Notebooks
     - `day1-analysis.ipynb` → for Day 1 ETL and visualisation work
     - `README.md` → for documentation and reporting

3. **Project Board and Workflow**

   - A GitHub Project Board was created to organise tasks using a **Kanban-style workflow** with the following columns:
     - **Backlog** → ideas and tasks not yet started
     - **To Do** → tasks planned for the current day
     - **In Progress** → tasks currently being worked on
     - **Done** → completed items
   - This structure helped visualise progress and prioritise daily deliverables.

4. **Labels and Prioritisation (MoSCoW method)**

- Each issue was labeled using MoSCoW prioritisation to manage importance:
  - **Must Have** → essential tasks (e.g., ETL process, data cleaning)
  - **Should Have** → important but not critical (e.g., basic visualisations)
  - **Could Have** → optional improvements (e.g., styling charts)
  - **Won’t Have** → postponed items outside Day 1 scope.
  - Additional functional labels were also used: `ETL`, `Visualisation`, `Report`, and `Dashboard`.

5. **Progress Monitoring**
   - Milestones and labels were used to track daily progress.
   - Minor setup issues (e.g., folder structure or file paths) were identified and fixed successfully during Day 1.

### **Extract**

- The dataset was loaded from [Kaggle – Healthcare Insurance Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance).
- It contains **1,338 rows** and **7 columns** describing personal and regional attributes such as age, gender, BMI, number of children, smoking status, region, and insurance charges.
- During this stage, a **path error** occurred in VS Code while loading the CSV file.  
  Through a short **debugging process**, the issue was identified and fixed by correcting the file path:
  ```python
  df = pd.read_csv("data/insurance.csv")
  ```

### **Debugging and Transformation Notes**

During the transformation stage, a small debugging step was required to verify file paths and ensure the data was correctly loaded.  
No missing values were found in the dataset, but a few **data quality checks** were performed to ensure consistency:

- Checked for duplicate rows and removed any if found.
- Standardised column names to lowercase for easier reference.
- Created a new column **`BMI_category`** to classify BMI values into:
  - Underweight (BMI < 18.5)
  - Normal (18.5–24.9)
  - Overweight (25–29.9)
  - Obese (≥30)

These steps improved the dataset’s structure and made it ready for further analysis and visualisation.  
The cleaned version was saved as **`insurance_cleaned.csv`** inside the `data/` folder.

## 📊 Data Visualisation (Day 1)

Initial data visualisations were created using **Matplotlib**, **Seaborn**, and **Plotly** to explore the cleaned dataset and understand its structure.

Before visualisation, the data was **cleaned and saved** into a new file named **`insurance_cleaned.csv`** in the `data/` folder.  
This ensured that all graphs were generated from accurate and preprocessed data.

During this process, a small issue occurred where the variable `df` was not recognized after restarting the Jupyter Notebook.  
This was solved by reloading the dataset and re-running previous steps with the help of **ChatGPT**, which provided debugging guidance.

---

### 1️⃣ Age Distribution

- **Tool used:** `Matplotlib`
- **Purpose:** To display how ages are distributed among insured individuals.
- **Insight:** Most policyholders fall between 20–50 years old, representing the main working-age population.

---

### 2️⃣ Charges by Smoking Status

- **Tool used:** `Seaborn (Boxplot)`
- **Purpose:** To compare insurance charges between smokers and non-smokers.
- **Insight:** Smokers clearly pay higher insurance costs compared to non-smokers.

---

### 3️⃣ Average Charges by Region

- **Tool used:** `Plotly (Interactive Bar Chart)`
- **Purpose:** To visualize regional differences in average insurance charges.
- **Insight:** The **southeast** region shows the highest average costs, while other regions remain relatively balanced.

### 4️⃣ Interactive Scatter Plot (BMI vs Insurance Charges)

To make the data visualisation more interactive and insightful, an **interactive scatter plot** was created using **Plotly Express**.  
This visualisation allows users to explore how **Body Mass Index (BMI)** and **smoking habits** influence insurance charges.

- **Tool used:** Plotly Express
- **X-axis:** BMI
- **Y-axis:** Insurance Charges
- **Color:** Smoker status (Yes/No)
- **Hover Data:** Age and Region
- **Purpose:** To visualise the relationship between BMI and medical charges and highlight how smoking amplifies costs.

**Insight:**  
The scatter plot shows a clear upward trend — individuals with higher BMI values and smoking habits tend to have significantly higher insurance charges.  
Users can hover over each data point to view details about the person’s age and region, making the visualisation both **interactive** and **informative**.

**Code Example:**

```python
import plotly.express as px

fig = px.scatter(
    df,
    x='bmi',
    y='charges',
    color='smoker',
    title="BMI vs Insurance Charges (Interactive Scatter Plot)",
    hover_data=['age', 'region']
)
fig.show()
--

These visualisations provided an in## ETL Pipeline Validation (Day 2)

During Day 2, the ETL pipeline was tested to ensure that the dataset was accurate, consistent, and ready for analysis before creating advanced visualisations.

### Steps Performed
1. **Extract:**
   The cleaned dataset `insurance_cleaned.csv` was supposed to be loaded from the `data/` folder.

2. **Issue Encountered:**
   At first, the data was not properly linked to the cleaned file, and the notebook could not find the dataset.
   After testing different paths and getting support from ChatGPT, the problem was fixed by reloading the file correctly.

3. **Transform:**
   - Checked column names for consistency.
   - Verified that there were no missing or duplicate records.
   - Confirmed that all data types were correct.

4. **Load:**
   - The cleaned data was successfully reloaded and confirmed to be correct and ready for visualisation.

### Reflection
The small error during data loading helped improve understanding of how to manage file paths in Jupyter Notebook.
After fixing it, the ETL process worked properly, and the dataset was validated and ready for further analysis.
itial understanding of how **age, lifestyle, and region** influence medical insurance costs.
They also confirmed that the dataset is clean, consistent, and ready for deeper predictive analysis in the following phases.
```
