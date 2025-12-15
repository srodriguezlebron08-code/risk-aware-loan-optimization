OPTIMIZATION FINAL PROJECT
Risk-Aware Loan Portfolio Optimization

Risk-Aware Loan Portfolio Optimization (Google Colab)

Overview

This project develops a risk-aware loan approval optimization model for the banking industry. Using historical loan-level data, borrowers are segmented by age group, education level, loan amount, employment type, and financial responsibilities (dependents and mortgage status).

A Gurobi optimization model is used to allocate loan approvals across borrower segments to maximize expected profit while respecting realistic banking constraints.

This project was fully developed and executed in Google Colab.

Business Motivation

With over four years of experience working in the banking industry, I observed firsthand the tradeoff between loan growth targets and credit risk management. High-risk borrower segments, particularly younger borrowers with limited financial buffers, often drive both profitability and defaults.

This project formalizes those decision challenges into a data-driven optimization model that supports better lending decisions.

Data Description

Dataset: Loan default dataset provided for ISOM 839

Key Variables Used:

Age
Education
Loan Amount
Interest Rate
Employment Type (Full-time / Part-time)
Has Dependents
Has Mortgage
Default Indicator (0/1)
Borrowers were grouped into segments based on:

Age group (18–25, 26–35, etc.)
Education level
Loan amount bands
Employment status
Financial responsibilities
Methodology

1. Data Preparation

Cleaned missing and invalid values
Created age groups and loan amount bands
Built borrower segments combining demographic and financial attributes
2. Risk Measurement

Calculated probability of default (PD) by segment
Tracked already-defaulted loan counts and defaulted dollar amounts
3. Optimization Model

Decision Variable

Dollar amount of loans approved per borrower segment
Objective

Maximize expected risk-adjusted profit
Constraints

Total lending budget
Expected loss (risk appetite) limit
Segment demand limits
Concentration caps to avoid overexposure
4. Advanced Analysis

Scenario analysis (base, mild recession, severe recession)
Sensitivity analysis on risk appetite limits
How to Run the Project (Google Colab)

Open the Google Colab notebook:

Run all cells from top to bottom.

When prompted, upload:

Note:

A Gurobi license is required to solve the optimization model.
If a license is unavailable in Colab, the same code can be run locally.
Key Outputs

Segment-level default probabilities
Already-defaulted loan dollar amounts
Optimized loan approvals by segment
Expected profit vs expected loss tradeoffs
Scenario and sensitivity analysis results All visualizations and tables are generated directly in the Colab notebook.
Files

Google Colab Notebook (.ipynb)
Loan_default_ISOM_839_Final_Project.xlsx
README (this page)
Author

Sofia Rodriguez
MSBA Candidate
Background in banking operations and risk-aware lending decisions
