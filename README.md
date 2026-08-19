# Sales Performance & Customer Segmentation Analytics

**Kinetrexa Software Pvt. Ltd. — Data Analytics Internship**
Applicant: Siva Prakash V · Application ID: `KTS020260712195`
Covers **Task 1 (Sales Performance Dashboard)** and **Task 2 (Customer Segmentation Analysis)**.

---

## 🔍 Overview

This project analyzes 24 months (Aug 2024 – Jul 2026) of e-commerce sales data — 6,000+ transactions
across 850 customers, 4 regions and 5 product categories — to answer two business questions:

1. **Sales Performance** — where is revenue coming from, which products/regions perform best, and how is it trending?
2. **Customer Segmentation** — which customers are most valuable, and how should marketing be targeted at each group?

## 📁 Project Structure

```
├── data/
│   ├── generate_data.py           # Script that generates the synthetic dataset
│   ├── sales_data.csv             # 6,015 order line items
│   └── customers.csv              # 850 customer records
│
├── notebooks/
│   ├── 01_sales_performance_dashboard.ipynb     # Task 1: cleaning, KPIs, trends, product & regional analysis
│   └── 02_customer_segmentation_analysis.ipynb  # Task 2: RFM analysis + K-Means clustering
│
├── dashboard/
│   └── index.html                 # Interactive dashboard (Chart.js) — deployable to Vercel/Netlify
│
├── reports/
│   ├── build_report.py            # Script that generates the PDF report
│   ├── Business_Insights_Report.pdf
│   └── *.csv / *.png              # Exported summary tables & charts used by the report/dashboard
│
├── requirements.txt
└── README.md
```

## 📊 Key Results

| Metric | Value |
|---|---|
| Total Revenue | ₹5.93 Cr |
| Total Orders | 5,755 |
| Unique Customers | 777 |
| Avg Order Value | ₹10,297 |
| Return Rate | 4.08% |
| Top Segment ("Champions") | 242 customers → 67% of revenue |

Full findings and recommendations are in [`reports/Business_Insights_Report.pdf`](reports/Business_Insights_Report.pdf).

## 🛠 Tech Stack

- **Python** — pandas, numpy, matplotlib, seaborn, plotly, scikit-learn (K-Means, StandardScaler)
- **Jupyter Notebook** — analysis & documentation
- **Chart.js (HTML/CSS/JS)** — interactive dashboard, static-hostable
- **ReportLab** — PDF report generation

## ▶️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Regenerate the dataset
cd data && python generate_data.py && cd ..

# 4. Launch Jupyter and run the notebooks
jupyter notebook notebooks/

# 5. View the dashboard locally
cd dashboard && python -m http.server 8000
# then open http://localhost:8000 in your browser
```

## 🌐 Live Deployment

The `dashboard/` folder is a static site (no build step) and can be deployed directly to
**Vercel** or **Netlify** — see the deployment guide provided alongside this project for
step-by-step instructions.

## 📈 Methodology Summary

**Task 1 — Sales Performance Dashboard**
- Cleaned duplicate rows and imputed missing values (discount %, rating)
- Computed core KPIs: revenue, orders, AOV, return rate, avg rating
- Analyzed monthly revenue trend, category/product performance, and regional/city breakdown

**Task 2 — Customer Segmentation Analysis**
- Engineered RFM features (Recency, Frequency, Monetary) per customer
- Rule-based RFM scoring (quartile-based) **and** unsupervised K-Means clustering (k=4, chosen via elbow method)
- Profiled each segment (Champions, Loyal Customers, Potential Loyalists, At Risk) and produced targeted recommendations

## 📄 Deliverables Checklist

- [x] Public GitHub Repository
- [x] Source Code / Jupyter Notebooks (Task 1 & Task 2)
- [x] Interactive Dashboard (`dashboard/index.html`)
- [x] README Documentation
- [x] Business Insights Report (PDF)

---
*Built as part of the Data Analytics Internship task assignment from Kinetrexa Software Pvt. Ltd.*
