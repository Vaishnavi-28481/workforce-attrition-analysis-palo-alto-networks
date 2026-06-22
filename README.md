# Workforce Attrition Patterns and Risk Hotspot Analysis

## Project Overview
This project analyzes workforce attrition patterns at Palo Alto Networks using employee demographic, career, and workload-related data. The objective is to identify attrition hotspots and provide data-driven recommendations for employee retention.

## Problem Statement
Employee attrition leads to loss of talent, increased hiring costs, and reduced productivity. This project identifies departments, job roles, demographics, and workload factors associated with employee turnover.

## Dataset Information
- Records: 1470
- Features: 31
- Target Variable: Attrition (0 = Retained, 1 = Left)

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Key Performance Indicators
- Total Employees: 1470
- Employees Left: 237
- Attrition Rate: 16.12%
- Retention Rate: 83.88%

## Key Findings
- Research & Development and Sales departments showed higher attrition.
- Sales Executive and Laboratory Technician roles experienced higher employee exits.
- Employees aged 26–35 showed the highest attrition.
- Overtime significantly increased attrition risk.
- Frequent business travel contributed to employee turnover.
- Single employees had higher attrition compared to married employees.

## Recommendations
- Reduce excessive overtime.
- Strengthen employee career development programs.
- Focus retention efforts on high-risk departments and job roles.
- Improve promotion opportunities.
- Review travel requirements for frequently traveling employees.

## Project Structure
```text
um_work_p2/
│
├── images/
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── Workforce_Attrition_Report.pdf
│
├── data/
│   └── cleaned_attrition.csv
    └── Palo Alto Networks.csv