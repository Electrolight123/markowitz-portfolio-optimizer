import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import scipy.optimize as optimization 

stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM']

start_date = '2010-01-01'
end_date = '2025-01-01'

# downloading the data from Yahoo Finance
def download_data(stocks):
    data = yf.download(stocks, start=start_date, end=end_date, auto_adjust=False, progress=False)['Adj Close']
    return data

def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show() 

#we usually use logarithmic for normalization purposes
def calculate_returns(data):
    returns = np.log(data / data.shift(1))
    return returns

def plot_daily_returns(returns):
    returns.plot(figsize=(10, 5))
    plt.show()

#print out mean and covariance of stocks within (start_date,end_date). There are 252 trading days within a year.
def show_statistics(returns):
    print(returns.mean() * 252) # annualized mean return
    print(returns.cov() * 252) # annualized covariance

#weight defines what stocks to includes (with what portion) in the portfolio
def initialize_weights():
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    return weights

#expected return of the portfolio
def calculated_portfolio_return(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    print("Expected Portfolio Return: ", portfolio_return)

#expected portfolio standard deviation (risk)
def calculate_portfolio_variance(weights, returns):
    portfolio_variance = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    print("Expected variance: ", portfolio_variance)

def generate_portfolios(weights, returns):
    preturns = []
    pvariances = []

    #Monte Carlo simulation : we generate several random weights -> so random portfolios !!
    for _ in range(10000):
        weights = np.random.random(len(stocks))
        weights /= np.sum(weights)
        preturns.append(np.sum(returns.mean() * weights) * 252)
        pvariances.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights))))

    preturns = np.array(preturns)
    pvariances = np.array(pvariances)
    return preturns, pvariances

def plot_portfolios(returns, variances):
    plt.figure(figsize=(10, 5))
    plt.scatter(variances, returns, c=returns / variances, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()

# OK this is the result of the simulation ... we have to find the optimal portfolio with some optimization technique !! Scipy can optimize functions (minimum / maximum finding)

def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_variance = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return np.array([portfolio_return, portfolio_variance, portfolio_return / portfolio_variance])

#[2] means that we want to maximize according to the Sharpe Ratio
#note : maximizing f(x) function is the same as minimizing -f(x) !!

def min_func_sharpe(weights, returns):
    return -statistics(weights, returns)[2]

#what are the constraints ? The sum of weights = 1 !! f(x) = 0 this is the function to minimize
def optimize_portfolio(weights, returns):
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1}) # sum of weights should be 1
    bounds = tuple((0, 1) for _ in range(len(stocks))) # weights should be between 0 and 1 (no short selling and no leverage)
    optimum = optimization.minimize(fun=min_func_sharpe, x0=weights, args=returns, method='SLSQP', bounds=bounds, constraints=constraints)
    return optimum

#optimal portfolio according to weights : 0 means no shares of that given company 
def print_optimal_portfolio(optimum, returns):
    print("Optimal Weights: ", optimum['x'].round(3))
    print("Expected return, volatility and Sharpe Ratio: ", statistics(optimum['x'].round(3), returns))

def show_optimal_portfolio(optimum, returns, preturns, pvariances):
    plt.figure(figsize=(10, 5))
    plt.scatter(pvariances, preturns, c=preturns / pvariances, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(optimum['x'], returns)[1], statistics(optimum['x'], returns)[0], 'g*', markersize=20)
    plt.show()

if __name__ == "__main__":
    data = download_data(stocks)
    show_data(data)
    returns = calculate_returns(data)
    plot_daily_returns(returns)
    show_statistics(returns)
    weights = initialize_weights()
    calculated_portfolio_return(weights, returns)
    calculate_portfolio_variance(weights, returns)
    preturns, pvariances = generate_portfolios(weights, returns)
    plot_portfolios(preturns, pvariances)
    optimum = optimize_portfolio(weights, returns)
    print_optimal_portfolio(optimum, returns)
    show_optimal_portfolio(optimum, returns, preturns, pvariances)