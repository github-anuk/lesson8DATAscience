import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


data=pd.read_csv("covid_data.csv")
data=data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
data.columns = ("state","country","late upd","lat","long",'confirmed','recovered','death','active')

data["state"].fillna(value = '',inplace= True)
print(data.head(10))

top10_confirmed= pd.DataFrame(data.groupby("country")['confirmed'].sum().nlargest(10).sort_values(ascending=False))
fig1 = px.scatter(top10_confirmed,x=top10_confirmed.index,y='confirmed',size='confirmed',size_max=120,color=top10_confirmed.index,title="TOP 10 COUNTRIES WITH CONFIRMED CASES")
fig1.write_html("Fig1.html",auto_open=True)

top10_oofs=pd.DataFrame(data.groupby('country')['death'].sum().nlargest(10).sort_values(ascending=False))
oofs=px.scatter(top10_oofs,x=top10_oofs.index,y='death',size='death',size_max=100,color=top10_oofs.index,title="COUNTRIES WITH THE MOST OOFS")
oofs.write_html('sadoofs.html',auto_open=True)

top10_YAY=pd.DataFrame(data.groupby('country')['recovered'].sum().nlargest(10).sort_values(ascending=False))
yay=px.bar(top10_YAY,x=top10_YAY.index,y='recovered',height=600,color='recovered',title='Top 10 Recovered Cases Countries',color_continuous_scale=px.colors.sequential.Viridis)
yay.write_html('YAYYAYAY.html',auto_open=True)