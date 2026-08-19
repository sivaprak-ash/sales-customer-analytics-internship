from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 Image, PageBreak, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBig", fontSize=22, leading=26, fontName="Helvetica-Bold",
                           textColor=colors.HexColor("#0A0F1A"), spaceAfter=6))
styles.add(ParagraphStyle(name="Subtitle", fontSize=11, leading=15, fontName="Helvetica",
                           textColor=colors.HexColor("#555555"), spaceAfter=14))
styles.add(ParagraphStyle(name="H2", fontSize=14, leading=18, fontName="Helvetica-Bold",
                           textColor=colors.HexColor("#0F172A"), spaceBefore=16, spaceAfter=8))
styles.add(ParagraphStyle(name="Body", fontSize=10, leading=15, fontName="Helvetica",
                           textColor=colors.HexColor("#222222")))
styles.add(ParagraphStyle(name="RecBullet", fontSize=10, leading=15, fontName="Helvetica",
                           textColor=colors.HexColor("#222222"), leftIndent=14, bulletIndent=2))

doc = SimpleDocTemplate("Business_Insights_Report.pdf", pagesize=A4,
                         topMargin=2.2*cm, bottomMargin=2*cm, leftMargin=2*cm, rightMargin=2*cm)

story = []

# ---- Cover ----
story.append(Paragraph("Sales Performance & Customer Segmentation", styles["TitleBig"]))
story.append(Paragraph("Business Insights Report — Data Analytics Internship", styles["Subtitle"]))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2DD4BF")))
story.append(Spacer(1, 10))
story.append(Paragraph("Prepared for: Kinetrexa Software Pvt. Ltd.", styles["Body"]))
story.append(Paragraph("Applicant: Siva Prakash V &nbsp;|&nbsp; Application ID: KTS020260712195", styles["Body"]))
story.append(Paragraph("Internship Domain: Data Analytics Internship &nbsp;|&nbsp; Duration: 20 Jul 2026 – 19 Aug 2026", styles["Body"]))
story.append(Spacer(1, 18))

# ---- Executive Summary ----
story.append(Paragraph("Executive Summary", styles["H2"]))
story.append(Paragraph(
    "This report analyzes 24 months of e-commerce sales transactions (Aug 2024 – Jul 2026) covering "
    "5,755 valid orders from 777 unique customers across four regions of India. The analysis combines "
    "a Sales Performance study (revenue trends, product and regional performance) with a Customer "
    "Segmentation study (RFM analysis and K-Means clustering) to surface actionable, data-driven "
    "recommendations for revenue growth and customer retention.", styles["Body"]))
story.append(Spacer(1, 10))

# ---- KPI table ----
kpi_data = [
    ["Metric", "Value"],
    ["Total Revenue", "Rs. 5,92,60,020 (~5.93 Cr)"],
    ["Total Orders", "5,755"],
    ["Unique Customers", "777"],
    ["Average Order Value", "Rs. 10,297"],
    ["Return Rate", "4.08%"],
    ["Average Customer Rating", "3.9 / 5"],
]
t = Table(kpi_data, colWidths=[8*cm, 8*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0A0F1A")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F3F6FA")]),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#D8DEE8")),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(Spacer(1, 10))

# ---- Monthly revenue chart ----
story.append(Paragraph("Revenue Trend", styles["H2"]))
story.append(Paragraph(
    "Revenue shows clear seasonality, peaking every October–November festive period and again in "
    "January new-year sales. The highest month on record is October 2025 at approximately Rs. 47.5 lakh.",
    styles["Body"]))
story.append(Spacer(1, 6))
story.append(Image("monthly_revenue_trend.png", width=16.5*cm, height=8.2*cm))
story.append(Spacer(1, 8))

# ---- Category / Region tables ----
story.append(Paragraph("Category & Regional Performance", styles["H2"]))

cat_data = [["Category", "Revenue (Rs.)"],
            ["Electronics", "3,65,95,797"],
            ["Home & Kitchen", "1,02,81,254"],
            ["Sports & Fitness", "55,84,528"],
            ["Fashion", "42,25,946"],
            ["Beauty & Personal Care", "25,72,494"]]
reg_data = [["Region", "Revenue (Rs.)", "Orders"],
            ["North", "1,75,74,099", "1,712"],
            ["West", "1,44,53,703", "1,403"],
            ["South", "1,37,96,185", "1,359"],
            ["East", "1,34,36,033", "1,281"]]

def make_table(data, widths):
    tt = Table(data, colWidths=widths)
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#111A2C")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F3F6FA")]),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#D8DEE8")),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
    ]))
    return tt

tbl_row = Table([[make_table(cat_data, [4.6*cm, 3.4*cm]), make_table(reg_data, [3*cm, 3.4*cm, 2*cm])]],
                 colWidths=[8.2*cm, 8.4*cm])
tbl_row.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP")]))
story.append(tbl_row)
story.append(Spacer(1, 10))

story.append(Paragraph(
    "Electronics dominates revenue (61.7% of total), led by Laptops, Wireless Earbuds and Smartphones. "
    "The North region is the top revenue contributor, followed closely by West, South and East — "
    "indicating a fairly balanced but North-leaning demand base.", styles["Body"]))

story.append(PageBreak())

# ---- Customer Segmentation ----
story.append(Paragraph("Customer Segmentation (RFM Analysis)", styles["H2"]))
story.append(Paragraph(
    "Customers were segmented using Recency, Frequency and Monetary (RFM) features with K-Means "
    "clustering (k=4, chosen via the elbow method). Four distinct segments emerged:", styles["Body"]))
story.append(Spacer(1, 6))

seg_data = [
    ["Segment", "Customers", "Avg Recency", "Avg Frequency", "Avg Monetary", "Total Revenue"],
    ["Champions", "242", "57 days", "15.3 orders", "Rs. 1,64,488", "Rs. 3,98,06,010"],
    ["Loyal Customers", "284", "126 days", "5.5 orders", "Rs. 56,381", "Rs. 1,60,12,162"],
    ["At Risk", "160", "194 days", "2.2 orders", "Rs. 11,982", "Rs. 19,17,176"],
    ["Potential Loyalists", "91", "514 days", "1.6 orders", "Rs. 16,755", "Rs. 15,24,671"],
]
story.append(make_table(seg_data, [3.4*cm, 2.2*cm, 2.4*cm, 2.4*cm, 2.6*cm, 3.2*cm]))
story.append(Spacer(1, 10))

story.append(Paragraph(
    "Champions represent just 31% of customers but generate roughly 67% of total revenue — a classic "
    "Pareto pattern. At Risk and Potential Loyalist segments together account for 251 customers who "
    "have not purchased recently and are the priority targets for win-back campaigns.", styles["Body"]))
story.append(Spacer(1, 14))

# ---- Recommendations ----
story.append(Paragraph("Business Recommendations", styles["H2"]))
recs = [
    "<b>Protect and grow Champions:</b> introduce a VIP/loyalty tier with early access and exclusive "
    "discounts — this segment already drives two-thirds of revenue from under a third of customers.",
    "<b>Convert Loyal Customers into Champions:</b> personalized upsell and cross-category bundles "
    "(e.g. Electronics + Home & Kitchen) can lift order frequency.",
    "<b>Win back At Risk customers:</b> time-boxed discount codes and reminder emails before the "
    "194-day average recency window closes the door entirely.",
    "<b>Re-engage Potential Loyalists</b> with a second-purchase incentive — this group has only ordered "
    "once on average and needs a nudge to return.",
    "<b>Double down on Electronics in the North region</b> during Oct–Nov and January, when seasonal "
    "demand peaks by 60-90% over baseline months.",
    "<b>Investigate the 4.08% return rate</b> by category to identify and fix quality or sizing/fit "
    "issues before they erode margins further.",
]
for r in recs:
    story.append(Paragraph("&bull; " + r, styles["RecBullet"]))
    story.append(Spacer(1, 4))

story.append(Spacer(1, 16))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#D8DEE8")))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Methodology: Data was cleaned (duplicates removed, missing values imputed), analyzed in Python "
    "(pandas, matplotlib, seaborn, scikit-learn) inside Jupyter notebooks, and visualized in an "
    "interactive HTML dashboard. Full analysis code is available in the accompanying GitHub repository.",
    styles["Body"]))

doc.build(story)
print("Report generated: Business_Insights_Report.pdf")
