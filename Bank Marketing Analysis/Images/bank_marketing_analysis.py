import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

df = pd.read_csv("bank-additional-full.csv", sep=";")


# Number of rows and columns
print("Dataset Shape:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Create a copy of original dataset
df_clean = df.copy()

# Remove duplicate records
df_clean = df_clean.drop_duplicates()


# Customer Subscription Analysis

print("\n----- Customer Subscription Analysis -----")
subscription_count = df_clean["y"].value_counts()

print(subscription_count)

subscription_percentage = (
    df_clean["y"].value_counts(normalize=True) * 100
)

print("\nSubscription Percentage:")
print(subscription_percentage.round(2))

# Visulaization


sns.countplot(data=df_clean, x="y")

plt.title("Customer Subscription Analysis")
plt.xlabel("Term Deposit Subscription")
plt.ylabel("Number of Customers")

plt.savefig("subscription_analysis.png", dpi=300, bbox_inches="tight")
plt.show()


# Age Analysis

print("\n----- Age Analysis -----")

# Age distribution
plt.figure(figsize=(10, 5))

sns.histplot(data=df_clean, x="age", bins=30, kde=True)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.savefig()
plt.show()

# Create age groups
df_clean["age_group"] = pd.cut(
    df_clean["age"],
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=["Below 25", "26-35", "36-45", "46-55", "56-65", "Above 65"]
)

# Subscription by age group
age_analysis = pd.crosstab(
    df_clean["age_group"],
    df_clean["y"],
    normalize="index"
) * 100

print(age_analysis.round(2))

age_analysis.plot(kind="bar", figsize=(10, 5))

plt.title("Subscription Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Percentage")
plt.xticks(rotation=45)

plt.savefig()
plt.show()


# Job-wise subscription Analysis

print("\n----- Job-wise subscription Analysis -----")

job_analysis = pd.crosstab(
    df_clean["job"],
    df_clean["y"],
    normalize="index"
) * 100

job_analysis = job_analysis.sort_values(
    by="yes",
    ascending=False
)

print(job_analysis.round(2))

job_analysis["yes"].plot(
    kind="bar",
    figsize=(12, 5)
)

plt.title("Subscription Rate by Job")
plt.xlabel("Job")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=45)

plt.savefig()
plt.show()


# Education - wise subscription analysis

print("\n----- Education - wise subscription Analysis -----")

education_analysis = pd.crosstab(
    df_clean["education"],
    df_clean["y"],
    normalize="index"
) * 100
print(education_analysis.round(2))

education_analysis.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Subscription Rate by Education")
plt.xlabel("Education")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=45)

plt.savefig()
plt.show()


# Monthly campaign analysis

print("\n----- Monthly campaign Analysis -----")

month_analysis = pd.crosstab(
    df_clean["month"],
    df_clean["y"],
    normalize="index"
) * 100

# Keep chronological month order
month_order = [
    "mar", "apr", "may", "jun", "jul", "aug",
    "sep", "oct", "nov", "dec"
]

month_analysis = month_analysis.reindex(month_order)

print(month_analysis.round(2))

month_analysis["yes"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Monthly Subscription Rate")
plt.xlabel("Month")
plt.ylabel("Subscription Rate (%)")

plt.savefig()
plt.show()


# Campaign Contact Analysis

print("\n----- Campaign Contact Analysis -----")

plt.figure(figsize=(10, 5))

sns.boxplot(
    data=df_clean,
    x="y",
    y="campaign"
)

plt.title("Number of Contacts vs Subscription")
plt.xlabel("Subscription")
plt.ylabel("Number of Contacts")

plt.savefig()
plt.show()

# Average campaign contacts by subscription
campaign_analysis = df_clean.groupby("y")["campaign"].mean()

print(campaign_analysis)


# Business Summary


total_customers = len(df_clean)

subscribed = (df_clean["y"] == "yes").sum()

not_subscribed = (df_clean["y"] == "no").sum()

conversion_rate = (subscribed / total_customers) * 100

average_age = df_clean["age"].mean()

average_campaign_calls = df_clean["campaign"].mean()

best_job = (
    pd.crosstab(df_clean["job"], df_clean["y"], normalize="index")["yes"]
    .idxmax()
)

best_month = (
    pd.crosstab(df_clean["month"], df_clean["y"], normalize="index")["yes"]
    .idxmax()
)

print("========== BUSINESS SUMMARY ==========")

print("Total Customers:", total_customers)
print("Subscribed Customers:", subscribed)
print("Not Subscribed:", not_subscribed)

print("Conversion Rate:", round(conversion_rate, 2), "%")

print("Average Customer Age:", round(average_age, 2))

print("Average Campaign Calls:", round(average_campaign_calls, 2))

print("Highest Subscription Rate Job:", best_job)

print("Highest Subscription Rate Month:", best_month)


# Exporting cleaned dataset and analysis results


# Export cleaned dataset
df_clean.to_csv("cleaned_bank_data.csv", index=False)

# Export job analysis
job_analysis.to_csv("job_subscription_analysis.csv")

# Export monthly analysis
month_analysis.to_csv("monthly_subscription_analysis.csv")

print("All files exported successfully!")







