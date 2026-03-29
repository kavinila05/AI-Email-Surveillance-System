CATEGORIES = [
    "Secrecy",
    "Market Manipulation",
    "Market Bribery",
    "Change in Communication",
    "Complaints",
    "Employee Ethics",
    "Normal"
]

RISK_MAP = {
    "Market Manipulation": 9,
    "Market Bribery": 9,
    "Secrecy": 6,
    "Employee Ethics": 6,
    "Change in Communication": 4,
    "Complaints": 3,
    "Normal": 1
}


def get_priority(score):
    if score >= 8:
        return "High Risk"
    elif score >= 5:
        return "Medium Risk"
    else:
        return "Low Risk"


def build_metrics(df):

    total = len(df)
    non_comp = (df["non_compliant"] == "Yes").sum()
    comp = total - non_comp

    by_cat = df["category"].value_counts()

    by_cat_nc = df[df["non_compliant"] == "Yes"]["category"].value_counts()
    by_cat_c = df[df["non_compliant"] == "No"]["category"].value_counts()

    by_cat_nc = by_cat_nc.reindex(by_cat.index, fill_value=0)
    by_cat_c = by_cat_c.reindex(by_cat.index, fill_value=0)

    return {
        "total": total,
        "non_comp": int(non_comp),
        "comp": int(comp),
        "by_cat": by_cat,
        "by_cat_nc": by_cat_nc,
        "by_cat_c": by_cat_c
    }
