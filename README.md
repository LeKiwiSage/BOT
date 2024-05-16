## 💸: Stock Trading Bot P.I.C.T.E.T

Der P.I.C.T.E.T. (Primarily Invented for Creative Tax Evasion Tactics) Portfolio Optimizer ist eine Investitionsplattform, die Nutzern hilft, ihre Anlageportfolios zu optimieren. Die Anwendung ermöglicht es Nutzern, ihre Portfolios über mehrere Vermögenswerte zu erweitern, die auf ihr einzigartiges Risiko-Rendite-Profil zugeschnitten sind. Durch das Verständnis der Risikotoleranz, Anlageziele und Präferenzen des Nutzers bietet die Plattform personalisierte Anlagestrategien und Kauf-/Verkaufsempfehlungen basierend auf technischer Analyse.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pictet-stock-bot.streamlit.app/)

## Funktionen
- **Risiko-Rendite-Profiling**: Bewertet den Risikoappetit, die Kapazität und das Gesamtprofil des Nutzers durch einen Fragebogen.
- **Anlageempfehlungen**: Bietet personalisierte Kauf-/Verkaufsempfehlungen für Aktien basierend auf dem Nutzerprofil.
- **Aktienanalyse**: Ruft Aktienmarktdaten ab und analysiert diese, um Einblicke und aktuelle Preise bereitzustellen.
- **Interaktive Visualisierungen**: Zeigt Portfoliozusammensetzungen und Anlagemetriken durch Diagramme und Grafiken an.

## Installation
1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/LeKiwiSage/BOT.git
    cd BOT
    ```
    
2. Installieren Sie die erforderlichen Pakete:
    ```bash
    pip install -r requirements.txt
    ```

3. Starten Sie die Anwendung:
    ```bash
    streamlit run PICTET_BOT.py
    ```

## Nutzung
1. Öffnen Sie die Anwendung in Ihrem Webbrowser.
2. Füllen Sie den Fragebogen zur Risiko-Rendite-Bewertung aus.
3. Sehen Sie Ihr personalisiertes Risikoprofil und Anlageempfehlungen ein.
4. Erkunden Sie die Aktienanalyse und Visualisierungen.

## Verwendete APIs
Dieses Projekt nutzt die folgenden APIs:
- **[Alpha Vantage API](https://www.alphavantage.co/documentation/)**: Bietet Echtzeit- und historische Aktienmarktdaten.
- **[Yahoo Finance API](https://www.yahoofinanceapi.com/)**: (über die `yfinance` Bibliothek) Ruft historische Marktdaten ab.

## Code-Struktur
- `PICTET_BOT.py`: Hauptanwendungsdatei, die den Streamlit-App-Code enthält.
- `requirements.txt`: Listet die für das Projekt erforderlichen Python-Pakete auf.

## Beitragen
Beiträge sind willkommen! Wenn Sie Vorschläge oder Verbesserungen haben, senden Sie gerne eine Pull-Request.

## Lizenz
Dieses Projekt steht unter der Apache 2.0 Lizenz.

## Danksagungen
Besonderer Dank gilt den Entwicklern und Betreuern der in diesem Projekt verwendeten APIs:
- Alpha Vantage API
- Yahoo Finance API (über die `yfinance` Bibliothek)

## Autor
Entwickelt von Gruppe 2.1 CS HSG SP2024 (https://github.com/LeKiwiSage).
