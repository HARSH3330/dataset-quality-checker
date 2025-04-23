def check_dataset(df):
    issues = []

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        issues.append("Missing values")

    # Check for duplicate rows
    if df.duplicated().sum() > 0:
        issues.append("Duplicate rows")

    # Check for negative numbers in numeric columns
    numeric_df = df.select_dtypes(include='number')
    if (numeric_df < 0).any().any():
        issues.append("Negative numbers found")

    # Decide status based on issues found
    score = len(issues)

    if score == 0:
        return "green", issues
    elif score <= 2:
        return "yellow", issues
    else:
        return "red", issues
