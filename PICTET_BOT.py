import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as datetime
import yfinance as yf
import empyrial as ep


def calculate_risk_reward_profile(time, income, finpriority, risk, high_risk, loss, min_loss):
    # Convert select box responses to numerical values
    time_map = {"Less than 3 years": 1, "3 to 10 years": 2, "More than 10 years": 3}
    income_map = {"Less than 100000 CHF": 1, "Between 100000 and 250000 CHF": 2, "More than 250000 CHF": 3}
    slider_map = {"Fully disagree": 1, "Rather disagree": 2, "Rather agree": 3, "Fully agree": 4}

    time_value = time_map.get(time)
    income_value = income_map.get(income)
    finpriority_value = slider_map.get(finpriority)
    risk_value = slider_map.get(risk)
    high_risk_value = slider_map.get(high_risk)
    loss_value = slider_map.get(loss)
    min_loss_value = slider_map.get(min_loss)

    # Calculate risk appetite
    risk_appetite = (finpriority_value + high_risk_value) / 2

    # Calculate risk capacity
    risk_capacity = (income_value + time_value) / 2

    # Calculate risk profile
    risk_profile = (risk_value + loss_value + min_loss_value) / 3

    return risk_appetite, risk_capacity, risk_profile

def determine_risk_appetite_category(risk_appetite):
    if risk_appetite < 2.5:
        return "Decreased"
    elif risk_appetite < 3.5:
        return "Medium"
    else:
        return "Increased"

def determine_risk_capacity_category(risk_capacity):
    if risk_capacity == 1:
        return "Low"
    elif risk_capacity == 2:
        return "Medium"
    else:
        return "High"

def determine_risk_profile_category(risk_profile):
    if risk_profile < 2:
        return "Conservative"
    elif risk_profile < 3:
        return "Moderately Conservative"
    elif risk_profile < 4:
        return "Moderate"
    elif risk_profile < 5:
        return "Moderately Aggressive"
    else:
        return "Aggressive"

def get_stock_symbols(risk_profile_category):
    # Define stock symbols based on risk profile category
    if risk_profile_category == "Conservative":
        return ["AAPL", "MSFT", "KO"]
    elif risk_profile_category == "Moderately Conservative":
        return ["AAPL", "MSFT", "KO", "FB", "GOOGL"]
    elif risk_profile_category == "Moderate":
        return ["AAPL", "MSFT", "KO", "FB", "GOOGL", "NFLX", "TSLA"]
    elif risk_profile_category == "Moderately Aggressive":
        return ["AAPL", "MSFT", "KO", "FB", "GOOGL", "NFLX", "TSLA", "AMZN"]
    else:  # Aggressive
        return ["AAPL", "MSFT", "KO", "FB", "GOOGL", "NFLX", "TSLA", "AMZN", "BABA"]

def optimize_portfolio(stock_symbols):
    # Download historical data for the selected stocks
    data = yf.download(stock_symbols, start="2020-01-01", end="2022-01-01")['Adj Close']

    # Optimize portfolio using Empyrial
    weights = ep.optimizer(data, "max_sharpe")

    return weights

def main():
    st.title("Portfolio Optimization based on Risk Profile")
    
    # Questionnaire
    time = st.selectbox("How long do you plan to invest your money?", ("Less than 3 years", "3 to 10 years", "More than 10 years"))
    income = st.selectbox("How much money do you plan to invest into the fund?", ("Less than 100000 CHF", "Between 100000 and 250000 CHF", "More than 250000 CHF"))
    finpriority = st.select_slider("I take financial matters seriously and security is my top priority.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    risk = st.select_slider("When it comes to my money, I am reluctant to take risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    high_risk = st.select_slider("I would like to achieve higher profits and therefore would be willing to take on higher risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    loss = st.select_slider("The risk of suffering losses on my assets concerns me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    min_loss = st.select_slider("Minimal losses also concern me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    
    # Calculate risk profile category
    risk_profile = calculate_risk_reward_profile(time, income, finpriority, risk, high_risk, loss, min_loss)
    risk_profile_category = determine_risk_profile_category(risk_profile)
    
    # Get stock symbols based on risk profile category
    stock_symbols = get_stock_symbols(risk_profile_category)
    
    # Optimize portfolio
    weights = optimize_portfolio(stock_symbols)
    
    # Display portfolio optimization results using Empyrial
    ep.summary(weights)

    # Display interesting graphics using Empyrial
    ep.cumulative_returns(weights)
    ep.eoy_returns(weights)
    ep.monthly_returns(weights)

if __name__ == "__main__":
    main()
