import pandas as pd
sdg = pd.read_csv('https://www.dropbox.com/s/fsxgf885s1f5bro/sdg_12_tickers.csv?dl=1',on_bad_lines='skip')
esg = pd.read_csv('https://www.dropbox.com/s/7h3k7v6z67q80df/esg_12_tickers.csv?dl=1',on_bad_lines='skip')
sent = pd.read_csv('https://www.dropbox.com/s/hv3p1d3xt4l9yvc/sentiment_12_tickers.csv?dl=1',on_bad_lines='skip')
sdg.head()
esg.head()
sent.head()
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pickle
import plotly.express as px
ticker = sdg['Ticker'].unique()
ticker
ticker1 = esg['Ticker'].unique()
ticker1
ticker2 = sent['Ticker'].unique()
ticker2
x=sdg.iloc[-1,41]
ticker
sdg.tail()
date=sdg.iloc[-1,0]
date
sec=pd.DataFrame(sdg['GICS Sector'].unique(),columns=['Sector'])
ti=pd.DataFrame(sdg['Ticker'].unique(),columns=['Ticker'])
st = pd.concat([sec,ti],axis=1)
st['Date']=''
st.fillna(0)

st=pd.read_csv('st.csv')
st=st.mask(st=='')
st=st.fillna(date)
st
stts=pd.read_csv('stts.csv')
upt=sdg['Ticker']
sdg['Ticker'].unique()
IBM=[]
XOM=[]
UNP=[]
DUK=[]
UNH=[]
JPM=[]
AMZN=[]
KO=[]
AAPL=[]
FB=[]
AMT=[]
TSLA=[]
for i in range(len(upt)):
    if upt[i] =='IBM':
        IBM.append(sdg.loc[i])
    if upt[i] =='XOM':
        XOM.append(sdg.loc[i])
    if upt[i] =='UNP':
        UNP.append(sdg.loc[i])
    if upt[i] =='DUK':
        DUK.append(sdg.loc[i])
    if upt[i] =='UNH':
        UNH.append(sdg.loc[i])
    if upt[i] =='JPM':
        JPM.append(sdg.loc[i])
    if upt[i] =='AMZN':
        AMZN.append(sdg.loc[i])
    if upt[i] =='KO':
        KO.append(sdg.loc[i])
    if upt[i] =='AAPL':
        AAPL.append(sdg.loc[i])
    if upt[i] =='FB':
        FB.append(sdg.loc[i])
    if upt[i] =='AMT':
        AMT.append(sdg.loc[i])
    if upt[i] =='TSLA':
        TSLA.append(sdg.loc[i])
d1=pd.DataFrame(IBM)
d2=pd.DataFrame(XOM)
d3=pd.DataFrame(UNP)
d4=pd.DataFrame(DUK)
d5=pd.DataFrame(UNH)
d6=pd.DataFrame(JPM)
d7=pd.DataFrame(AMZN)
d8=pd.DataFrame(KO)
d9=pd.DataFrame(AAPL)
d10=pd.DataFrame(FB)
d11=pd.DataFrame(AMT)
d12=pd.DataFrame(TSLA)

mom7= pd.DataFrame([d1.iloc[-1,42]-d1['STS_Mean'].rolling(window=7).mean().iloc[-1],
d2.iloc[-1,42]-d2['STS_Mean'].rolling(window=7).mean().iloc[-1],
d3.iloc[-1,42]-d3['STS_Mean'].rolling(window=7).mean().iloc[-1],
d4.iloc[-1,42]-d4['STS_Mean'].rolling(window=7).mean().iloc[-1],
d5.iloc[-1,42]-d5['STS_Mean'].rolling(window=7).mean().iloc[-1],
d6.iloc[-1,42]-d6['STS_Mean'].rolling(window=7).mean().iloc[-1],
d7.iloc[-1,42]-d7['STS_Mean'].rolling(window=7).mean().iloc[-1],
d8.iloc[-1,42]-d8['STS_Mean'].rolling(window=7).mean().iloc[-1],
d9.iloc[-1,42]-d9['STS_Mean'].rolling(window=7).mean().iloc[-1],
d10.iloc[-1,42]-d10['STS_Mean'].rolling(window=7).mean().iloc[-1],
d11.iloc[-1,42]-d11['STS_Mean'].rolling(window=7).mean().iloc[-1],
d12.iloc[-1,42]-d12['STS_Mean'].rolling(window=7).mean().iloc[-1]],columns=['Momentum 7-Day'])

mom30= pd.DataFrame([d1.iloc[-1,42]-d1['STS_Mean'].rolling(window=30).mean().iloc[-1],
d2.iloc[-1,42]-d2['STS_Mean'].rolling(window=30).mean().iloc[-1],
d3.iloc[-1,42]-d3['STS_Mean'].rolling(window=30).mean().iloc[-1],
d4.iloc[-1,42]-d4['STS_Mean'].rolling(window=30).mean().iloc[-1],
d5.iloc[-1,42]-d5['STS_Mean'].rolling(window=30).mean().iloc[-1],
d6.iloc[-1,42]-d6['STS_Mean'].rolling(window=30).mean().iloc[-1],
d7.iloc[-1,42]-d7['STS_Mean'].rolling(window=30).mean().iloc[-1],
d8.iloc[-1,42]-d8['STS_Mean'].rolling(window=30).mean().iloc[-1],
d9.iloc[-1,42]-d9['STS_Mean'].rolling(window=30).mean().iloc[-1],
d10.iloc[-1,42]-d10['STS_Mean'].rolling(window=30).mean().iloc[-1],
d11.iloc[-1,42]-d11['STS_Mean'].rolling(window=30).mean().iloc[-1],
d12.iloc[-1,42]-d12['STS_Mean'].rolling(window=30).mean().iloc[-1]],columns=['Momentum 30-Day'])

d1x=pd.DataFrame(d1.iloc[-1]).T
d22=pd.DataFrame(d2.iloc[-1]).T
d33=pd.DataFrame(d3.iloc[-1]).T
d44=pd.DataFrame(d4.iloc[-1]).T
d55=pd.DataFrame(d5.iloc[-1]).T
d66=pd.DataFrame(d6.iloc[-1]).T
d77=pd.DataFrame(d7.iloc[-1]).T
d88=pd.DataFrame(d8.iloc[-1]).T
d99=pd.DataFrame(d9.iloc[-1]).T
d100=pd.DataFrame(d10.iloc[-1]).T
d111=pd.DataFrame(d11.iloc[-1]).T
d122=pd.DataFrame(d12.iloc[-1]).T

dd = pd.concat([d1x,d22,d33,d44,d55,d66,d77,d88,d99,d100,d111,d122])
dd=dd.reset_index()
dd=dd.iloc[:,[3,42,60]]
dd=pd.concat([dd,mom7,mom30],axis=1)
dd

dddd=dd.reset_index()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Row([
        dbc.Col([html.P('Select Stock:', style={'textDecoration': 'underline'}),
            dcc.Dropdown(id='rad', multi=False, value='IBS',
                            options=[{'label': x, 'value': x}
                                    for x in sorted (stts['Ticker'].unique())],style={"width": "50%",'color':'black'}),
            dcc.Graph(id='table1',figure={},style={'color':'black','background-color': 'black','width': '70vh', 'height': '40vh'})
        ], width={'size': 10}),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        html.P(
                            "SDG DASHBOARD",
                            className="card-text")
                    ),
                    dbc.CardImg(
                        src='https://www.dropbox.com/s/ahypx9xi90yi4fh/glo.jpg?dl=1',
                        bottom=True),
                ],
                style={"width": "18rem"},
            )
        ], width={'size':2, 'offset':0},
           xs=5, sm=5, md=5, lg=2, xl=2
        )
    ], align="right"),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='data',figure={},style={'color':'black','background-color': 'black', 'height': '40vh'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph2', figure={})
        ], width={'size': 4}),
            dbc.Col([
            dcc.Graph(id='graph3', figure={},style={'color':'black','background-color': 'black'})
        ], width={'size': 4}),
            dbc.Col([
            dcc.Graph(id='graph4', figure={})
        ], width={'size': 4}),
    ]),
    dbc.Row([
        dbc.Col(html.H1("SDG",
                        className='text-center text-primary, mb-3'),
                width=16)
    ]),
    dbc.Row([
        dbc.Col([
            html.P('Select Stock:', style={'textDecoration': 'underline'}),
            dcc.Graph(id='fig1', figure={})
        ], width={'size': 20}),
    ]),
    dbc.Row([
        dbc.Col(html.H1("ESG",
                        className='text-center text-primary, mb-3'),
                width=16)
    ]),
    dbc.Row([
        dbc.Col([
            html.P('Select Date:', style={'textDecoration': 'underline'}),
            dcc.Graph(id='fig2', figure={})
        ], width={'size': 20}),
    ]),
    dbc.Row([
        dbc.Col(html.H1("Sentiment",
                        className='text-center text-primary, mb-3'),
                width=16)
    ]),
    dbc.Row([
        dbc.Col([
            html.P('Select Date:', style={'textDecoration': 'underline'}),
            dcc.Graph(id='fig3', figure={})
        ], width={'size': 20}),

        ])
    ])


@app.callback(
    Output('data', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    ddd = dd[dd['Ticker']==(com)]
    fighist = go.Figure(go.Table(header={"values": ddd.columns}, cells={"values": ddd.T.values}))
    fighist.update_layout(template = "plotly_dark")
    return fighist


@app.callback(
    Output('table1', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    stt = st[st['Ticker']==(com)]
    fighist = go.Figure(go.Table(header={"values": stt.columns}, cells={"values": stt.T.values}))
    fighist.update_layout(template = "plotly_dark")
    return fighist


@app.callback(
    Output('graph2', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    sttss = stts[stts['Ticker']==(com)]
    fighist = px.line_polar(sttss, r ='Number',theta='STS',line_close=True, template ="plotly_dark")
    return fighist

@app.callback(
    Output('graph3', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    ddd1 = dddd[dddd['Ticker']==(com)]
    speeed=dddd['STS_Mean']
    for i in range(len(speeed)):
        if dddd.iloc[i,1]== com:
            speeedd = speeed[i]
    fighist = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = speeedd,
    mode = "gauge+number+delta",
    title = {'text': "STS SDG Score"},
    gauge = {'axis': {'range': [-3, 3]},
             'steps' : [
                 {'range': [-3, speeedd], 'color': "red"},
                 {'range': [speeedd, 3], 'color': "blue"}],
             }))
    fighist.update_layout(template = "plotly_dark")
    return fighist




@app.callback(
    Output('graph4', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    sttss = stts[stts['Ticker']==(com)]
    fighist = px.bar(sttss, x='STS', y='Number')
    fighist.update_layout(template = "plotly_dark")
    return fighist


@app.callback(
    Output('fig1', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    dff = sdg[sdg['Ticker']==(com)]
    fighist = px.line(dff, x = 'Timestamp',y = 'SDG_Mean',color = 'Ticker',template ='plotly_dark')
    return fighist

@app.callback(
    Output('fig2', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    dff = esg[esg['Ticker']==(com)]
    fighist = px.line(dff, x = 'Timestamp',y = 'ESG_Mean',color = 'Ticker',template ="plotly_dark")
    return fighist


@app.callback(
    Output('fig3', 'figure'),
    Input('rad', 'value')
)
def update_graph(com):
    dff = sent[sent['Ticker']==(com)]
    fighist = px.line(dff, x = 'Timestamp',y = 'Sentiment',color = 'Ticker',template ="plotly_dark")
    return fighist



if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
