{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b9f3e9e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import math\n",
    "from empyrial import empyrial, Engine\n",
    "import matplotlib.pyplot as plt\n",
    "import yfinance as yf\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "281d95ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-09 11:06:44.879 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\bojar\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.title('P.I.C.T.E.T Portfolio Optimizer')\n",
    "\n",
    "\n",
    "#Welcome Statement\n",
    "txt = st.text_area(\n",
    "    \"Welcome to our investment platform!\",\n",
    "    \"We are thrilled to have you onboard as we embark on an exciting journey together.\"\n",
    "    \"Our goal is simple yet ambitious: to empower you to grow your investment portfolio\" \n",
    "    \"across multiple assets, tailored precisely to your unique risk-reward profile.\"\n",
    "    \"By understanding your risk tolerance, investment goals, and preferences, we will\" \n",
    "    \"craft a personalized investment strategy that aligns with your vision for the future.\"\n",
    "    \"Whether you are seeking steady growth, aggressive expansion, or somewhere in between,\" \n",
    "    \"our bot will work tirelessly to optimize your portfolio for maximum returns while managing risk effectively.\"\n",
    "    \"With our investment fund, you're not just investing your money – you're investing in your future.\" \n",
    "    \"Together, let's unlock the full potential of your assets and build a brighter financial tomorrow. Welcome aboard!\",\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "25474222",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Auswahl der Risk-Reward Profile\n",
    "Questionnaire_Time = st.selectbox(\n",
    "    \"How long do you plan to invest your money?\",\n",
    "    (\"Less than 3 years\", \"3 to 10 years\", \"More than 10 years\"))\n",
    "\n",
    "st.write(\"You selected:\", Questionnaire_Time)\n",
    "\n",
    "#Questionnaire about the income of the user\n",
    "Questionnaire_Income = st.selectbox(\n",
    "    \"How much money do you plan to invest into the fund?\",\n",
    "    (\"Less than 100000 CHF\", \"Between 100000 and 250000 CHF\", \"More than 250000 CHF\"))\n",
    "\n",
    "st.write(\"You selected:\", Questionnaire_Income)\n",
    "\n",
    "#Questionnaire about the financial priorities of the user\n",
    "Questionnaire_FinPriority = st.select_slider(\n",
    "    \"I take financial matters seriously and security is my top priority.\",\n",
    "    options=[\"Fully disagree\", \"Rather disagree\", \"Rather agree\", \"Fully agree\"])\n",
    "\n",
    "#Questionnaire about the risk tolerance of the user\n",
    "Questionnaire_Risk = st.select_slider(\n",
    "    \"When it comes to my money, I am reluctant to take risks.\",\n",
    "    options=[\"Fully disagree\", \"Rather disagree\", \"Rather agree\", \"Fully agree\"])\n",
    "\n",
    "st.write(\"You selected\", Questionnaire_Risk)\n",
    "\n",
    "#Questionnaire about the maximal risk tolerance of the user\n",
    "Questionnaire_HRisk = st.select_slider(\n",
    "    \"I would like to achieve higher profits and therefore would be willing to take on higher risks.\",\n",
    "    options=[\"Fully disagree\", \"Rather disagree\", \"Rather agree\", \"Fully agree\"])\n",
    "\n",
    "st.write(\"You selected\", Questionnaire_HRisk)\n",
    "\n",
    "#Questionnaire about the loss tolerance of the user\n",
    "Questionnaire_Loss = st.select_slider(\n",
    "    \"The risk of suffering losses on my assets concerns me.\",\n",
    "    options=[\"Fully disagree\", \"Rather disagree\", \"Rather agree\", \"Fully agree\"])\n",
    "\n",
    "st.write(\"You selected\", Questionnaire_Loss)\n",
    "\n",
    "#Questionnaire about the minimal loss tolerance of the user\n",
    "Questionnaire_MinLoss = st.select_slider(\n",
    "    \"Minimal losses also concern me.\",\n",
    "    options=[\"Fully disagree\", \"Rather disagree\", \"Rather agree\", \"Fully agree\"])\n",
    "\n",
    "st.write(\"You selected\", Questionnaire_MinLoss)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
