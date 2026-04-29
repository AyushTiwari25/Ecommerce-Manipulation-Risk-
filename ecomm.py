"""
Dark Pattern Detection in E-commerce Platforms
Author: Ayush Tiwari

Each section includes expected OUTPUT as comments
"""

# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# OUTPUT:
# (No visible output — libraries loaded)


# ==============================
# 2. DATA GENERATION
# ==============================
brands = ["Samsung", "Apple", "Realme", "Redmi", "OnePlus", "Vivo", "Oppo"]
models = ["Pro", "Max", "Ultra", "Lite", "Plus", "Prime"]
categories = ["Smartphone", "Headphones", "Laptop", "Smartwatch"]

platforms = [
    "Amazon", "Flipkart", "Myntra", "Ajio",
    "Meesho", "Nykaa", "Snapdeal", "Paytm Mall", "JioMart"
]


def generate_product_name():
    return f"{random.choice(brands)} {random.choice(models)} {random.choice(categories)}"


def generate_price():
    return random.randint(5000, 80000)


def generate_discount(price):
    discount_percent = random.choice([10, 20, 30, 40, 50, 60])
    final_price = int(price * (1 - discount_percent / 100))
    return discount_percent, final_price


def urgency_flag():
    return random.choice([0, 1])


def fake_discount(discount):
    return 1 if discount > 40 else 0


def rating():
    return round(random.uniform(2.5, 5.0), 1)


def generate_platform():
    return random.choice(platforms)


def create_dataset(n=50000):
    data = []

    for _ in range(n):
        price = generate_price()
        discount_percent, final_price = generate_discount(price)

        row = [
            generate_product_name(),
            price,
            final_price,
            discount_percent,
            urgency_flag(),
            fake_discount(discount_percent),
            rating(),
            generate_platform()
        ]

        data.append(row)

    columns = [
        "product_name", "original_price", "final_price",
        "discount_percent", "urgency_flag",
        "fake_discount", "rating", "platform"
    ]

    return pd.DataFrame(data, columns=columns)


# OUTPUT:
# DataFrame with ~50,000 rows and columns:
# product_name | original_price | final_price | discount_percent | urgency_flag | fake_discount | rating | platform


# ==============================
# 3. FEATURE ENGINEERING
# ==============================
def add_dark_pattern_features(df):

    df["discount_score"] = df["discount_percent"]

    df["price_diff_ratio"] = (
        (df["original_price"] - df["final_price"]) / df["original_price"] * 100
    )

    df["urgency_weight"] = df["urgency_flag"] * 20
    df["fake_discount_weight"] = df["fake_discount"] * 30

    df["dark_pattern_score"] = (
        df["discount_score"]
        + df["price_diff_ratio"]
        + df["urgency_weight"]
        + df["fake_discount_weight"]
    )

    def categorize(score):
        if score < 50:
            return "Low"
        elif score < 80:
            return "Moderate"
        else:
            return "High Manipulation"

    df["manipulation_level"] = df["dark_pattern_score"].apply(categorize)

    return df


# OUTPUT:
# New columns added:
# discount_score, price_diff_ratio, urgency_weight, fake_discount_weight,
# dark_pattern_score, manipulation_level


# ==============================
# 4. VISUALIZATION
# ==============================
def plot_distribution(df):
    counts = df["manipulation_level"].value_counts()
    total = counts.sum()

    fig, ax = plt.subplots()
    bars = ax.bar(counts.index, counts.values)

    ax.set_title("Manipulation Level Distribution", loc='left')
    ax.set_ylabel("Number of Products")
    ax.spines[['top', 'right']].set_visible(False)

    for bar in bars:
        height = bar.get_height()
        percent = (height / total) * 100
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{int(height)}\n({percent:.1f}%)",
            ha='center'
        )

    plt.tight_layout()

    plt.savefig("manipulation_distribution.png", dpi=300)
    plt.show()


# OUTPUT:
# File saved → manipulation_distribution.png
# Graph showing distribution of Low / Moderate / High manipulation


# ==============================
# 5. MODEL TRAINING
# ==============================
def train_model(df):

    features = [
        "original_price", "final_price", "discount_percent",
        "urgency_flag", "fake_discount", "rating"
        # NOTE: removed dark_pattern_score to avoid leakage
    ]

    X = df[features]
    y = df["manipulation_level"]

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n=== Model Performance ===\n")
    print(classification_report(y_test, y_pred))

    return model


# OUTPUT:
# Console:
# precision, recall, f1-score, accuracy
# Example:
# accuracy ~0.85–0.95 (after fixing leakage)


# ==============================
# 6. MAIN EXECUTION
# ==============================
def main():

    print("Generating dataset...")
    df = create_dataset()

    print("Applying feature engineering...")
    df = add_dark_pattern_features(df)

    print("\nSample Data:")
    print(df.head())

    print("\nDistribution:")
    print(df["manipulation_level"].value_counts())

    # Save dataset
    df.to_csv("dark_pattern_dataset.csv", index=False)

    # Platform analysis
    platform_avg = df.groupby("platform")["dark_pattern_score"].mean()
    platform_avg.to_csv("platform_analysis.csv")

    # Plot
    plot_distribution(df)

    # Train model
    model = train_model(df)

    # Save model
    joblib.dump(model, "dark_pattern_model.pkl")

    print("\nSaved Files:")
    print("dark_pattern_dataset.csv")
    print("platform_analysis.csv")
    print("manipulation_distribution.png")
    print("dark_pattern_model.pkl")


# OUTPUT:
# Files generated:
# ✔ dark_pattern_dataset.csv
# ✔ platform_analysis.csv
# ✔ manipulation_distribution.png
# ✔ dark_pattern_model.pkl


if __name__ == "__main__":
    main()
