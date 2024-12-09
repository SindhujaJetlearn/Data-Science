
# Data Analysis on Covid Data Set (Part - 2 Time Series Data Analysis)

# Open the data in excel and explain the data and columns data
# Explain what is time-series data, Special Emphasis on Date_reported column present

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plotly is same as Matplotlib but with higher graphic standards
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Import the data
#Encoding = 'ISO-8859-1' refers to the ISO standard Latin-1 character set and encoding format
data = pd.read_csv('WHO-COVID-19-global-data.csv', encoding = 'ISO-8859-1')
data.columns = ("Date_reported","Country_code","Country","WHO_region","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths")

# Date_Reported column is string, typecast it to datatime format
data["Date_reported"] = pd.to_datetime(data["Date_reported"])

data_dates = data.groupby('Date_reported').sum()

# Plot the basic graphs below and explain the results
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x = data_dates.index, y = data_dates['Cumulative_cases'], fill = 'tonexty', line_color = 'blue'))
fig1.update_layout(title = 'Cumulative Cases Worldwide')
fig1.write_html('Fig1.html', auto_open=True)


fig2 = go.Figure()
fig2.add_trace(go.Scatter(x = data_dates.index, y = data_dates['Cumulative_deaths'], fill = 'tonexty', line_color = 'red'))
fig2.update_layout(title = 'Cumulative Deaths Worldwide')
fig2.write_html('fig2.html', auto_open=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x = data_dates.index, y = data_dates['New_cases'], fill = 'tonexty', line_color = 'gold'))
fig3.update_layout(title = 'Daily New Cases Worldwide')
fig3.write_html('fig3.html', auto_open=True)


fig4 = go.Figure()
fig4.add_trace(go.Scatter(x = data_dates.index, y = data_dates['New_deaths'], fill = 'tonexty', line_color = 'hotpink'))
fig4.update_layout(title = 'Daily Death Cases Worldwide')
fig4.write_html('fig4.html', auto_open=True)

# Ask the student for taking a country as homework and draw the same graphs again showing the trend for the particular country as homework
