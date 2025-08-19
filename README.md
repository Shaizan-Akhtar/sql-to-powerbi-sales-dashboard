# sql-to-powerbi-sales-dashboard
This project demonstrates a complete data pipeline and business intelligence workflow, starting from data modeling in SQL to data transformation with Python, and finally interactive visualization with Power BI.

1️. Database Creation (SQL):
Designed relational tables: Products, Customers, and Sales.
Established primary & foreign keys to ensure referential integrity.
Inserted sample sales data covering multiple product categories, customers, and regions.

2️. Data Extraction & Transformation (Python + MySQL):
Connected Python to MySQL using PyMySQL.
Extracted sales data from the database.
Performed basic cleaning & transformation to prepare the dataset.
Exported the transformed data into Excel format for visualization.

3️. Data Visualization (Power BI):
Imported the dataset into Power BI Desktop.
Built an interactive dashboard with:
KPIs: Total Sales, Average Sales, Quantity Sold.
Visuals: Sales by Product, Category, Region, and Customer demographics.
Trend Analysis: Monthly and gender-based sales insights.
Added filters/slicers for dynamic exploration of sales by region and category.

Key Insights:
Furniture category recorded the highest sales (~374K).
Lake Sandra emerged as the top-performing city (60K).
Clear seasonal trends and gender-based purchasing patterns were identified.
Regional filters allowed for targeted insights into sales distribution.
