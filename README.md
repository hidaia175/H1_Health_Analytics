# H1 Health Analytics

A comprehensive Python ETL and data visualization project for analyzing health insurance costs. This project provides end-to-end data processing, statistical analysis, and interactive visualizations to gain insights into factors affecting health insurance charges.

## 📋 Project Overview

This project analyzes health insurance data to understand the relationships between various factors (age, BMI, smoking status, region, etc.) and insurance costs. It includes:

- **ETL Pipeline**: Extract, Transform, and Load health insurance data
- **Data Analysis**: Statistical analysis and key insights generation
- **Data Visualization**: Comprehensive charts and graphs for visual insights

## 🚀 Features

- **Data Extraction**: Load health insurance data from CSV files
- **Data Transformation**: Clean data, handle missing values, and create derived features
- **Statistical Analysis**: 
  - Correlation analysis
  - Impact analysis (smoker, BMI, age, region)
  - High-risk profile identification
  - Key insights generation
- **Visualizations**:
  - Charges distribution
  - Smoker impact analysis
  - Age vs charges scatter plots
  - BMI vs charges analysis
  - Regional comparisons
  - BMI category distributions
  - Correlation heatmaps
  - Children impact analysis

## 📁 Project Structure

```
H1_Health_Analytics/
├── data/
│   └── insurance.csv              # Sample health insurance dataset
├── src/
│   ├── __init__.py               # Package initialization
│   ├── etl.py                    # ETL pipeline module
│   ├── analysis.py               # Data analysis module
│   └── visualization.py          # Visualization module
├── notebooks/                     # Jupyter notebooks (optional)
├── outputs/                       # Generated visualizations
├── main.py                        # Main script to run the pipeline
├── requirements.txt               # Project dependencies
└── README.md                      # This file
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/hidaia175/H1_Health_Analytics.git
cd H1_Health_Analytics
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run the Complete Pipeline

Execute the main script to run the entire ETL, analysis, and visualization pipeline:

```bash
python main.py
```

This will:
1. Extract and transform the insurance data
2. Generate a comprehensive analysis report
3. Create visualizations and save them to the `outputs/` directory
4. Save processed data to `data/processed_insurance.csv`

### Use Individual Modules

You can also use the modules independently:

#### ETL Module

```python
from src.etl import HealthInsuranceETL

# Initialize ETL
etl = HealthInsuranceETL('data/insurance.csv')

# Run complete pipeline
processed_data = etl.run_pipeline(output_path='data/processed_insurance.csv')

# Or run steps individually
etl.extract()
etl.transform()
etl.load('data/output.csv')
```

#### Analysis Module

```python
from src.analysis import HealthInsuranceAnalyzer

# Initialize analyzer with processed data
analyzer = HealthInsuranceAnalyzer(processed_data)

# Get basic statistics
stats = analyzer.get_basic_statistics()

# Analyze smoker impact
smoker_impact = analyzer.analyze_smoker_impact()

# Print comprehensive report
analyzer.print_comprehensive_report()
```

#### Visualization Module

```python
from src.visualization import HealthInsuranceVisualizer

# Initialize visualizer
visualizer = HealthInsuranceVisualizer(processed_data, output_dir='outputs')

# Create individual plots
visualizer.plot_smoker_impact()
visualizer.plot_age_vs_charges()
visualizer.plot_bmi_vs_charges()

# Create comprehensive dashboard
visualizer.create_comprehensive_dashboard(save=True)
```

## 📊 Dataset

The project uses a sample health insurance dataset with the following features:

- **age**: Age of the primary beneficiary
- **sex**: Gender (male/female)
- **bmi**: Body Mass Index
- **children**: Number of dependents
- **smoker**: Smoking status (yes/no)
- **region**: Geographic region (northeast, northwest, southeast, southwest)
- **charges**: Individual medical costs billed by health insurance

### Derived Features

The ETL pipeline creates additional features:
- **bmi_category**: Categorized BMI (Underweight, Normal, Overweight, Obese)
- **age_group**: Age groups (18-25, 26-35, 36-45, 46-55, 56+)
- **is_smoker**: Binary smoker indicator (0/1)
- **charges_per_person**: Charges divided by number of people in family

## 📈 Key Insights

The analysis reveals several important findings:

1. **Smoking Impact**: Smokers have significantly higher insurance charges (~4x on average)
2. **Age Correlation**: Insurance charges increase with age
3. **BMI Effect**: Higher BMI correlates with higher charges, especially for smokers
4. **Regional Variations**: Different regions show varying average charges
5. **Children Impact**: Number of children has minimal impact on charges

## 🔍 Example Output

When you run `main.py`, you'll see:

```
==================================================
HEALTH INSURANCE DATA ANALYSIS REPORT
==================================================

📊 OVERALL STATISTICS
  Total Records: 100
  Average Age: 39.2 years
  Average BMI: 30.66
  Average Charges: $13,270.42
  Median Charges: $9,382.03

🚬 SMOKER IMPACT
  Smoker Percentage: 20.0%
  Smoker Charge Increase: 287.5%

...
```

## 📦 Dependencies

- pandas >= 1.5.0
- numpy >= 1.23.0
- matplotlib >= 3.6.0
- seaborn >= 0.12.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**hidaia175**

## 📞 Contact

For questions or feedback, please open an issue on GitHub.