def validate_data(df):
    return {
        "rows": len(df),
        "nulls": df.isnull().sum().to_dict()
    }