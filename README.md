# Canadian_Grants_ETL_Project
End-to-End ETL Data Analysis Project: Cleaning messy government financial data using Python, storing in MySQL, and visualizing in Power BI.
# 🇨🇦 Canadian Federal Grants Analysis (ETL & Data Engineering)

![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Data%20Cleaning-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Data%20Warehouse-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📊 Project Overview
This project focuses on **Data Engineering and ETL (Extract, Transform, Load)** processes. I analyzed 10 years of Canadian Government financial grants (2007-2016). The raw data was unstructured ("messy"), containing merged columns, missing values, and formatting errors. I built a Python pipeline to clean the data and creating a dynamic dashboard for financial insights.

### 🎯 Key Objectives
*   **Data Cleaning (Python):** Handling missing values (`NaN`), removing formatting characters (`X`, `...`), and converting data types.
*   **Data Transformation:** Performing **Unpivoting (Melting)** to convert the dataset from "Wide Format" (Years as columns) to "Long Format" suitable for analysis.
*   **Data Warehousing:** Designing a MySQL schema to store over 1,350 financial records.
*   **Visualization:** Tracking spending trends and identifying top-funded programs (e.g., IRAP).

---

## 📸 Dashboard Preview

![Dashboard Screenshot](dashboard_screenshot.png)

---

## 🔄 The ETL Pipeline

1.  **Extract:** Loaded raw CSV data containing unstructured headers and symbols.
2.  **Transform (Python & Pandas):**
    *   Forward-filled missing "Type of Support" values.
    *   Removed sub-headers and footer notes.
    *   **Melted** the dataframe to restructure years into rows.
    *   Cleaned currency columns (removed commas and symbols).
3.  **Load (MySQL):** Injected the clean data into a structured SQL database.
4.  **Visualize (Power BI):** Connected directly to MySQL to build the report.

---

## 🔍 Key Insights
1.  **Total Spending:** Analyzed a total of **$9.51 Billion CAD** in grants and contributions.
2.  **Spending Trend:** A significant spike in government funding was observed post-2010.
3.  **Top Program:** The **IRAP (Industrial Research Assistance Program)** is the largest beneficiary, indicating a strong government focus on R&D innovation.

---

## 🛠️ Tech Stack

| Tool | Usage |
| :--- | :--- |
| **Python (Pandas)** | Used for advanced data cleaning, unpivoting, and string manipulation. |
| **MySQL** | Central repository for the clean dataset. |
| **Power BI** | Financial reporting and trend analysis. |

---

## 👤 Author
**Wael Yousef**
*Data Analyst | Python | SQL | Power BI*

*   🌐 **Portfolio:** [waelanalytics.carrd.co](https://waelanalytics.carrd.co/)
*   💼 **LinkedIn:** [Wael Yousef](https://www.linkedin.com/in/wael-yousef-data-analyst/)
