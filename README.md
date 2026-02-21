# 📈 Markowitz Portfolio Optimizer (Max Sharpe Ratio)

A Python implementation of Modern Portfolio Theory (MPT) that uses Monte
Carlo simulation and constrained optimization (SLSQP) to construct an
optimal portfolio by maximizing the Sharpe Ratio.

This project demonstrates quantitative finance concepts including return modeling, covariance estimation, efficient frontier visualization, and portfolio optimization under realistic constraints.
------------------------------------------------------------------------

## 🚀 Project Overview

This project:

-   Downloads historical stock data from Yahoo Finance
-   Computes logarithmic daily returns
-   Annualizes mean returns and covariance matrix
-   Generates 10,000 random portfolios (Monte Carlo simulation)
-   Visualizes the Efficient Frontier
-   Optimizes portfolio weights to maximize the Sharpe Ratio
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

## 📊 Example Workflow

-   Download stock data
-   Calculate daily log returns
-   Generate random portfolios
-   Plot return vs volatility
-   Identify optimal portfolio (Max Sharpe)
-   Highlight optimal point on Efficient Frontier

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   NumPy
-   Pandas
-   SciPy
-   Matplotlib
-   yfinance

------------------------------------------------------------------------

## 📦 Installation

``` bash
git clone https://github.com/Electrolight123/markowitz-portfolio-optimizer.git
cd markowitz-portfolio-optimizer
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Usage

``` bash
python Modern_portfolio_Theory.py
```

The program will: 

- Display price charts
- Plot daily returns
- Simulate portfolios
- Show the Efficient Frontier
- Print optimal weights
- Highlight the maximum Sharpe portfolio

------------------------------------------------------------------------

## 📌 Key Formulae

Portfolio Return (Annualized):

E(Rp) = Σ (wi \* μi) \* 252

Portfolio Volatility (Annualized):

σp = sqrt(wᵀ Σ w)

Sharpe Ratio:

Sharpe = Return / Volatility

------------------------------------------------------------------------

## ⚙ Constraints Applied

-   Sum of weights = 1
-   0 ≤ weight ≤ 1
-   No leverage
-   No short selling

  Optimization is performed using Sequential Least Squares Programming (SLSQP) from SciPy.

------------------------------------------------------------------------

## 📈 Sample Output

-   Scatter plot of simulated portfolios
-   Color-coded Sharpe ratio
-   Efficient frontier visualization
-   Optimal portfolio marked with a green star

------------------------------------------------------------------------

## 📜 License

This project is for educational and research purposes.

