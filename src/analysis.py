"""
Data Analysis Module for Health Insurance Data
Provides statistical analysis and insights
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional


class HealthInsuranceAnalyzer:
    """Analyzer class for health insurance data"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize analyzer with data
        
        Args:
            data: Processed DataFrame from ETL
        """
        self.data = data
    
    def get_basic_statistics(self) -> pd.DataFrame:
        """
        Get basic statistical summary of numerical columns
        
        Returns:
            DataFrame with descriptive statistics
        """
        return self.data.describe()
    
    def analyze_charges_by_factor(self, factor: str) -> pd.DataFrame:
        """
        Analyze insurance charges by a specific factor
        
        Args:
            factor: Column name to group by (e.g., 'smoker', 'region', 'sex')
            
        Returns:
            DataFrame with average, min, max charges by factor
        """
        if factor not in self.data.columns:
            raise ValueError(f"Factor '{factor}' not found in data")
        
        analysis = self.data.groupby(factor, observed=False)['charges'].agg([
            ('count', 'count'),
            ('mean', 'mean'),
            ('median', 'median'),
            ('std', 'std'),
            ('min', 'min'),
            ('max', 'max')
        ]).round(2)
        
        return analysis
    
    def analyze_smoker_impact(self) -> Dict:
        """
        Analyze the impact of smoking on insurance charges
        
        Returns:
            Dictionary with smoker vs non-smoker statistics
        """
        smoker_data = self.data[self.data['smoker'] == 'yes']['charges']
        non_smoker_data = self.data[self.data['smoker'] == 'no']['charges']
        
        impact = {
            'smoker_avg': smoker_data.mean(),
            'non_smoker_avg': non_smoker_data.mean(),
            'difference': smoker_data.mean() - non_smoker_data.mean(),
            'percentage_increase': ((smoker_data.mean() / non_smoker_data.mean() - 1) * 100),
            'smoker_count': len(smoker_data),
            'non_smoker_count': len(non_smoker_data)
        }
        
        return impact
    
    def analyze_bmi_impact(self) -> pd.DataFrame:
        """
        Analyze the impact of BMI categories on insurance charges
        
        Returns:
            DataFrame with charges by BMI category
        """
        if 'bmi_category' not in self.data.columns:
            raise ValueError("BMI category not found. Ensure ETL transform was run.")
        
        return self.analyze_charges_by_factor('bmi_category')
    
    def analyze_age_impact(self) -> pd.DataFrame:
        """
        Analyze the impact of age on insurance charges
        
        Returns:
            DataFrame with charges by age group
        """
        if 'age_group' not in self.data.columns:
            raise ValueError("Age group not found. Ensure ETL transform was run.")
        
        return self.analyze_charges_by_factor('age_group')
    
    def analyze_regional_differences(self) -> pd.DataFrame:
        """
        Analyze regional differences in insurance charges
        
        Returns:
            DataFrame with charges by region
        """
        return self.analyze_charges_by_factor('region')
    
    def analyze_children_impact(self) -> pd.DataFrame:
        """
        Analyze the impact of number of children on insurance charges
        
        Returns:
            DataFrame with charges by number of children
        """
        return self.analyze_charges_by_factor('children')
    
    def correlation_analysis(self) -> pd.DataFrame:
        """
        Perform correlation analysis on numerical features
        
        Returns:
            Correlation matrix
        """
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        return self.data[numeric_cols].corr().round(3)
    
    def identify_high_risk_profiles(self, threshold_percentile: float = 75) -> pd.DataFrame:
        """
        Identify high-risk profiles (high insurance charges)
        
        Args:
            threshold_percentile: Percentile threshold for high charges
            
        Returns:
            DataFrame with high-risk profiles
        """
        threshold = self.data['charges'].quantile(threshold_percentile / 100)
        high_risk = self.data[self.data['charges'] >= threshold]
        
        return high_risk
    
    def get_key_insights(self) -> Dict[str, any]:
        """
        Generate key insights from the data
        
        Returns:
            Dictionary with key insights
        """
        insights = {}
        
        # Overall statistics
        insights['total_records'] = len(self.data)
        insights['avg_age'] = self.data['age'].mean()
        insights['avg_bmi'] = self.data['bmi'].mean()
        insights['avg_charges'] = self.data['charges'].mean()
        insights['median_charges'] = self.data['charges'].median()
        
        # Smoker impact
        smoker_impact = self.analyze_smoker_impact()
        insights['smoker_percentage'] = (smoker_impact['smoker_count'] / 
                                        (smoker_impact['smoker_count'] + smoker_impact['non_smoker_count']) * 100)
        insights['smoker_charge_increase'] = smoker_impact['percentage_increase']
        
        # Age insights
        insights['youngest_age'] = self.data['age'].min()
        insights['oldest_age'] = self.data['age'].max()
        
        # BMI insights
        insights['min_bmi'] = self.data['bmi'].min()
        insights['max_bmi'] = self.data['bmi'].max()
        
        # Charges insights
        insights['min_charges'] = self.data['charges'].min()
        insights['max_charges'] = self.data['charges'].max()
        insights['charges_range'] = insights['max_charges'] - insights['min_charges']
        
        # Gender distribution
        insights['gender_distribution'] = self.data['sex'].value_counts().to_dict()
        
        # Regional distribution
        insights['regional_distribution'] = self.data['region'].value_counts().to_dict()
        
        return insights
    
    def print_comprehensive_report(self) -> None:
        """Print a comprehensive analysis report"""
        print("\n" + "="*60)
        print("HEALTH INSURANCE DATA ANALYSIS REPORT")
        print("="*60)
        
        # Key insights
        insights = self.get_key_insights()
        
        print("\n📊 OVERALL STATISTICS")
        print(f"  Total Records: {insights['total_records']}")
        print(f"  Average Age: {insights['avg_age']:.1f} years")
        print(f"  Average BMI: {insights['avg_bmi']:.2f}")
        print(f"  Average Charges: ${insights['avg_charges']:,.2f}")
        print(f"  Median Charges: ${insights['median_charges']:,.2f}")
        
        print("\n🚬 SMOKER IMPACT")
        print(f"  Smoker Percentage: {insights['smoker_percentage']:.1f}%")
        print(f"  Smoker Charge Increase: {insights['smoker_charge_increase']:.1f}%")
        
        print("\n👥 DEMOGRAPHICS")
        print(f"  Age Range: {insights['youngest_age']} - {insights['oldest_age']} years")
        print(f"  BMI Range: {insights['min_bmi']:.1f} - {insights['max_bmi']:.1f}")
        print(f"  Gender Distribution: {insights['gender_distribution']}")
        
        print("\n💰 CHARGES ANALYSIS")
        print(f"  Min Charges: ${insights['min_charges']:,.2f}")
        print(f"  Max Charges: ${insights['max_charges']:,.2f}")
        print(f"  Charges Range: ${insights['charges_range']:,.2f}")
        
        print("\n🗺️  REGIONAL DISTRIBUTION")
        for region, count in insights['regional_distribution'].items():
            print(f"  {region.capitalize()}: {count}")
        
        print("\n📈 CHARGES BY SMOKER STATUS")
        print(self.analyze_charges_by_factor('smoker'))
        
        print("\n📈 CHARGES BY REGION")
        print(self.analyze_charges_by_factor('region'))
        
        print("\n📊 CORRELATION ANALYSIS")
        print(self.correlation_analysis())
        
        print("\n" + "="*60)
        print("END OF REPORT")
        print("="*60 + "\n")
