"""
Generates a realistic synthetic e-commerce sales dataset used for both
Task 1 (Sales Performance Dashboard) and Task 2 (Customer Segmentation Analysis).

Run: python generate_data.py
Output: sales_data.csv
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

# ---------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------
regions = {
    "North":  ["Delhi", "Chandigarh", "Lucknow", "Jaipur"],
    "South":  ["Chennai", "Bengaluru", "Hyderabad", "Kochi"],
    "East":   ["Kolkata", "Patna", "Bhubaneswar", "Guwahati"],
    "West":   ["Mumbai", "Pune", "Ahmedabad", "Surat"],
}

categories = {
    "Electronics":    ["Wireless Earbuds", "Smartphone", "Laptop", "Smartwatch", "Bluetooth Speaker"],
    "Home & Kitchen":  ["Air Fryer", "Mixer Grinder", "Vacuum Cleaner", "Non-Stick Cookware Set", "Water Purifier"],
    "Fashion":        ["Running Shoes", "Backpack", "Denim Jacket", "Sunglasses", "Wrist Watch"],
    "Beauty & Personal Care": ["Face Serum", "Hair Dryer", "Trimmer", "Perfume", "Skincare Kit"],
    "Sports & Fitness": ["Yoga Mat", "Dumbbell Set", "Cycling Helmet", "Fitness Band", "Resistance Bands"],
}

category_price_range = {
    "Electronics": (1200, 55000),
    "Home & Kitchen": (900, 15000),
    "Fashion": (400, 6000),
    "Beauty & Personal Care": (250, 3500),
    "Sports & Fitness": (300, 8000),
}

payment_methods = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]
customer_segments_seed = ["New", "Returning"]  # will be recomputed later from behavior, this is just acquisition channel
acquisition_channel = ["Organic Search", "Paid Ads", "Social Media", "Referral", "Email Campaign"]

N_CUSTOMERS = 850
N_ORDERS = 6000

# ---------------------------------------------------------------
# Customers
# ---------------------------------------------------------------
first_names = ["Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Reyansh","Krishna","Ishaan","Rohan",
               "Ananya","Diya","Isha","Kavya","Meera","Priya","Riya","Saanvi","Tara","Zara",
               "Rahul","Karthik","Suresh","Vikram","Anil","Deepak","Manish","Naveen","Ramesh","Sanjay",
               "Neha","Pooja","Shreya","Sneha","Divya","Kiran","Lakshmi","Manisha","Nisha","Swati"]
last_names = ["Sharma","Verma","Iyer","Nair","Reddy","Rao","Gupta","Singh","Patel","Kumar",
              "Menon","Pillai","Chopra","Malhotra","Kapoor","Bose","Das","Mukherjee","Joshi","Desai"]

cust_ids = [f"CUST{str(i).zfill(4)}" for i in range(1, N_CUSTOMERS + 1)]
customers = pd.DataFrame({
    "customer_id": cust_ids,
    "customer_name": [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in cust_ids],
    "region": [np.random.choice(list(regions.keys())) for _ in cust_ids],
    "age": np.random.randint(18, 65, size=N_CUSTOMERS),
    "gender": np.random.choice(["Male", "Female"], size=N_CUSTOMERS, p=[0.52, 0.48]),
    "acquisition_channel": [np.random.choice(acquisition_channel) for _ in cust_ids],
})
customers["city"] = customers["region"].apply(lambda r: np.random.choice(regions[r]))

# Give each customer a "loyalty tendency" so some customers order much more than others (Pareto-ish)
customers["loyalty_weight"] = np.random.exponential(scale=1.0, size=N_CUSTOMERS) + 0.05

# ---------------------------------------------------------------
# Orders / order line items
# ---------------------------------------------------------------
start_date = datetime(2024, 8, 1)
end_date = datetime(2026, 7, 31)
date_range_days = (end_date - start_date).days

weights = customers["loyalty_weight"].values
weights = weights / weights.sum()

rows = []
order_counter = 100000

for i in range(N_ORDERS):
    cust_idx = np.random.choice(customers.index, p=weights)
    cust = customers.loc[cust_idx]

    # seasonality: boost order likelihood around Oct-Nov (festive) and Jan (New Year sales)
    while True:
        day_offset = np.random.randint(0, date_range_days)
        order_date = start_date + timedelta(days=day_offset)
        month = order_date.month
        seasonal_boost = 1.0
        if month in (10, 11):
            seasonal_boost = 1.8
        elif month == 1:
            seasonal_boost = 1.3
        elif month in (6, 7):
            seasonal_boost = 0.8
        if np.random.rand() < seasonal_boost / 1.8:
            break

    category = np.random.choice(list(categories.keys()))
    product = np.random.choice(categories[category])
    low, high = category_price_range[category]
    unit_price = round(np.random.uniform(low, high), 2)
    quantity = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.45, 0.2, 0.15, 0.1, 0.06, 0.04])
    discount_pct = np.random.choice([0, 0, 5, 10, 15, 20, 25], p=[0.35, 0.15, 0.15, 0.15, 0.1, 0.06, 0.04])
    gross_amount = round(unit_price * quantity, 2)
    discount_amount = round(gross_amount * discount_pct / 100, 2)
    net_amount = round(gross_amount - discount_amount, 2)

    # small chance of return
    is_returned = np.random.rand() < 0.04

    order_counter += 1
    rows.append({
        "order_id": f"ORD{order_counter}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": cust["customer_id"],
        "customer_name": cust["customer_name"],
        "region": cust["region"],
        "city": cust["city"],
        "category": category,
        "product_name": product,
        "unit_price": unit_price,
        "quantity": int(quantity),
        "discount_pct": discount_pct,
        "gross_amount": gross_amount,
        "discount_amount": discount_amount,
        "net_amount": net_amount,
        "payment_method": np.random.choice(payment_methods, p=[0.35, 0.25, 0.15, 0.15, 0.10]),
        "is_returned": is_returned,
        "customer_rating": np.random.choice([5, 4, 3, 2, 1], p=[0.4, 0.3, 0.15, 0.1, 0.05]),
    })

df = pd.DataFrame(rows)

# introduce a few intentional data-quality issues so the "Data Cleaning" step is meaningful
dupe_sample = df.sample(15, random_state=1)
df = pd.concat([df, dupe_sample], ignore_index=True)                       # duplicate rows
missing_idx = df.sample(25, random_state=2).index
df.loc[missing_idx, "customer_rating"] = np.nan                             # missing ratings
missing_idx2 = df.sample(10, random_state=3).index
df.loc[missing_idx2, "discount_pct"] = np.nan                               # missing discount

df = df.sort_values("order_date").reset_index(drop=True)

df.to_csv("sales_data.csv", index=False)
customers.drop(columns=["loyalty_weight"]).to_csv("customers.csv", index=False)

print(f"sales_data.csv -> {len(df)} rows")
print(f"customers.csv  -> {len(customers)} rows")
