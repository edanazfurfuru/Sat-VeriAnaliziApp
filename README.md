# Annual Sales Analysis Project

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
- **Data Source**: Synthetic dataset (`sales_data.csv`) containing 1000 transaction records.
- **Process**:
    1.  Data Cleaning & Preprocessing.
    2.  Aggregating sales by month and category.
    3.  Identifying top-performing customers.
    4.  Visualizing key trends.

## Results & Key Findings
- **Total Revenue generated**: $257,338.50
- **Total Orders processed**: 1000
- **Average Order Value**: $257.34

Detailed charts and breakdowns can be found in the accompanying [HTML Report](./report.html).
