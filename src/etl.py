"""
ETL Module for Health Insurance Data
Handles extraction, transformation, and loading of health insurance data
"""

import pandas as pd
import numpy as np
from typing import Optional
import os


class HealthInsuranceETL:
    """ETL class for processing health insurance data"""
    
    def __init__(self, data_path: str = None):
        """
        Initialize ETL with data path
        
        Args:
            data_path: Path to the CSV data file
        """
        if data_path is None:
            # Default to data/insurance.csv in project root
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_path = os.path.join(project_root, 'data', 'insurance.csv')
        
        self.data_path = data_path
        self.raw_data = None
        self.processed_data = None
    
    def extract(self) -> pd.DataFrame:
        """
        Extract data from CSV file
        
        Returns:
            Raw DataFrame
        """
        try:
            self.raw_data = pd.read_csv(self.data_path)
            print(f"✓ Extracted {len(self.raw_data)} records from {self.data_path}")
            return self.raw_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise Exception(f"Error extracting data: {str(e)}")
    
    def transform(self, data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Transform and clean the data
        
        Args:
            data: DataFrame to transform (uses raw_data if None)
            
        Returns:
            Transformed DataFrame
        """
        if data is None:
            if self.raw_data is None:
                raise ValueError("No data available. Run extract() first.")
            data = self.raw_data.copy()
        else:
            data = data.copy()
        
        # Handle missing values
        initial_rows = len(data)
        data = data.dropna()
        removed_rows = initial_rows - len(data)
        if removed_rows > 0:
            print(f"✓ Removed {removed_rows} rows with missing values")
        
        # Convert categorical variables to proper types
        data['sex'] = data['sex'].astype('category')
        data['smoker'] = data['smoker'].astype('category')
        data['region'] = data['region'].astype('category')
        
        # Create additional features
        # BMI categories
        data['bmi_category'] = pd.cut(
            data['bmi'],
            bins=[0, 18.5, 25, 30, 100],
            labels=['Underweight', 'Normal', 'Overweight', 'Obese']
        )
        
        # Age groups
        data['age_group'] = pd.cut(
            data['age'],
            bins=[0, 25, 35, 45, 55, 100],
            labels=['18-25', '26-35', '36-45', '46-55', '56+']
        )
        
        # Convert smoker to binary
        data['is_smoker'] = (data['smoker'] == 'yes').astype(int)
        
        # Calculate charges per person (useful metric)
        data['charges_per_person'] = data['charges'] / (data['children'] + 1)
        
        print(f"✓ Transformed data with {len(data)} records and {len(data.columns)} features")
        
        self.processed_data = data
        return data
    
    def load(self, output_path: str, data: Optional[pd.DataFrame] = None) -> None:
        """
        Load processed data to CSV file
        
        Args:
            output_path: Path to save the processed data
            data: DataFrame to save (uses processed_data if None)
        """
        if data is None:
            if self.processed_data is None:
                raise ValueError("No processed data available. Run transform() first.")
            data = self.processed_data
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        data.to_csv(output_path, index=False)
        print(f"✓ Loaded {len(data)} records to {output_path}")
    
    def run_pipeline(self, output_path: Optional[str] = None) -> pd.DataFrame:
        """
        Run the complete ETL pipeline
        
        Args:
            output_path: Optional path to save processed data
            
        Returns:
            Processed DataFrame
        """
        print("\n" + "="*50)
        print("Running ETL Pipeline")
        print("="*50)
        
        # Extract
        print("\n[1/3] Extracting data...")
        self.extract()
        
        # Transform
        print("\n[2/3] Transforming data...")
        self.transform()
        
        # Load
        if output_path:
            print("\n[3/3] Loading data...")
            self.load(output_path)
        else:
            print("\n[3/3] Skipping load step (no output path provided)")
        
        print("\n" + "="*50)
        print("ETL Pipeline Complete!")
        print("="*50 + "\n")
        
        return self.processed_data
    
    def get_data_summary(self) -> dict:
        """
        Get summary statistics of the processed data
        
        Returns:
            Dictionary with summary statistics
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Run transform() first.")
        
        data = self.processed_data
        
        summary = {
            'total_records': len(data),
            'total_features': len(data.columns),
            'numeric_features': data.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_features': data.select_dtypes(include=['category', 'object']).columns.tolist(),
            'missing_values': data.isnull().sum().to_dict(),
            'data_types': data.dtypes.astype(str).to_dict()
        }
        
        return summary
