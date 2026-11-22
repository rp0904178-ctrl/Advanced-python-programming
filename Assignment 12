import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset load kara
df = pd.read_csv("customer_churn.csv")

# 2. Basic information
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# 3. Missing values check
print("Missing values:\n", df.isnull().sum())

# 4. Data cleaning
# Duplicates kadha
df = df.drop_duplicates()

# Numeric columns madhe missing values median ne bhara
num_cols = df.select_dtypes(include=np.number).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns madhe mode ne bhara
cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Outliers kadha (IQR method)
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

# 5. EDA: patterns shodha
# Churn distribution
if "Churn" in df.columns:
    sns.countplot(x="Churn", data=df)
    plt.title("Churn Distribution")
    plt.show()

# Numeric features chi distribution
df[num_cols].hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 6. Categorical columns vs Churn
if "Churn" in df.columns:
    for col in cat_cols:
        if col != "Churn" and df[col].nunique() < 10:
            sns.countplot(x=col, hue="Churn", data=df)
            plt.title(f"{col} vs Churn")
            plt.xticks(rotation=45)
            plt.show()

# 7. Clean data save kara
df.to_csv("customer_churn_cleaned.csv", index=False)
print("Cleaned data saved.")
