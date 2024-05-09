#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title('P.I.C.T.E.T Portfolio Optimizer')

#Welcome Statement
txt = st.markdown(
    """
    :red-background[**Welcome to your investment platform!**]

    We are thrilled to have you onboard as we embark on an exciting journey together.
    Our goal is simple yet ambitious: to empower you to grow your investment portfolio 
    across multiple assets, tailored precisely to your :red[unique risk-reward profile].
    
    By understanding your ***risk tolerance***, ***investment goals***, and ***preferences***, we will 
    craft a :red-background[personalized investment strategy] that aligns with your vision for the future.
    
    Whether you are seeking steady growth, aggressive expansion, or somewhere in between, 
    our bot will work tirelessly to optimize your portfolio for maximum returns while managing risk effectively.
    
    With our investment fund, you're not just investing your money – **you're investing in your future**.
    Together, let's unlock the full potential of your assets and build a brighter financial tomorrow. 
    
    **Welcome aboard!**
    """)


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

def plot_risk_profile(risk_profile_category):
    categories = ["Conservative", "Moderately Conservative", "Moderate", "Moderately Aggressive", "Aggressive"]
    colors = ['red' if cat == risk_profile_category else 'blue' for cat in categories]

    fig, ax = plt.subplots()
    ax.barh(categories, [1]*len(categories), color=colors, height=0.5)
    ax.set_xlim(0, 1)  # Adjust based on the scale you want
    ax.set_xlabel('Risk Profile')
    ax.set_title('User Risk Profile')
    ax.grid(False)

    st.pyplot(fig)

def main():
    st.subheader("Risk-Reward Profile Assessment")
    
    # Questionnaire
    time = st.selectbox("How long do you plan to invest your money?", ("Less than 3 years", "3 to 10 years", "More than 10 years"))
    income = st.selectbox("How much money do you plan to invest into the fund?", ("Less than 100000 CHF", "Between 100000 and 250000 CHF", "More than 250000 CHF"))
    finpriority = st.select_slider("I take financial matters seriously and security is my top priority.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    risk = st.select_slider("When it comes to my money, I am reluctant to take risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    high_risk = st.select_slider("I would like to achieve higher profits and therefore would be willing to take on higher risks.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    loss = st.select_slider("The risk of suffering losses on my assets concerns me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    min_loss = st.select_slider("Minimal losses also concern me.", options=["Fully disagree", "Rather disagree", "Rather agree", "Fully agree"])
    
    if st.button("Calculate Risk-Reward Profile"):
        risk_appetite, risk_capacity, risk_profile = calculate_risk_reward_profile(time, income, finpriority, risk, high_risk, loss, min_loss)
        
        risk_appetite_category = determine_risk_appetite_category(risk_appetite)
        risk_capacity_category = determine_risk_capacity_category(risk_capacity)
        risk_profile_category = determine_risk_profile_category(risk_profile)

        txt = st.markdown("""**The following risk profile has been prepared based on your risk capacity and risk tolerance:**""")
        st.write("Risk Appetite:", risk_appetite_category)
        st.write("Risk Capacity:", risk_capacity_category)
        st.write("Risk Profile:", risk_profile_category)

        plot_risk_profile(risk_profile_category)
        
if __name__ == "__main__":
    main()
