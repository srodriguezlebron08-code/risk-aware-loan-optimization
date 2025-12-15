import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Risk-Aware Loan Optimization", layout="wide")

st.title("Risk-Aware Loan Portfolio Optimization")

st.markdown("""
This app demonstrates a prescriptive analytics approach to allocating loan approvals
while controlling credit risk.
""")

uploaded_file = st.file_uploader(
    "Upload Loan Default Dataset (Excel)",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Please upload the dataset to begin.")
    st.stop()

df = pd.read_excel(uploaded_file)

st.subheader("Data Preview")
st.dataframe(df.head())

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=["18-25", "26-35", "36-45", "46-55", "56+"]
)

df["LoanAmtBand"] = pd.qcut(
    df["LoanAmount"],
    q=3,
    labels=["Low", "Medium", "High"]
)

df["Segment"] = (
    df["AgeGroup"].astype(str) + " | " +
    df["Education"].astype(str) + " | " +
    df["LoanAmtBand"].astype(str)
)

seg = (
    df.groupby("Segment")
      .agg(
          Loans=("LoanID", "count"),
          DefaultRate=("Default", "mean"),
          Demand=("LoanAmount", "sum")
      )
      .reset_index()
)

st.subheader("Segment Risk Summary")
st.dataframe(seg.sort_values("DefaultRate", ascending=False))

st.sidebar.header("Controls")

budget_pct = st.sidebar.slider(
    "Approve % of Total Loan Demand",
    5, 50, 20
) / 100

total_budget = budget_pct * seg["Demand"].sum()

seg["Approved"] = np.minimum(seg["Demand"], total_budget * (1 - seg["DefaultRate"]))

st.subheader("Optimized Allocation (Simplified)")
st.dataframe(seg.sort_values("Approved", ascending=False))

st.metric("Total Approved ($)", f"{seg['Approved'].sum():,.0f}")
