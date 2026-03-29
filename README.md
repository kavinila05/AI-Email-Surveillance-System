# 🏦 AI Communication Surveillance System

An AI-powered application that monitors email communications to detect compliance risks, classify intent, and prioritize alerts using LLMs and rule-based scoring.

---

## 🚀 Overview

This project simulates a real-world **banking compliance surveillance system** where large volumes of emails are analyzed to detect:

* Market manipulation
* Bribery / quid pro quo
* Secrecy / off-record communication
* Ethical violations
* Suspicious communication patterns

The system reduces **manual review effort** by automatically identifying and prioritizing high-risk emails.

---

## ✨ Key Features

### 📩 Flexible Input

* Generate synthetic emails using LLM
* Upload real datasets (CSV/Excel)

---

### 🧠 LLM-Based Classification

Each email is analyzed and classified into:

* Secrecy
* Market Manipulation
* Market Bribery
* Change in Communication
* Complaints
* Employee Ethics
* Normal (Compliant)

---

### ⚖️ Risk Prioritization

Predefined scoring assigns:

* **High Risk**
* **Medium Risk**
* **Low Risk**

This helps teams focus only on critical alerts.

---

### 📊 Interactive Dashboard

* Total emails processed
* Compliance vs Non-compliance
* Category distribution
* Risk distribution

---

### 🔍 Explainability

For each email, the system provides:

* Classification category
* Risk level
* Reason for classification
* Extracted suspicious text

---

## 🏗️ Project Structure

```bash
.
├── app.py          # Streamlit UI (main dashboard)
├── pipeline.py     # End-to-end workflow orchestration
├── analyzer.py     # Classification & risk scoring logic
├── generator.py    # Synthetic email generation (LLM-based)
├── llm.py          # OpenRouter API integration
├── config.py       # Configuration (categories, weights)
├── requirements.txt
├── .env            # API key (not committed)
└── .gitignore
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Integration:** OpenRouter API
* **Data Processing:** Pandas

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd ai-communication-surveillance

python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

### Step 1 — Input

* Generate emails OR upload dataset

### Step 2 — Processing

* Clean data
* Run LLM classification
* Assign categories and risk

### Step 3 — Output

* Dashboard visualization
* Download analyzed results

---

## 📁 Sample Input Format

```csv
date,from,to,subject,body
2025-03-01,emp@bank.com,client@ext.com,Trade discussion,"Email content..."
```

---

## 📌 Use Cases

* Banking compliance monitoring
* Fraud detection
* Internal audit automation
* Risk prioritization systems

---

## ⚠️ Limitations

* LLM outputs may vary slightly
* Requires prompt tuning for higher accuracy
* Synthetic emails may not fully reflect real-world complexity

---

## 🚀 Future Improvements

* Real-time monitoring system
* Multi-label classification
* Advanced visualization (Plotly dashboards)
* Alert notification system
* Model fine-tuning

---

## 👩‍💻 Author

**Kavinila V**

---

## ⭐ If you found this useful, consider giving a star!
