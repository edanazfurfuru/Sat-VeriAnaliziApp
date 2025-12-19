import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from datetime import datetime, timedelta

# Configuration
OUTPUT_DIR = "output"
DATA_FILE = "sales_data.csv"
REPORT_HTML = "report.html"
README_FILE = "README.md"
NUM_RECORDS = 1000

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_data():
    """Generates synthetic sales data."""
    print("Generating data...")
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports']
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for _ in range(NUM_RECORDS):
        date = start_date + timedelta(days=random.randint(0, 365))
        category = random.choice(categories)
        region = random.choice(regions)
        customer_id = f"CUST-{random.randint(100, 200)}"
        sales_amount = round(random.uniform(10.0, 500.0), 2)
        
        data.append([date, category, sales_amount, customer_id, region])
        
    df = pd.DataFrame(data, columns=['Date', 'Category', 'Sales_Amount', 'Customer_ID', 'Region'])
    df.to_csv(DATA_FILE, index=False)
    print(f"Data saved to {DATA_FILE}")
    return df

def analyze_data(df):
    """Performs analysis on the dataframe."""
    print("Analyzing data...")
    
    # ensure date is datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 1. Total Sales by Month
    monthly_sales = df.set_index('Date').resample('ME')['Sales_Amount'].sum()
    
    # 2. Sales by Category
    category_sales = df.groupby('Category')['Sales_Amount'].sum()
    
    # 3. Top 5 Customers
    top_customers = df.groupby('Customer_ID')['Sales_Amount'].sum().sort_values(ascending=False).head(5)
    
    # 4. Key Metrics
    total_revenue = df['Sales_Amount'].sum()
    avg_order_value = df['Sales_Amount'].mean()
    total_orders = len(df)
    
    return {
        'monthly_sales': monthly_sales,
        'category_sales': category_sales,
        'top_customers': top_customers,
        'metrics': {
            'total_revenue': total_revenue,
            'avg_order_value': avg_order_value,
            'total_orders': total_orders
        }
    }

def create_visualizations(analysis_results):
    """Generates and saves plots."""
    print("Creating visualizations...")
    
    # 1. Monthly Sales Line Plot
    plt.figure(figsize=(10, 6))
    analysis_results['monthly_sales'].plot(kind='line', marker='o', color='b')
    plt.title('Monthly Sales Trend (2023)')
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/monthly_sales.png")
    plt.close()
    
    # 2. Category Pie Chart
    plt.figure(figsize=(8, 8))
    analysis_results['category_sales'].plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Sales Distribution by Category')
    plt.ylabel('') # Hide y-label
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/category_distribution.png")
    plt.close()
    
    # 3. Top Customers Bar Chart
    plt.figure(figsize=(10, 6))
    analysis_results['top_customers'].plot(kind='bar', color='green')
    plt.title('Top 5 Customers with Highest Spend')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Spend ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_customers.png")
    plt.close()

def generate_readme(metrics):
    """Generates the README.md file."""
    print("Generating README.md...")
    content = f"""# Annual Sales Analysis Project

## Project Description
The objective of this project is to analyze annual sales data to understand revenue trends, popular product categories, and key customer segments. This insight is crucial for strategic planning for the upcoming fiscal year.

## Features
- **Data Generation**: Creates synthetic sales data for testing and analysis.
- **Data Analysis**: Aggregates sales by month, category, and customer.
- **Visualization**: Generates charts for monthly trends, category distribution, and top customers.
- **Reporting**: Produces an HTML report and this README file.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib
   ```

## Usage

Run the analysis script:
```bash
python analysis.py
```

This will:
1. Generate `sales_data.csv`.
2. Perform analysis.
3. Create visualizations in the `output/` directory.
4. Generate `report.html`.
5. Update this `README.md`.

## File Structure
- `analysis.py`: Main script for data generation, analysis, and reporting.
- `sales_data.csv`: Generated synthetic sales data.
- `output/`: Directory containing generated charts (PNG files).
- `report.html`: Detailed HTML report with tables and charts.
- `README.md`: Project documentation (this file).

## Methodology
- **Tool**: Python (Pandas for data processing, Matplotlib for visualization).
- **Data Source**: Synthetic dataset (`{DATA_FILE}`) containing {NUM_RECORDS} transaction records.
- **Process**:
    1.  Data Cleaning & Preprocessing.
    2.  Aggregating sales by month and category.
    3.  Identifying top-performing customers.
    4.  Visualizing key trends.

## Results & Key Findings
- **Total Revenue generated**: ${metrics['total_revenue']:,.2f}
- **Total Orders processed**: {metrics['total_orders']}
- **Average Order Value**: ${metrics['avg_order_value']:.2f}

Detailed charts and breakdowns can be found in the accompanying [HTML Report](./report.html).
"""
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_html_report(analysis_results):
    """Generates a rich HTML report."""
    print("Generating HTML report...")
    
    metrics = analysis_results['metrics']
    
    # Convert series to HTML tables
    top_cust_html = analysis_results['top_customers'].to_frame(name='Total Spend ($)').to_html(classes='table table-striped')
    cat_sales_html = analysis_results['category_sales'].to_frame(name='Total Sales ($)').to_html(classes='table table-striped')
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Annual Sales Analysis Report</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; color: #333; }}
            .container {{ max-width: 1000px; margin: auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h1, h2 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
            .metrics-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }}
            .metric-card {{ background: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #ddd; }}
            .metric-value {{ font-size: 2em; font-weight: bold; color: #2980b9; }}
            .chart-container {{ margin: 30px 0; text-align: center; }}
            img {{ max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; }}
            .table-container {{ overflow-x: auto; margin-bottom: 20px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #f2f2f2; }}
            .footer {{ margin-top: 50px; text-align: center; font-size: 0.9em; color: #777; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Annual Sales Analysis Report 2023</h1>
            <p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <h2>Executive Summary</h2>
            <div class="metrics-grid">
                <div class="metric-card">
                    <div>Total Revenue</div>
                    <div class="metric-value">${metrics['total_revenue']:,.2f}</div>
                </div>
                <div class="metric-card">
                    <div>Total Orders</div>
                    <div class="metric-value">{metrics['total_orders']}</div>
                </div>
                <div class="metric-card">
                    <div>Avg Order Value</div>
                    <div class="metric-value">${metrics['avg_order_value']:.2f}</div>
                </div>
            </div>

            <h2>Sales Trends</h2>
            <p>The following chart illustrates the monthly sales performance throughout the year.</p>
            <div class="chart-container">
                <img src="output/monthly_sales.png" alt="Monthly Sales Chart">
            </div>

            <h2>Category Performance</h2>
            <div style="display: flex; gap: 20px; align-items: start;">
                <div style="flex: 1;">
                    <p>Sales distribution across different product categories.</p>
                    <div class="table-container">{cat_sales_html}</div>
                </div>
                <div style="flex: 1;" class="chart-container">
                    <img src="output/category_distribution.png" alt="Category Distribution">
                </div>
            </div>

            <h2>Customer Insights</h2>
            <p>Top 5 customers contributing the most to revenue.</p>
            <div style="display: flex; gap: 20px; align-items: start;">
                <div style="flex: 1;" class="chart-container">
                    <img src="output/top_customers.png" alt="Top Customers">
                </div>
                 <div style="flex: 1;">
                    <br><br>
                    <div class="table-container">{top_cust_html}</div>
                </div>
            </div>

            <div class="footer">
                <p>Generated by Automated Analysis System (Python/Matplotlib)</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(REPORT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Report saved to {REPORT_HTML}")

def main():
    df = generate_data()
    results = analyze_data(df)
    create_visualizations(results)
    generate_readme(results['metrics'])
    generate_html_report(results)
    print("Project run complete successfully.")

if __name__ == "__main__":
    main()
