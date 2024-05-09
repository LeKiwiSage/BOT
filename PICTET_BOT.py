#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import math
from empyrial import empyrial, Engine
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st


# In[2]:


st.title('P.I.C.T.E.T Portfolio Optimizer')


#Welcome Statement
txt = st.text_area(
    "Welcome to our investment platform!",
    "We are thrilled to have you onboard as we embark on an exciting journey together."
    "Our goal is simple yet ambitious: to empower you to grow your investment portfolio" 
    "across multiple assets, tailored precisely to your unique risk-reward profile."
    "By understanding your risk tolerance, investment goals, and preferences, we will" 
    "craft a personalized investment strategy that aligns with your vision for the future."
    "Whether you are seeking steady growth, aggressive expansion, or somewhere in between," 
    "our bot will work tirelessly to optimize your portfolio for maximum returns while managing risk effectively."
    "With our investment fund, you're not just investing your money – you're investing in your future." 
    "Together, let's unlock the full potential of your assets and build a brighter financial tomorrow. Welcome aboard!",
    )


# In[3]:


def calculate_risk_appetite(finpriority, risk, high_risk):
    # Assign numerical values to options
    options_mapping = {
        "Fully disagree": 1,
        "Rather disagree": 2,
        "Rather agree": 3,
        "Fully agree": 4
    }    
    # Calculate risk appetite based on responses
    risk_appetite = (options_mapping[finpriority] + options_mapping[risk] + options_mapping[high_risk]) / 3
    return risk_appetite

def calculate_risk_capacity(loss, min_loss):
    # Assign numerical values to options
    options_mapping = {
        "Fully disagree": 1,
        "Rather disagree": 2,
        "Rather agree": 3,
        "Fully agree": 4
    } 
    # Calculate risk capacity based on responses
    risk_capacity = (options_mapping[loss] + options_mapping[min_loss]) / 2
    return risk_capacity

def determine_risk_profile(risk_appetite, risk_capacity):
    # Define risk profile based on risk appetite and risk capacity
    if risk_appetite >= 3 and risk_capacity >= 3:
        return "Offensive"
    elif risk_appetite >= 3 and risk_capacity < 3:
        return "Defensive"
    else:
        return "Conservative"
    
    
def main():
    st.title("Risk-Reward Profile Assessment")
    
    finpriority = st.select_slider("I take financial matters seriously and security is my top priority.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    risk = st.select_slider("When it comes to my money, I am reluctant to take risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    high_risk = st.select_slider("I would like to achieve higher profits and therefore would be willing to take on higher risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    loss = st.select_slider("The risk of suffering losses on my assets concerns me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    min_loss = st.select_slider("Minimal losses also concern me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
  
    # Calculate risk appetite, risk capacity, and risk profile
    risk_appetite = calculate_risk_appetite(finpriority, risk, high_risk)
    risk_capacity = calculate_risk_capacity(loss, min_loss)
    risk_profile = determine_risk_profile(risk_appetite, risk_capacity)

    # Display results
    st.write("Risk Appetite:", risk_appetite)
    st.write("Risk Capacity:", risk_capacity)
    st.write("Risk Profile:", risk_profile)

if __name__ == "__main__":
    main()

