import pandas as pd
import json
from llm import call_llm
from config import RISK_MAP, get_priority


def analyze_email(row):

    category = row["true_category"]

    score = RISK_MAP[category]
    priority = get_priority(score)

    non_compliant = "Yes" if category != "Normal" else "No"

    # LLM only for explanation
    prompt = f"""
Explain why this email is classified as {category}:

{row['body']}

Return:
Reason + exact risky sentence.
"""

    try:
        explanation = call_llm(prompt)
    except:
        explanation = "Could not generate explanation"

    return {
        "category": category,
        "non_compliant": non_compliant,
        "score": score,
        "priority": priority,
        "reason": explanation,
        "source": ""
    }


def process_emails():
    df = pd.read_csv("data/raw_emails.csv")

    outputs = []

    for _, row in df.iterrows():
        result = analyze_email(row["body"])

        outputs.append({
            **row,
            **result
        })

    final = pd.DataFrame(outputs)

    # ✅ ALWAYS ensure column exists
    if "priority" not in final.columns:
        final["priority"] = 1

    final.to_csv("data/final_output.csv", index=False)
