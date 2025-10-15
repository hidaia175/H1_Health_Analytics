"""
Main script to run the complete Health Insurance Analytics pipeline
Demonstrates ETL, Analysis, and Visualization
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from etl import HealthInsuranceETL
from analysis import HealthInsuranceAnalyzer
from visualization import HealthInsuranceVisualizer


def main():
    """Main function to run the complete analytics pipeline"""
    
    print("\n" + "="*60)
    print("H1 HEALTH ANALYTICS - INSURANCE COST ANALYSIS")
    print("="*60 + "\n")
    
    # Step 1: ETL Pipeline
    print("STEP 1: ETL Pipeline")
    print("-" * 60)
    
    etl = HealthInsuranceETL()
    processed_data = etl.run_pipeline(output_path='data/processed_insurance.csv')
    
    # Step 2: Data Analysis
    print("\nSTEP 2: Data Analysis")
    print("-" * 60)
    
    analyzer = HealthInsuranceAnalyzer(processed_data)
    analyzer.print_comprehensive_report()
    
    # Step 3: Data Visualization
    print("\nSTEP 3: Data Visualization")
    print("-" * 60)
    
    visualizer = HealthInsuranceVisualizer(processed_data, output_dir='outputs')
    visualizer.create_comprehensive_dashboard(save=True)
    
    # Print summary
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print("\nOutputs saved to:")
    print("  - Processed data: data/processed_insurance.csv")
    print("  - Visualizations: outputs/")
    print("\n")


if __name__ == "__main__":
    main()
