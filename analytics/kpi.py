def compute_kpis(df):
    return {
        "total_sales": df["sales"].sum() if "sales" in df else 0
    }