"""
Data Visualization Module for Health Insurance Data
Creates comprehensive visualizations and charts
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, List
import os


class HealthInsuranceVisualizer:
    """Visualizer class for health insurance data"""
    
    def __init__(self, data: pd.DataFrame, output_dir: str = 'outputs'):
        """
        Initialize visualizer with data
        
        Args:
            data: Processed DataFrame from ETL
            output_dir: Directory to save visualizations
        """
        self.data = data
        self.output_dir = output_dir
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
    
    def plot_charges_distribution(self, save: bool = True) -> None:
        """
        Plot distribution of insurance charges
        
        Args:
            save: Whether to save the plot
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Histogram
        axes[0].hist(self.data['charges'], bins=50, edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Charges ($)')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title('Distribution of Insurance Charges')
        axes[0].grid(True, alpha=0.3)
        
        # Box plot
        axes[1].boxplot(self.data['charges'])
        axes[1].set_ylabel('Charges ($)')
        axes[1].set_title('Box Plot of Insurance Charges')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filepath = os.path.join(self.output_dir, 'charges_distribution.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_smoker_impact(self, save: bool = True) -> None:
        """
        Plot impact of smoking on charges
        
        Args:
            save: Whether to save the plot
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Bar plot of average charges
        smoker_avg = self.data.groupby('smoker', observed=False)['charges'].mean()
        axes[0].bar(smoker_avg.index, smoker_avg.values, color=['green', 'red'], alpha=0.7)
        axes[0].set_xlabel('Smoker Status')
        axes[0].set_ylabel('Average Charges ($)')
        axes[0].set_title('Average Insurance Charges by Smoker Status')
        axes[0].grid(True, alpha=0.3, axis='y')
        
        # Box plot
        smoker_data = [self.data[self.data['smoker'] == 'no']['charges'],
                      self.data[self.data['smoker'] == 'yes']['charges']]
        axes[1].boxplot(smoker_data, labels=['No', 'Yes'])
        axes[1].set_xlabel('Smoker Status')
        axes[1].set_ylabel('Charges ($)')
        axes[1].set_title('Distribution of Charges by Smoker Status')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save:
            filepath = os.path.join(self.output_dir, 'smoker_impact.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_age_vs_charges(self, save: bool = True) -> None:
        """
        Plot relationship between age and charges
        
        Args:
            save: Whether to save the plot
        """
        plt.figure(figsize=(12, 6))
        
        # Scatter plot with different colors for smokers
        for smoker in ['yes', 'no']:
            subset = self.data[self.data['smoker'] == smoker]
            plt.scatter(subset['age'], subset['charges'], 
                       label=f'Smoker: {smoker}',
                       alpha=0.6, s=50)
        
        plt.xlabel('Age (years)')
        plt.ylabel('Charges ($)')
        plt.title('Insurance Charges vs Age (by Smoker Status)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save:
            filepath = os.path.join(self.output_dir, 'age_vs_charges.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_bmi_vs_charges(self, save: bool = True) -> None:
        """
        Plot relationship between BMI and charges
        
        Args:
            save: Whether to save the plot
        """
        plt.figure(figsize=(12, 6))
        
        # Scatter plot with different colors for smokers
        for smoker in ['yes', 'no']:
            subset = self.data[self.data['smoker'] == smoker]
            plt.scatter(subset['bmi'], subset['charges'], 
                       label=f'Smoker: {smoker}',
                       alpha=0.6, s=50)
        
        plt.xlabel('BMI')
        plt.ylabel('Charges ($)')
        plt.title('Insurance Charges vs BMI (by Smoker Status)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save:
            filepath = os.path.join(self.output_dir, 'bmi_vs_charges.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_regional_analysis(self, save: bool = True) -> None:
        """
        Plot regional analysis of charges
        
        Args:
            save: Whether to save the plot
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Average charges by region
        region_avg = self.data.groupby('region', observed=False)['charges'].mean().sort_values()
        axes[0].barh(region_avg.index, region_avg.values, alpha=0.7)
        axes[0].set_xlabel('Average Charges ($)')
        axes[0].set_ylabel('Region')
        axes[0].set_title('Average Insurance Charges by Region')
        axes[0].grid(True, alpha=0.3, axis='x')
        
        # Count by region
        region_count = self.data['region'].value_counts()
        axes[1].bar(region_count.index, region_count.values, alpha=0.7)
        axes[1].set_xlabel('Region')
        axes[1].set_ylabel('Count')
        axes[1].set_title('Number of Records by Region')
        axes[1].grid(True, alpha=0.3, axis='y')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        if save:
            filepath = os.path.join(self.output_dir, 'regional_analysis.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_bmi_categories(self, save: bool = True) -> None:
        """
        Plot analysis of BMI categories
        
        Args:
            save: Whether to save the plot
        """
        if 'bmi_category' not in self.data.columns:
            print("Warning: BMI category not found. Skipping this visualization.")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Average charges by BMI category
        bmi_avg = self.data.groupby('bmi_category', observed=False)['charges'].mean()
        axes[0].bar(range(len(bmi_avg)), bmi_avg.values, alpha=0.7)
        axes[0].set_xticks(range(len(bmi_avg)))
        axes[0].set_xticklabels(bmi_avg.index, rotation=45)
        axes[0].set_xlabel('BMI Category')
        axes[0].set_ylabel('Average Charges ($)')
        axes[0].set_title('Average Insurance Charges by BMI Category')
        axes[0].grid(True, alpha=0.3, axis='y')
        
        # Distribution by BMI category
        bmi_count = self.data['bmi_category'].value_counts()
        axes[1].pie(bmi_count.values, labels=bmi_count.index, autopct='%1.1f%%', startangle=90)
        axes[1].set_title('Distribution of BMI Categories')
        
        plt.tight_layout()
        
        if save:
            filepath = os.path.join(self.output_dir, 'bmi_categories.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_correlation_heatmap(self, save: bool = True) -> None:
        """
        Plot correlation heatmap of numerical features
        
        Args:
            save: Whether to save the plot
        """
        plt.figure(figsize=(10, 8))
        
        # Select numerical columns
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        correlation = self.data[numeric_cols].corr()
        
        # Create heatmap
        sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0,
                   square=True, linewidths=1, fmt='.2f')
        
        plt.title('Correlation Heatmap of Numerical Features')
        plt.tight_layout()
        
        if save:
            filepath = os.path.join(self.output_dir, 'correlation_heatmap.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def plot_children_impact(self, save: bool = True) -> None:
        """
        Plot impact of number of children on charges
        
        Args:
            save: Whether to save the plot
        """
        plt.figure(figsize=(12, 6))
        
        children_avg = self.data.groupby('children', observed=False)['charges'].mean()
        
        plt.bar(children_avg.index, children_avg.values, alpha=0.7)
        plt.xlabel('Number of Children')
        plt.ylabel('Average Charges ($)')
        plt.title('Average Insurance Charges by Number of Children')
        plt.grid(True, alpha=0.3, axis='y')
        
        if save:
            filepath = os.path.join(self.output_dir, 'children_impact.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {filepath}")
        
        plt.show()
    
    def create_comprehensive_dashboard(self, save: bool = True) -> None:
        """
        Create a comprehensive dashboard with multiple visualizations
        
        Args:
            save: Whether to save the dashboard
        """
        print("\n" + "="*50)
        print("Creating Comprehensive Visualization Dashboard")
        print("="*50 + "\n")
        
        self.plot_charges_distribution(save=save)
        self.plot_smoker_impact(save=save)
        self.plot_age_vs_charges(save=save)
        self.plot_bmi_vs_charges(save=save)
        self.plot_regional_analysis(save=save)
        self.plot_bmi_categories(save=save)
        self.plot_correlation_heatmap(save=save)
        self.plot_children_impact(save=save)
        
        print("\n" + "="*50)
        print("Dashboard Creation Complete!")
        print("="*50 + "\n")
