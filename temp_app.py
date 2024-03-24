import streamlit as st
import plotly.express as px
# import pandas as pd
import sqlite3

connection = sqlite3.connect("data_temp.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM world_temp")
dates = cursor.fetchall()

dates = [item for t in dates for item in t]
# dates = [item[0] for item in dates]
print(dates)

cursor.execute("SELECT temperature FROM world_temp")
temperatures = cursor.fetchall()

temperatures = [item for t in temperatures for item in t]
# temperatures = [item[0] for item in temperatures]
print(temperatures)

# df = pd.read_csv("data.txt")

st.title("Average World Temperature")

# figure = px.line(x=df["date"], y=df["temperature"],
#                  labels={"x": "Date", "y": "Temperature (Celsius)"})
# st.plotly_chart(figure)

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (Celsius)"})
st.plotly_chart(figure)