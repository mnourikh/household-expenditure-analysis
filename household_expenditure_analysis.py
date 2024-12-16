
# Household Expenditure Analysis
# This script processes household expenditure data to calculate savings, income, and expenditure ratios.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_paths):
    '''
    Loads and preprocesses data from the given file paths.

    Parameters:
        file_paths (list): List of file paths for CSV data.

    Returns:
        pd.DataFrame: Combined and preprocessed data.
    '''
    data = pd.DataFrame()
    for file_path in file_paths:
        temp = pd.read_csv(file_path, low_memory=False)
        data = pd.concat([data, temp], ignore_index=True)
    return data

def calculate_ratios(data):
    '''
    Calculates savings and expenditure ratios.

    Parameters:
        data (pd.DataFrame): DataFrame with income, expenditure, and tax columns.

    Returns:
        pd.DataFrame: DataFrame with new ratio columns.
    '''
    data['Savings'] = data['Income'] - data['Expenditure'] - data['Tax']
    data['SavingsRatio'] = data.apply(
        lambda row: row['Savings'] / (row['Income'] - row['Tax']) if row['Income'] != 0 else None, axis=1
    )
    data['FoodExpenditureRatio'] = data['FoodExpenditure'] / data['Expenditure']
    data['HealthExpenditureRatio'] = data['HealthExpenditure'] / data['Expenditure']
    return data

def visualize_ratios(data, ratio_columns, title):
    '''
    Plots specified ratios over time.

    Parameters:
        data (pd.DataFrame): DataFrame with time and ratio columns.
        ratio_columns (list): List of column names to plot.
        title (str): Plot title.
    '''
    data.plot(x='year_quarter', y=ratio_columns, kind='line', title=title)
    plt.show()

if __name__ == "__main__":
    # Load and process data
    file_paths = ['data/fmli2015.csv', 'data/fmli2016.csv']  # Update paths as needed
    data = load_data(file_paths)
    data = calculate_ratios(data)

    # Visualize savings ratio
    savings_ratios = ['SavingsRatio']
    visualize_ratios(data, savings_ratios, "Savings Ratio Over Time")

    # Visualize expenditure ratios
    expenditure_ratios = ['FoodExpenditureRatio', 'HealthExpenditureRatio']
    visualize_ratios(data, expenditure_ratios, "Expenditure Ratios Over Time")
