#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as datetime

st.title('STOCK TRADING BOT')
st.subheader('Primarily Invented for Creative Tax Evasion Tactics (P.I.C.T.E.T) Portfolio Optimizer')
st.write('---')

# Custom CSS style for text justification
st.markdown("""
<style>
    .text-justify {
        text-align: justify;
    }
    .highlight-light-red {
        background-color: #FFE9E9; 
    }
    .bold {
        font-weight: bold;
    }
      .italic {
        font-style: italic;
    }
    .red-text {
        color: #e32417;
    }
</style>
""", unsafe_allow_html=True)

##Welcome Statement
st.subheader('Dear client P.I.C.T.E.T')
st.markdown('\n\n')
txt = st.markdown("""
        <p span class="highlight-light-red bold">
            Willkommen auf Ihrer Investitionsplattform!</span>
        </p>

        <p class="text-justify">
            Wir freuen uns sehr, dass Sie bei uns sind und wir gemeinsam auf eine spannende Reise gehen. Unser Ziel ist einfach, aber ehrgeizig: Wir möchten Sie in die Lage versetzen, Ihr Anlageportfolio über mehrere Vermögenswerte zu erweitern, die genau auf Ihr <span class="red-text">einzigartiges Risiko-Ertrags-Profil</span> zugeschnitten sind.
        </p>

        <p class="text-justify">
            Indem wir Ihre <span class="italic">Risikotoleranz</span>, Ihre <span class="italic">Anlageziele</span> und Ihre <span class="italic">Präferenzen</span> kennenlernen, können wir eine <span class="highlight-light-red">persönliche Anlagestrategie</span> entwickeln, können wir eine personalisierte Anlagestrategie entwickeln, die Ihren Zukunftsvorstellungen entspricht, indem wir auf der Grundlage der technischen Analyse der von Ihnen vorgeschlagenen Aktienanlage <span class="bold">Kauf- oder Verkaufsempfehlungen</span> aussprechen.
        </p>

        <p class="text-justify">
            Ganz gleich, ob Sie ein stetiges Wachstum, eine aggressive Expansion oder irgendetwas dazwischen anstreben, unser Bot wird unermüdlich daran arbeiten, Ihr Portfolio für maximale Renditen zu optimieren und gleichzeitig das Risiko effektiv zu steuern.
        </p>

        <p class="text-justify">
            Mit unserem Investmentfonds investieren Sie nicht nur Ihr Geld - <span class="bold">Sie investieren in Ihre Zukunft</span>. Lassen Sie uns gemeinsam das volle Potenzial Ihres Vermögens ausschöpfen und eine bessere finanzielle Zukunft aufbauen.
        </p>

        <p span class="highlight-light-red bold">
            Willkommen an Bord!</span>
        </p>
""", unsafe_allow_html=True)

# Image load & display
image_url = "https://static.vecteezy.com/system/resources/previews/012/806/386/original/3d-businessman-buying-or-selling-shares-investing-in-stock-market-from-mobile-phone-candlestick-chart-of-stock-sale-and-buy-using-mobile-phones-market-investment-trading-3d-rendering-png.png"
st.image(image_url, caption='Image Free of Use under Creative Commons license', use_column_width=True)

st.write('---')

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

def main():
    st.subheader("Risk-Reward Profile Assessment")
    
    # Text with justified alignment
    st.markdown("""
        <p class="text-justify">
        Um Ihre Investitionen zu optimieren, ist es von größter Bedeutung, Ihre Risikotoleranz und Ihre finanziellen Ziele <b>zu verstehen</b>. Indem wir Ihnen <mark class="highlight-light-red">maßgeschneiderte Fragen</mark> zu Ihren <i>Risikofähigkeiten</i> und <i>Anlagezielen</i> stellen, gewährleisten wir <span style="color:red"><b>personalisierte Strategien</b></span>, die genau auf Ihre Bedürfnisse und Wünsche abgestimmt sind. Lassen Sie uns diese Reise gemeinsam antreten.
        </p>
        """, unsafe_allow_html=True)
    
    st.markdown('\n')
    st.markdown("""
        <p class="text-justify">
        Mit den nächsten <span class="bold">7 Fragen</span> können Sie Ihr aktuelles Risikoprofil <span class="highlight-light-red">in eines der 5 verschiedenen verfügbaren Profile einordnen.</span> Vergewissern Sie sich, dass Sie die richtigen Antworten geben, um anschließend die genauesten Kauf-/Verkaufsvorschläge zu erhalten.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('\n')
  
    
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

if __name__ == "__main__":
    main()
