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
