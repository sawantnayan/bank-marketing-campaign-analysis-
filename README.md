# Bank Marketing Campaign Analysis Using Python

## 1. Project Overview

This project analyses a bank's historical marketing campaign data to understand customer behaviour and identify patterns associated with term-deposit subscriptions.

The analysis uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn to clean, explore, and visualise the dataset.

The main objective is to understand which customer groups show higher subscription rates and how campaign contact patterns relate to subscription outcomes.

## 2. Business Problem

Banks conduct marketing campaigns to encourage customers to subscribe to term deposits. However, not all customers respond positively to these campaigns.

The bank needs to understand customer characteristics, identify customer segments with higher subscription rates, and evaluate campaign contact patterns.

This analysis aims to provide insights that can support better customer targeting and more informed marketing decisions.

## 3. Dataset Information

- Dataset: Bank Marketing Dataset
- Source: UCI Machine Learning Repository
- Records: 41,188 (before any duplicate removal)
- Original features: 20 input features and 1 target variable
- Target variable: `y`
- Target values: `yes` and `no`
- Period: Historical campaign data from 2008–2010


## 4. Tools and Technologies

- Python
- Pandas – Data manipulation and cleaning
- NumPy – Numerical operations
- Matplotlib – Data visualisation
- Seaborn – Statistical visualisation
- Python IDLE – Development environment

## 5. Data Cleaning and Preparation

The following activities were performed:

- Loaded the dataset using Pandas.
- Inspected rows, columns, data types, and statistical summaries.
- Checked for missing values.
- Identified and removed duplicate records.
- Standardised text columns by removing unnecessary spaces.
- Created age groups for customer segmentation.
- Prepared data for exploratory analysis.

## 6. Business Questions

1. What is the overall distribution of customers who subscribed and did not subscribe?
2. What is the age distribution of customers contacted by the bank?
3. Which age groups have higher term-deposit subscription rates?
4. Which job categories show higher subscription rates?
5. How does education level relate to subscription rates?
6. How does the number of campaign contacts relate to subscription decisions?
7. Which months show higher subscription rates?

## 7. Exploratory Data Analysis and Visualisations

### 1. Subscription Analysis
Examines the number of customers who subscribed and did not subscribe to the term deposit.

### 2. Customer Age Distribution
Analyses the distribution of customer ages to understand the age profile of the bank's campaign audience.

### 3. Subscription Rate by Age Group
Compares subscription percentages across different customer age groups.

### 4. Subscription Rate by Job
Identifies job categories with comparatively higher and lower subscription rates.

### 5. Subscription Rate by Education
Examines how subscription rates vary across education categories.

### 6. Campaign Contact Analysis
Explores the relationship between the number of contacts during the current campaign and subscription outcomes.

### 7. Monthly Subscription Rate
Compares subscription rates across different months to identify seasonal patterns in the historical campaign data.

## 8. Key Insights

Based on the exploratory data analysis and visualisations, the following observations were identified:

1. **Overall Subscription:** Only approximately 11% of customers subscribed to the term deposit, indicating a relatively low overall campaign conversion rate.

2. **Customer Age Distribution:** Most customers contacted were between 30 and 50 years old, with the highest concentration around 30–35 years.

3. **Age Group Analysis:** Customers above 65 showed the highest subscription rate at approximately 47%, followed by customers below 25 at around 21%.

4. **Job Analysis:** Students had the highest subscription rate at approximately 31%, followed by retired customers at around 25%.

5. **Education Analysis:** Customers in the illiterate education category showed the highest subscription rate at approximately 22%, while basic 6-year and basic 9-year education categories had comparatively lower rates.

6. **Campaign Contact Analysis:** Customers who subscribed generally had fewer campaign contacts than customers who did not subscribe. This suggests that repeated contacts do not necessarily result in higher conversions.

7. **Monthly Analysis:** March, December, September, and October showed comparatively higher subscription rates, while May had the lowest rate.

## 9. Business Recommendations

Based on the historical patterns observed:

- Explore customer segmentation strategies using age, occupation, and education categories.
- Investigate the preferences of customer groups with higher subscription rates.
- Evaluate contact frequency to improve campaign efficiency.
- Study seasonal patterns when planning future marketing campaigns.
- Monitor conversion rates across customer segments to evaluate campaign performance.

**Note:** These findings describe associations in historical campaign data from 2008–2010. They do not establish that any customer characteristic or campaign factor directly causes a subscription.


## 10. Conclusion

This project demonstrates how Python can be used to analyse customer demographics and historical marketing campaign performance.

Through data cleaning, exploratory data analysis, and visualisation, the project identifies patterns associated with term-deposit subscriptions and provides insights that can support more informed marketing decisions.

## 12. Disclaimer

This analysis uses historical data from 2008–2010. The findings should not be assumed to represent current banking customers or current marketing performance. Observed relationships do not establish causation.
