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

top10_yas=pd.DataFrame(data.groupby('country')['recovered'].sum().nlargest(10).sort_values(ascending=False))
oofs=px.scatter(top10_yas,x=top10_yas.index,y='recovered',size='recovered',size_max=100,color=top10_yas.index,title="COUNTRIES WITH THE MOST RECOVERED")
oofs.write_html('SLAYY.html',auto_open=True)

top10_sad=pd.DataFrame(data.groupby('country')['death'].sum().nlargest(10).sort_values(ascending=False))
yay=px.bar(top10_sad,x=top10_sad.index,y='death',height=600,color='death',title='Top 10 death Cases Countries',color_continuous_scale=px.colors.sequential.Viridis)
yay.write_html('depressionz.html',auto_open=True)

top10_confirmed=pd.DataFrame(data.groupby('country')['confirmed'].sum().nlargest(10).sort_values(ascending=False))
yay=px.bar(top10_confirmed,x=top10_confirmed.index,y='confirmed',height=600,color='confirmed',title='Top 10 confirmed Cases Countries',color_continuous_scale=px.colors.sequential.Viridis)
yay.write_html('itzfreezed.html',auto_open=True)
