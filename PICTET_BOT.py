#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import yfinance as yf

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
    .questionnaire-header {
        font-size: 24px; 
        font-weight: bold;
    }
    .konservativ { color: green; }
    .moderat-konservativ { color: blue; }
    .moderat { color: orange; }
    .moderat-aggressiv { color: purple; }
    .aggressiv { color: red; }
</style>
""", unsafe_allow_html=True)

# Website Title
st.title('STOCK TRADING BOT')
st.subheader('Primarily Invented for Creative Tax Evasion Tactics (P.I.C.T.E.T) Portfolio Optimizer')
st.write('---')

# Welcome Statement
st.subheader('Lieber P.I.C.T.E.T.-Kunde')
st.markdown('\n\n')
txt = st.markdown("""
        <p span class="highlight-light-red bold">
            Willkommen auf Ihrer Investitionsplattform!</span>
        </p>

        <p class="text-justify">
            Wir freuen uns sehr, dass Sie bei uns sind und wir gemeinsam auf eine spannende Reise gehen. Unser Ziel ist einfach, aber ehrgeizig: Wir möchten Sie in die Lage versetzen, Ihr Anlageportfolio über mehrere Vermögenswerte zu erweitern, die genau auf Ihr <span class="red-text">einzigartiges Risiko-Ertrags-Profil</span> zugeschnitten sind.
        </p>

        <p class="text-justify">
            Indem wir Ihre <span class="italic">Risikotoleranz</span>, Ihre <span class="italic">Anlageziele</span> und Ihre <span class="italic">Präferenzen</span> kennenlernen, können wir eine <span class="highlight-light-red">persönliche Anlagestrategie</span> entwickeln, die Ihren Zukunftsvorstellungen entspricht, indem wir auf der Grundlage der technischen Analyse der von Ihnen vorgeschlagenen Aktienanlage <span class="bold">Kauf- oder Verkaufsempfehlungen</span> aussprechen.
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
    time_map = {"Weniger als 3 Jahre": 1, "3 bis 10 Jahre": 2, "Mehr als 10 Jahre": 3}
    income_map = {"Weniger als 100.000 CHF": 1, "Zwischen 100.000 und 250.000 CHF": 2, "Mehr als 250.000 CHF": 3}
    slider_map = {"Vollständig dagegen": 1, "Eher dagegen": 2, "Eher dafür": 3, "Vollständig dafür": 4}

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
        return "Verringert"
    elif risk_appetite < 3.5:
        return "Mittel"
    else:
        return "Erhöht"

def determine_risk_capacity_category(risk_capacity):
    if risk_capacity <= 1.5:
        return "Tief"
    elif risk_capacity <= 2.5:
        return "Mittel"
    else:
        return "Hoch"

def determine_risk_profile_category(risk_profile):
    if risk_profile < 2:
        return "Konservativ"
    elif risk_profile < 3:
        return "Moderat Konservativ"
    elif risk_profile < 4:
        return "Moderat"
    elif risk_profile < 5:
        return "Moderat Aggressiv"
    else:
        return "Aggressiv"

def main():
    st.subheader("Risiko-Reward Profilbewertung")
    
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
    st.markdown('<p class="questionnaire-header">Questionnaire</p>', unsafe_allow_html=True)

    options = ["Vollständig dagegen", "Eher dagegen", "Eher dafür", "Vollständig dafür"]
    time = st.selectbox("**Wie lange planen Sie zu investieren?**", ["Weniger als 3 Jahre", "3 bis 10 Jahre", "Mehr als 10 Jahre"])
    st.markdown('\n')
    income = st.selectbox("**Wie viel möchten Sie investieren?**", ["Weniger als 100.000 CHF", "Zwischen 100.000 und 250.000 CHF", "Mehr als 250.000 CHF"])
    st.markdown('\n')
    finpriority = st.select_slider("**Ich nehme finanzielle Angelegenheiten ernst, und Sicherheit hat für mich oberste Priorität.**", options=options)
    st.markdown('\n')
    risk = st.select_slider("**Wenn es um mein Geld geht, zögere ich, Risiken einzugehen.**", options=options)
    st.markdown('\n')
    high_risk = st.select_slider("**Ich möchte höhere Gewinne erzielen und wäre daher bereit, höhere Risiken einzugehen.**", options=options)
    st.markdown('\n')
    loss = st.select_slider("**Das Risiko, mit meinem Vermögen Verluste zu erleiden, macht mir Sorgen.**", options=options)
    st.markdown('\n')
    min_loss = st.select_slider("**Auch minimale Verluste machen mir Sorgen.**", options=options)

    st.markdown('\n')

    if st.button("Risiko-Reward-Profil berechnen"):
        risk_appetite, risk_capacity, risk_profile = calculate_risk_reward_profile(time, income, finpriority, risk, high_risk, loss, min_loss)
        
        risk_appetite_category = determine_risk_appetite_category(risk_appetite)
        risk_capacity_category = determine_risk_capacity_category(risk_capacity)
        risk_profile_category = determine_risk_profile_category(risk_profile)

        txt = st.markdown("""
        #### **Your following risk profile has been established based on your risk capacity and risk tolerance:**
        """)
        st.markdown('\n')
        st.write("Ihr Risiko Appetit:", f"<span class='{risk_appetite_category.lower().replace(' ', '-')}'><b>{risk_appetite_category}</b></span>", unsafe_allow_html=True)
        st.markdown('\n')
        st.write("Ihr Kapazitätsprofil:", f"<span class='{risk_capacity_category.lower().replace(' ', '-')}'><b>{risk_capacity_category}</b></span>", unsafe_allow_html=True)
        st.markdown('\n')
        st.write("Ihr Risikoprofil:", f"<span class='{risk_profile_category.lower().replace(' ', '-')}'><b>{risk_profile_category}</b></span>", unsafe_allow_html=True)
    
    st.markdown('\n')
    st.write('---')

if __name__ == "__main__":
    main()

     
    st.subheader("**P.I.C.T.E.T. Personalisierte Kauf-/Verkaufsvorschläge**")
    txt = st.markdown("""
        <p class="text-justify">
        Nach der Bewertung Ihres Risikoprofils (der vorhin eingefärbte Begriff) kann unsere Anlageplattform P.I.C.T.E.T. nun für Sie ermitteln, ob Sie eine Aktie aus Ihrem Portfolio kaufen oder verkaufen sollten. Dazu müssen Sie den Ticker (Symbol) der Aktie von der NYSE oder NASDAQ kennen. Bitte schauen Sie unter dieser URL nach, wenn Sie es nicht wissen (https://www.nyse.com/listings_directory/stock) und (https://www.nasdaq.com/market-activity/stocks/screener).
        </p>
        <p class="text-justify">
        Lassen Sie uns nun damit beginnen, eine bestimmte Aktie auszuwählen, über die Sie sich erkundigen möchten:
        </p>
    """, unsafe_allow_html=True)

# Aktienauswahl und -analyse mit Alpha Vantage API
def second_main():
    st.subheader("Stock Ticker Search")
    
    stock_symbol = st.text_input('**Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):**')
    
    if st.button("Search"):
        if stock_symbol:
            # Fetching current price
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=YOUR_API_KEY'
            response = requests.get(url)
            data = response.json()
            current_price = data.get('Global Quote', {}).get('05. price', 'Not available')
            st.write(f"Current price of {stock_symbol}: ${current_price}")

            # Loading historical data
            end_date = pd.Timestamp.today()
            start_date = end_date - pd.DateOffset(months=3)
            stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
            stock_data['SMA'] = stock_data['Close'].rolling(window=20).mean()
            average_close = stock_data['Close'].mean()
            latest_sma = stock_data['SMA'].iloc[-1]

            # Recommendation based on risk profile
            recommendation = 'Buy' if latest_sma > average_close else 'Sell'
            st.write(f"Recommendation based on your risk profile: {recommendation}")
            st.write(f"Average closing price of the last 3 months: ${average_close:.2f}")
            st.write(f"Current Simple Moving Average (SMA): ${latest_sma:.2f}")

            # Plotting stock data
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(stock_data['Close'], label='Closing Price')
            ax.plot(stock_data['SMA'], label='SMA (20 Days)')
            ax.set_title(f'Price Development of {stock_symbol}')
            ax.legend()
            st.pyplot(fig)
        else:
            st.write("Please enter the stock symbol.")

if __name__ == "__main__":
    second_main()
