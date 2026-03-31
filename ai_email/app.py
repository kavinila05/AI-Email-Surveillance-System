import streamlit as st
import pandas as pd
import time
from pipeline import run_pipeline
from generator import generate_emails
from config import build_metrics

st.set_page_config(layout="wide")

st.title(" AI Communication Surveillance")

# ---------------- SESSION ----------------
if "raw" not in st.session_state:
    st.session_state["raw"] = None

if "result" not in st.session_state:
    st.session_state["result"] = None

# ---------------- SIDEBAR ----------------
st.sidebar.header("Input Source")

mode = st.sidebar.radio("Choose", ["Generate Emails", "Upload Emails"])

num = st.sidebar.slider("Number of emails", 5, 50, 15)

# ---------------- STEP 1 ----------------
st.header("Step 1 — Generate / Upload Emails")

if mode == "Generate Emails":
    if st.button(" Generate Emails"):

        with st.spinner("Generating emails..."):
            df = generate_emails(num)
            st.session_state["raw"] = df

        st.success(f"{len(df)} emails generated")

if mode == "Upload Emails":
    file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])

    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.session_state["raw"] = df
        st.success("File uploaded successfully")

# ---------------- SHOW RAW ----------------
if st.session_state["raw"] is not None:

    st.subheader("Raw Emails Preview")
    st.dataframe(st.session_state["raw"], use_container_width=True)

    st.download_button(
        " Download Raw Emails",
        st.session_state["raw"].to_csv(index=False),
        file_name="raw_emails.csv"
    )

    st.markdown("---")

    # ---------------- STEP 2 ----------------
    st.header("Step 2 — Analyse Emails")

    if st.button(" Analyse Emails"):

        progress_bar = st.progress(0)
        status = st.empty()

        data = st.session_state["raw"]
        results = []

        for i in range(len(data)):
            status.text(f"Analyzing email {i+1} of {len(data)}...")

            row_df = pd.DataFrame([data.iloc[i]])
            result = run_pipeline(row_df)

            results.append(result.iloc[0])

            progress_bar.progress((i + 1) / len(data))
            time.sleep(0.05)

        final_df = pd.DataFrame(results)
        st.session_state["result"] = final_df

        status.text("Analysis complete ")
        st.success("All emails analysed")

# ---------------- STEP 3 ----------------
if st.session_state["result"] is not None:

    df = st.session_state["result"]
    m = build_metrics(df)

    st.markdown("---")
    st.header("Step 3 — Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Emails", m["total"])
    col2.metric("Non-Compliant", m["non_comp"])
    col3.metric("Compliant", m["comp"])

    st.subheader(" Category Distribution")
    st.bar_chart(df["category"].value_counts())

    st.subheader(" Risk Distribution")
    st.bar_chart(df["priority"].value_counts())

    st.download_button(
        " Download Analysed Data",
        df.to_csv(index=False),
        file_name="analysed_emails.csv"
    )

    # ---------------- STEP 4 ----------------
    st.markdown("---")
    st.header("Step 4 — Explainability")

    for _, row in df.iterrows():

        title = f"{row['subject']} ({row['priority']})"

        with st.expander(title):

            body = row["body"]

            st.markdown(body)

            st.write("Category:", row["category"])
            st.write("Non-Compliant:", row["non_compliant"])
            st.write("Priority:", row["priority"])
            st.write("Reason:", row["reason"])

