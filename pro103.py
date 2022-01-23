import pandas as pd
import plotly.express as px

df = pd.read_csv("covid.csv")
#fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
#fig = px.bar(df, x = "Year", y = "Per capita income")
fig = px.scatter(df, x = "date", y = "cases", color = "country", size = "cases", size_max = 30)
fig.show()

