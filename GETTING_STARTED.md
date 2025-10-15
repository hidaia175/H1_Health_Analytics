# Getting Started with H1 Health Analytics

This guide will help you get started with the H1 Health Analytics project.

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/hidaia175/H1_Health_Analytics.git
cd H1_Health_Analytics

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Complete Pipeline

The easiest way to get started is to run the main script:

```bash
python main.py
```

This will:
- Extract and transform the insurance data
- Generate a comprehensive analysis report
- Create visualizations (saved to `outputs/` directory)
- Save processed data to `data/processed_insurance.csv`

### 3. Expected Output

When you run the pipeline, you'll see:

1. **ETL Progress**: Extract → Transform → Load steps
2. **Analysis Report**: Statistical insights and key findings
3. **Visualizations**: Multiple charts saved to the outputs folder

## Using Individual Modules

### ETL Module Example

```python
from src.etl import HealthInsuranceETL

# Initialize and run ETL
etl = HealthInsuranceETL('data/insurance.csv')
processed_data = etl.run_pipeline(output_path='data/output.csv')

# Get data summary
summary = etl.get_data_summary()
print(summary)
```

### Analysis Module Example

```python
from src.analysis import HealthInsuranceAnalyzer

# Initialize analyzer
analyzer = HealthInsuranceAnalyzer(processed_data)

# Get various analyses
basic_stats = analyzer.get_basic_statistics()
smoker_impact = analyzer.analyze_smoker_impact()
regional_diff = analyzer.analyze_regional_differences()
correlations = analyzer.correlation_analysis()

# Print comprehensive report
analyzer.print_comprehensive_report()
```

### Visualization Module Example

```python
from src.visualization import HealthInsuranceVisualizer

# Initialize visualizer
visualizer = HealthInsuranceVisualizer(
    processed_data, 
    output_dir='outputs'
)

# Create individual visualizations
visualizer.plot_charges_distribution(save=True)
visualizer.plot_smoker_impact(save=True)
visualizer.plot_age_vs_charges(save=True)

# Or create all visualizations at once
visualizer.create_comprehensive_dashboard(save=True)
```

## Using Jupyter Notebook

Open the example notebook:

```bash
jupyter notebook notebooks/health_insurance_analysis.ipynb
```

The notebook demonstrates all features with interactive visualizations.

## Project Structure Explained

```
H1_Health_Analytics/
├── data/                          # Data directory
│   └── insurance.csv             # Raw insurance data
│
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── etl.py                   # ETL pipeline
│   ├── analysis.py              # Data analysis
│   └── visualization.py         # Visualizations
│
├── notebooks/                    # Jupyter notebooks
│   └── health_insurance_analysis.ipynb
│
├── outputs/                      # Generated visualizations
│   ├── charges_distribution.png
│   ├── smoker_impact.png
│   └── ... (other charts)
│
├── main.py                       # Main pipeline script
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```

## Key Features

### 1. ETL Pipeline
- **Extract**: Load data from CSV
- **Transform**: Clean data, create derived features
- **Load**: Save processed data

### 2. Analysis Capabilities
- Basic statistical summary
- Smoker impact analysis
- BMI impact analysis
- Age impact analysis
- Regional differences
- Correlation analysis
- High-risk profile identification

### 3. Visualizations
- Distribution plots
- Box plots
- Scatter plots
- Bar charts
- Pie charts
- Heatmaps

## Common Tasks

### Add Your Own Data

Replace `data/insurance.csv` with your own CSV file (must have the same columns):
- age
- sex
- bmi
- children
- smoker
- region
- charges

### Customize Analysis

Edit the analysis module to add your own metrics:

```python
# In src/analysis.py
def custom_analysis(self) -> dict:
    """Your custom analysis logic"""
    # Add your code here
    pass
```

### Add New Visualizations

Edit the visualization module:

```python
# In src/visualization.py
def plot_custom_chart(self, save: bool = True) -> None:
    """Create a custom visualization"""
    # Add your code here
    pass
```

## Troubleshooting

### Import Errors

If you get import errors, make sure you're running from the project root:

```bash
cd /path/to/H1_Health_Analytics
python main.py
```

### Visualization Issues

If plots don't display, install the matplotlib backend:

```bash
pip install pyqt5
```

Or use the non-interactive backend in your script:

```python
import matplotlib
matplotlib.use('Agg')
```

### Missing Dependencies

Reinstall all dependencies:

```bash
pip install -r requirements.txt --upgrade
```

## Next Steps

1. Explore the example notebook
2. Run the main pipeline with your own data
3. Customize the analysis for your specific needs
4. Create additional visualizations
5. Share your insights!

## Support

For questions or issues, please open an issue on GitHub.
