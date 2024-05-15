import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests


### Abschnitt für Funktionen, die im Code wiederverwendet werden ###

## CSS-Styling-Optionen ##
def load_css():
    css = """
    /* Textausrichtung */
    .text-justify {
        text-align: justify;
    } 
    
    /* hellrot hervorheben */
    .highlight-light-red {
        background-color: #FFE9E9; 
    }
    
    /* Text fett formatieren */
    .bold {
        font-weight: bold;
    }
    
    /* Text italic formatieren */
    .italic {
        font-style: italic;
    }
    
    /* Text in rot formatieren */
    .red-text {
        color: #e32417;
    }
    
    /* Text in bestimmter Größe formatieren */
    .questionnaire-header {
        font-size: 24px; 
        font-weight: bold;
    }
    
    /* Ergebnis der Risikoprofilanalyse farblich hervorgehoben */
    .konservativ { color: green; }
    .moderat-konservativ { color: blue; }
    .moderat { color: orange; }
    .moderat-aggressiv { color: purple; }
    .aggressiv { color: red; }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True) #Rendert benutzerdefinierte CSS-Stile 
load_css()                                                       #Laden und Anwenden benutzerdefinierter CSS-Stile auf das Streamlit

## Hilfsfunktion für die Sektionstrennung ##
def separator():
    st.markdown('---')
    
## Hilfsfunktion für Zeilensprung ##
def empty_line(n=1):
    st.markdown('\n' * n, unsafe_allow_html=True)

## Hilfsfunktion für Zwischenüberschriften ##
def section_header(text):
    st.subheader(f" {text}")

## Hilfsfunktion zur Erstellung von Textabsätzen in CSS ##  
def section_paragraph(*text_styles):
    styled_text_parts = []                                                                       # Initialisiere leere Liste, um gestaltete Textteile zu speichern
    for text, style_classes in text_styles:                                                      # Iterieren über jedes Textstiltupel, das als Eingabeargumente angegeben wurde
        if text == "":                                                                           # Prüfen, ob Text leer ist
            styled_text_parts.append("<br><br>")                                                 # Wenn der Text leer ist, fügen zwei Zeilenumbrüche ein, um eine leere Zeile zu erzeugen
        else:
             styled_text_parts.append(f'<span class="{style_classes}">{text}</span>')            # Wenn Text nicht leer ist, konstruiere gestylten Text mit den angegebenen Stilklassen
    text_with_styles = " ".join(styled_text_parts)                                               # Zusammenfügen der gestylten Textteile zu einer einzigen Zeichenkette
    st.markdown(f"<div class='text-justify'>{text_with_styles}</div>", unsafe_allow_html=True)   # Rendering gestalteter Text innerhalb eines div mit Textausrichtung


### Einleitung Absatz ###

## Einleitende Texte ##
def introduction():
    st.title('Stock Trading Bot')   # Website-Titel
    section_header('Primarily Invented for Creative Tax Evasion Tactics (P.I.C.T.E.T) Portfolio Optimizer')      # Abschnittsüberschrift für die Einleitung anzeigen
    separator()
    
    # Willkommens-Nachricht
    section_header('Lieber P.I.C.T.E.T.-Kunde')
    empty_line(2)
    
    # Texteingabe mit diversen zuvor definierten CSS-Klassen wie kursiv, etc. ; ("", "") ist für die Erstellung eines Zeilenumbruchs und eines Sprungs
    section_paragraph(
        ("Willkommen auf Ihrer Investitionsplattform!", "bold highlight-light-red"),
        ("", ""),     
        ("Wir freuen uns sehr, dass Sie bei uns sind und wir gemeinsam auf eine spannende Reise gehen. Unser Ziel ist einfach, aber ehrgeizig: Wir möchten Sie in die Lage versetzen, Ihr Anlageportfolio über mehrere Vermögenswerte zu erweitern, die genau, auf Ihr", ""),
        ("einzigartiges Risiko-Ertrags-Profil", "red-text"),
        ("zugeschnitten sind.", ""),
        ("Indem wir Ihre", ""),
        ("Risikotoleranz,", "italic"), 
        ("Ihre", ""),
        ("Anlageziele", "italic"),
        ("und Ihre", ""),
        ("Präferenzen", "italic"),
        ("kennenlernen, können wir eine", ""),
        ("persönliche Anlagestrategie", "highlight-light-red"), 
        ("entwickeln, die Ihren Zukunftsvorstellungen entspricht, indem wir auf der Grundlage der technischen Analyse der von Ihnen vorgeschlagenen Aktienanlage", ""),
        ("Kauf- oder Verkaufsempfehlungen", "bold"),
        ("aussprechen", ""),
        ("", ""),
        ("Ganz gleich, ob Sie ein stetiges Wachstum, eine aggressive Expansion oder irgendetwas dazwischen anstreben, unser Bot wird unermüdlich daran arbeiten, Ihr Portfolio für maximale Renditen zu optimieren und gleichzeitig das Risiko effektiv zu steuern.", ""),
        ("", ""),
        ("Mit unserem Investmentfonds investieren Sie nicht nur Ihr Geld -", ""),
        ("Sie investieren in Ihre Zukunft.", "bold"),
        ("Lassen Sie uns gemeinsam das volle Potenzial Ihres Vermögens ausschöpfen und eine bessere finanzielle Zukunft aufbauen.", ""),
        ("",""),
        ("Willkommen an Bord!", "bold highlight-light-red"),
        ("", "")
    )

    # Bild laden & anzeigen
    image_url = "https://static.vecteezy.com/system/resources/previews/012/806/386/original/3d-businessman-buying-or-selling-shares-investing-in-stock-market-from-mobile-phone-candlestick-chart-of-stock-sale-and-buy-using-mobile-phones-market-investment-trading-3d-rendering-png.png"
    st.image(image_url, caption='Image Free of Use under Creative Commons license', use_column_width=True)

    separator()


### Abschnitt zur Bewertung des Risiko-Ertrags-Profils ###

## Einleitende Texte ##
def risiko_ertrag_profile():
    section_header('Risiko-Reward Profilbewertung')
    
    # Texteingabe mit diversen zuvor definierten CSS-Klassen wie kursiv, etc. ; ("", "") ist für die Erstellung eines Zeilenumbruchs und eines Sprungs
    section_paragraph(
        ("Um Ihre Investitionen zu optimieren, ist es von größter Bedeutung, Ihre Risikotoleranz und Ihre finanziellen Ziele", ""),
        ("zu verstehen.", "bold"),
        ("Indem wir Ihnen", ""), 
        ("maßgeschneiderte Fragen", "highlight-light-red"),
        ("zu Ihren", ""), 
        ("Risikofähigkeiten", "italic"),
        ("und", ""), 
        ("Anlagezielen", "italic"), 
        ("stellen, gewährleisten wir", ""), 
        ("personalisierte Strategien", "bold red-text"),
        (", die genau auf Ihre Bedürfnisse und Wünsche abgestimmt sind. Lassen Sie uns diese Reise gemeinsam antreten.", ""),
        ("", ""),
        ("Mit den nächsten", ""),
        ("7 Fragen", "bold"),
        ("können Sie Ihr aktuelles Risikoprofil", ""),
        ("in eines der 5 verschiedenen verfügbaren Profile einordnen.", "highlight-light-red"),
        ("Vergewissern Sie sich, dass Sie die richtigen Antworten geben, um anschließend die genauesten Kauf-/Verkaufsvorschläge zu erhalten.", ""),
        ("", "")
    ) 

    section_paragraph(("Questionnaire", "questionnaire-header")) # Untertitel für den Fragebogen
    empty_line()


## Definition der Risikoklassifikationen ##

# Kategorisierung nach 3 Arten von Risikobereitschaft auf Grundlage einer numerischen Punktzahl aus Fragebogengröße und Finanzstandards
def risk_appetite_category(risk_appetite):
    if risk_appetite < 2.5:              
        return "Verringert"
    elif risk_appetite < 3.5:       
        return "Mittel"
    else:
        return "Erhöht"

# Kategorisierung nach 3 Arten von Risikokapazität auf Grundlage einer numerischen Punktzahl aus Fragebogengröße und Finanzstandards
def risk_capacity_category(risk_capacity):
    if risk_capacity <= 1.5:
        return "Tief"
    elif risk_capacity <= 2.5:
        return "Mittel"
    else:
        return "Hoch"

# Kategorisierung nach 5 Arten von Risikoprofils auf Grundlage einer numerischen Punktzahl aus Fragebogengröße und Finanzstandards
def risk_profile_category(risk_profile):
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


## Definition des Fragebogens zum Risikoprofiling ##
def risk_profile_questionnaire():
    # Definition der Zeit- und Einkommensoptionen
    time_options = {"Weniger als 3 Jahre": 1, "3 bis 10 Jahre": 2, "Mehr als 10 Jahre": 3}
    income_options = {"Weniger als 100.000 CHF": 1, "Zwischen 100.000 und 250.000 CHF": 2, "Mehr als 250.000 CHF": 3}
    
    # Abfrage geplanten Investitionsdauer und Investitionsbetrags
    time = st.selectbox("**Wie lange planen Sie zu investieren?**", list(time_options.keys()))
    empty_line()
    income = st.selectbox("**Wie viel möchten Sie investieren?**", list(income_options.keys()))
    empty_line()
    
    # Zuordnung ausgewählten Zeit- und Einkommensoptionen zu Zahlenwerten
    time_value = time_options[time]
    income_value = income_options[income]

    # Abfrage von Risikopräferenzen mithilfe von Schiebereglern
    options = ["Vollständig dagegen", "Eher dagegen", "Eher dafür", "Vollständig dafür"]   # Vier Optionsmöglichkeiten
    finpriority = st.select_slider("**Ich nehme finanzielle Angelegenheiten ernst, und Sicherheit hat für mich oberste Priorität.**", options=options, value="Vollständig dagegen")
    empty_line()
    risk = st.select_slider("**Wenn es um mein Geld geht, zögere ich, Risiken einzugehen.**", options=options, value="Vollständig dagegen")
    empty_line()    
    high_risk = st.select_slider("**Ich möchte höhere Gewinne erzielen und wäre daher bereit, höhere Risiken einzugehen.**", options=options, value="Vollständig dagegen")
    empty_line()    
    loss = st.select_slider("**Das Risiko, mit meinem Vermögen Verluste zu erleiden, macht mir Sorgen.**", options=options, value="Vollständig dagegen")
    empty_line()    
    min_loss = st.select_slider("**Auch minimale Verluste machen mir Sorgen.**", options=options, value="Vollständig dagegen")
    empty_line()

    # Berechnung Risiko-Reward-Profils bei Klick auf Schaltfläche
    if st.button("Risiko-Reward-Profil berechnen"):
            risk_appetite, risk_capacity, risk_profile = calculate_risk_profile(time, income, finpriority, risk, high_risk, loss, min_loss)

            #Kategorisierung des Risiko-/Ertragsprofils anhand zuvor definierter Kategorisierungsfunktionen
            risk_appetite = risk_appetite_category(risk_appetite)
            risk_capacity = risk_capacity_category(risk_capacity)
            risk_profile = risk_profile_category(risk_profile)

            # Anzeige Risiko-/Ertragsprofils mit Hilfe CSS-Befehls
            txt = st.markdown("""#### **Ihr folgendes Risikoprofil wurde auf der Grundlage Ihrer Risikofähigkeit und Risikotoleranz erstellt:**""")
            st.write("Ihr Risiko Appetit:",  f"<span class='{risk_appetite.lower().replace(' ', '-')}'><b>{risk_appetite}</b></span>", unsafe_allow_html=True)
            st.write("Ihr Kapazitätsprofil:", f"<span class='{risk_capacity.lower().replace(' ', '-')}'><b>{risk_capacity}</b></span>", unsafe_allow_html=True)
            st.write("Ihr Risikoprofil:", f"<span class='{risk_profile.lower().replace(' ', '-')}'><b>{risk_profile}</b></span>", unsafe_allow_html=True)
    
    empty_line()
    separator()


## Rechnerische Definition des Risikoprofilings ##
def calculate_risk_profile(time, income, finpriority, risk, high_risk, loss, min_loss):
    
    # Definierte Sliderbox-Optionen für Zeit und Einkommen
    time_options = {"Weniger als 3 Jahre": 1, "3 bis 10 Jahre": 2, "Mehr als 10 Jahre": 3}
    income_options = {"Weniger als 100.000 CHF": 1, "Zwischen 100.000 und 250.000 CHF": 2, "Mehr als 250.000 CHF": 3}

    # Verknüpfung von Schiebereglerwerten mit numerischen Werten
    slider_values = {"Vollständig dagegen": 1, "Eher dagegen": 2, "Eher dafür": 3, "Vollständig dafür": 4}
    time_value = time_options[time]
    income_value = income_options[income]

    # Berechnung Risikobereitschaft, Risikofähigkeit & Risikoprofils mit verschiedenen Fragebogenergebnissen, die für jeden funktion wichtig sind.
    risk_appetite = (slider_values[finpriority] + slider_values[high_risk]) / 2
    risk_capacity = (time_value + income_value) / 2
    risk_profile = (slider_values[risk] + slider_values[loss] + slider_values[min_loss]) / 3

    return risk_appetite, risk_capacity, risk_profile


### Sektion für den Kauf/Verkaufsvorschlag & Aktiensuche mit Grafik und Analysen ###

##  Kauf/Verkaufsvorschlag ##
def proposition_buy_sell():
    section_header('P.I.C.T.E.T. Personalisierte Kauf-/Verkaufsvorschläge')
    
    # Texteingabe mit diversen zuvor definierten CSS-Klassen wie kursiv, etc. ; ("", "") ist für die Erstellung eines Zeilenumbruchs und eines Sprungs
    section_paragraph(
        ("Nach der Bewertung Ihres Risikoprofils (der vorhin eingefärbte Begriff) kann unsere Anlageplattform P.I.C.T.E.T. nun für Sie ermitteln,", ""), 
        ("ob Sie eine Aktie aus Ihrem Portfolio kaufen oder verkaufen sollten. Dazu müssen Sie den Ticker (Symbol) der Aktie von der NYSE oder NASDAQ kennen.", ""), 
        ("Bitte schauen Sie unter dieser URL nach, wenn Sie es nicht wissen (https://www.nyse.com/listings_directory/stock) und (https://www.nasdaq.com/market-activity/stocks/screener)", ""),
        ("", ""),
        ("Lassen Sie uns nun damit beginnen, eine bestimmte Aktie auszuwählen, über die Sie sich erkundigen möchten:", "")
    )
    empty_line()

## Aktiensuche mit Grafik und Analysen ##
def stock_finder():
    # Auswahl der Aktie
    stock_symbol = st.text_input('**Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):**')

    if stock_symbol:
        # API URL für den aktuellen Kurs
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=NBNWK0B3DGAYJGFH'
        response = requests.get(url)
        data = response.json()

        # Versucht aktuellen Kurs des angegebenen Aktiensymbols von API abzurufen und anzuzeigen 
        try:
            current_price = data['Global Quote']['05. price']
            st.write(f"Aktueller Kurs von {stock_symbol}: ${current_price}")
       
        # Zeigt Fehlermeldung, wenn Abruf fehlschlägt oder Symbol ungültig.
        except KeyError:
            st.error('Fehler beim Abrufen des aktuellen Kurses. Bitte überprüfen Sie das Symbol und versuchen Sie es erneut.')
    
        # Laden der Aktiendaten für die letzten 3 Monate
        end_date = pd.Timestamp.today()  # heutiges Datum
        start_date = end_date - pd.DateOffset(months=3)  # Datum vor drei Monaten
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)  # Daten-Download von Yahoo Finance

        # Überprüfung, ob der stock_data DataFrame nicht leer ist
        if not stock_data.empty:
            stock_data['SMA'] = stock_data['Close'].rolling(window=3).mean()  # Berechnung des gleitenden Durchschnitts
            latest_close = stock_data['Close'].iloc[-1]
            latest_sma = stock_data['SMA'].iloc[-1]
    
            # Durchschnitt der Schlusskurse über die letzten 3 Monate
            average_close = stock_data['Close'].mean()
    
            # Empfehlung mit Hervorhebung darstellen
            if latest_close > latest_sma:
                recommendation = 'Kaufen'
                st.success(f"Empfehlung: {recommendation}")
            else:
                recommendation = 'Verkaufen'
                st.error(f"Empfehlung: {recommendation}")

            # Anzeige 3 Monate durchschnittlichen Schlusskurses & SMA
            st.write(f"Durchschnittlicher Schlusskurs der letzten 3 Monate: ${average_close:.2f}")
            st.write(f"Aktueller gleitender Durchschnitt (SMA): ${latest_sma:.2f}")
    
            # Erste Grafik: Kursentwicklung
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(stock_data['Close'], label='Schlusskurs')
            ax.plot(stock_data['SMA'], label='SMA')
            ax.set_title('Kursentwicklung für ' + stock_symbol)
            ax.set_xlabel('Datum')
            ax.set_ylabel('Schlusskurs ($)')
            ax.legend()
            st.pyplot(fig)
    
            # Zweite Grafik: Beispiel für eine Portfolioverteilung
            st.subheader('Beispielhafte Portfolioverteilung')
            portfolio_data = {"AAPL": 30, "MSFT": 30, "GOOGL": 20, "AMZN": 20} # Zufällig gewählte Gewichtszahlen
            fig2, ax2 = plt.subplots()
            ax2.pie(portfolio_data.values(), labels=portfolio_data.keys(), autopct='%1.1f%%', startangle=90)  # Erstellung Tortendiagramms mit portfolio_data-Werten als Größen, Schlüsseln als Beschriftungen, Prozentsätzen mit Dezimalstelle und 90 Grad Startwinkel.
            ax2.axis('equal')  # Gleiches Seitenverhältnis, damit der Pie als Kreis gezeichnet wird.        
            st.pyplot(fig2)

        # Wenn leer, Fehlermeldung mit Aufforderung das Symbol zu ändern angezeigt
        else:
            st.error('Keine historischen Daten für das Symbol gefunden. Bitte versuchen Sie mit ein anderes Symbol')

# Definition der Hauptfunktion, in der alle benötigten Funktionen aufgerufen werden und die Programmausführung gesteuert wird
def main():
    introduction()
    risiko_ertrag_profile()
    risk_profile_questionnaire()
    proposition_buy_sell()
    stock_finder()
    
# Überprüft, ob das Skript direkt ausgeführt wird und ruft dann die Hauptfunktion main() auf 
if __name__ == "__main__":
    main()
