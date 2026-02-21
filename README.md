# 📈 Markowitz Portfolio Optimizer (Max Sharpe Ratio)

A Python implementation of Modern Portfolio Theory (MPT) that uses Monte
Carlo simulation and constrained optimization (SLSQP) to construct an
optimal portfolio by maximizing the Sharpe Ratio.

------------------------------------------------------------------------

## 🚀 Project Overview

This project:

-   Downloads historical stock data from Yahoo Finance\
-   Computes logarithmic daily returns\
-   Annualizes mean returns and covariance matrix\
-   Generates 10,000 random portfolios (Monte Carlo simulation)\
-   Visualizes the Efficient Frontier\
-   Optimizes portfolio weights to maximize the Sharpe Ratio\
-   Enforces realistic constraints:
    -   Full capital allocation (∑ weights = 1)
    -   No short selling (0 ≤ weight ≤ 1)

------------------------------------------------------------------------

## 🧠 Financial Concepts Used

-   Modern Portfolio Theory (Harry Markowitz)
-   Log Returns
-   Covariance Matrix
-   Portfolio Volatility
-   Sharpe Ratio
-   Efficient Frontier
-   Constrained Optimization (SLSQP)

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python\
-   NumPy\
-   Pandas\
-   SciPy\
-   Matplotlib\
-   yfinance

------------------------------------------------------------------------

## 📦 Installation

``` bash
git clone https://github.com/<your-username>/markowitz-portfolio-optimizer.git
cd markowitz-portfolio-optimizer
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Usage

``` bash
python src/portfolio_optimizer.py
```

The program will: - Display price charts - Plot daily returns - Simulate
portfolios - Show the Efficient Frontier - Print optimal weights -
Highlight the maximum Sharpe portfolio

------------------------------------------------------------------------

## 📌 Key Formulae

Portfolio Return (Annualized):

E(Rp) = Σ (wi \* μi) \* 252

Portfolio Volatility (Annualized):

σp = sqrt(wᵀ Σ w)

Sharpe Ratio:

Sharpe = Return / Volatility

------------------------------------------------------------------------

## 🎯 Why This Project Matters

This project demonstrates:

-   Quantitative finance fundamentals\
-   Real financial data handling\
-   Monte Carlo simulation\
-   Numerical optimization\
-   Financial modeling in Python

Applicable for roles in: - Quantitative Finance\
- Asset Management\
- Portfolio Strategy\
- Financial Data Analytics

------------------------------------------------------------------------

## 📜 License

This project is for educational and research purposes.

