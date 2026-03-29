import os
import pandas as pd
from config import CATEGORIES, RISK_MAP, get_priority
import json
from llm import call_llm


def generate_emails(n):

    rows = []

    # force distribution (VERY IMPORTANT)
    category_cycle = CATEGORIES * (n // len(CATEGORIES) + 1)

    for i in range(n):

        category = category_cycle[i]

        prompt = f"""
Write a realistic corporate banking email.

Category: {category}

Make it:
- Natural
- Unique
- With signature
- 100+ words

Return plain text only.
"""

        try:
            body = call_llm(prompt)

            rows.append({
                "date": "2025-03-01",
                "from": f"user{i}@bank.com",
                "to": f"client{i}@external.com",
                "subject": f"{category} discussion {i}",
                "body": body,
                "true_category": category
            })

        except:
            continue

    return pd.DataFrame(rows)
