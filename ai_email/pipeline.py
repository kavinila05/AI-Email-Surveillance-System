import pandas as pd
import random
from config import CATEGORIES, RISK_MAP, get_priority
from llm import call_llm
from analyzer import *


# ---------------- PIPELINE ----------------


def run_pipeline(df):

    results = []

    for _, row in df.iterrows():

        analysis = analyze_email(row)

        results.append({
            **row,
            **analysis
        })

    return pd.DataFrame(results)






