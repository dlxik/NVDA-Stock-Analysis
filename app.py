import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# Load dữ liệu
df_raw = pd.read_csv("nvda_stock_data.csv")

df_raw['Date'] = pd.to_datetime(df_raw['Date'], utc=True)
df_raw.set_index('Date', inplace=True)

fig_raw_candlestick = go.Figure(data=[go.Candlestick(
    x=df_raw.index,
    open=df_raw['Open'],
    high=df_raw['High'],
    low=df_raw['Low'],
    close=df_raw['Close'],
    name='Candlestick'
)])
fig_raw_candlestick.update_layout(
    title='Candlestick Chart for NVDA (1 Year)',
    title_font=dict(
        color='white',
        size=24, 
        family="Arial, sans-serif", 
        weight='bold'  
    ),
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False,
    plot_bgcolor='black', 
    paper_bgcolor='black',
    font=dict(color="white"),
    xaxis=dict(
        gridcolor='white', 
        color='white',   
        ticks="outside",   
        ticklen=6, 
        tickwidth=1,
    ),
    yaxis=dict(
        gridcolor='white',
        color='white',
        ticks="outside", 
        ticklen=6, 
        tickwidth=2, 
    ),
    shapes=[
        dict(
            type='line',
            x0=df_raw.index[0],
            x1=df_raw.index[-1],
            y0=df_raw['Low'].min(),
            y1=df_raw['Low'].min(),
            line=dict(color='white', width=1)
        ),
        dict(
            type='line',
            x0=df_raw.index[0],
            x1=df_raw.index[-1],
            y0=df_raw['High'].max(),
            y1=df_raw['High'].max(),
            line=dict(color='white', width=1)
        ),
    ]
)

fig_raw_price_distribution = px.histogram(df_raw, x='Close', nbins=50, title="Price Distribution Chart for NVDA (1 Year)", labels={"Close": "Price (USD)"})
fig_raw_price_distribution.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white', 
    title_font=dict(
        color='white', 
        size=24, 
        family="Arial, sans-serif",  
        weight='bold'  
    ),
    xaxis_title="Price (USD)",
    yaxis_title="Frequency",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

fig_raw_price_volume = go.Figure()
fig_raw_price_volume.add_trace(go.Bar(
    x=df_raw.index, 
    y=df_raw['Volume'], 
    name='Volume',
    marker=dict(color='mediumpurple'),
    yaxis='y' 
))
fig_raw_price_volume.add_trace(go.Scatter(
    x=df_raw.index, 
    y=df_raw['Close'], 
    mode='lines', 
    name='Price (USD)',
    line=dict(color='deepskyblue'), 
    yaxis='y2'
))
fig_raw_price_volume.update_layout(
    title="Price and Volume Chart for NVDA (1 Year)",
    xaxis_title="Date",  # Đảm bảo trục x là 'Date'
    title_font=dict(
        color='white',
        size=24, 
        family="Arial, sans-serif",
        weight='bold'
    ),
    yaxis=dict(  # Trục Volume
        title="Volume (Shares)",
        showgrid=False,
        side="left"
    ),
    yaxis2=dict(  # Trục Price
        title="Price (USD)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(  # Chỉ khai báo legend 1 lần
        x=0.9, 
        y=1.25,
        xanchor='left',
        yanchor='top',  
        bgcolor='rgba(0, 0, 0, 0)',  
        font=dict(color='white')  
    ),
    bargap=0.1,
    template="plotly_dark",
    xaxis=dict(
        title="Date",  # Đảm bảo tiêu đề trục x là 'Date'
        showgrid=True,
        gridcolor='rgba(255,255,255,0.2)'  
    )
)

df_cleaned = pd.read_csv("nvda_stock_data_cleaned.csv")
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], utc=True)
df_cleaned.set_index('Date', inplace=True)
df_cleaned_head = df_cleaned.head(1000)

fig_cleaned_candlestick = go.Figure(data=[go.Candlestick(
    x=df_cleaned.index,
    open=df_cleaned['Open'],
    high=df_cleaned['High'],
    low=df_cleaned['Low'],
    close=df_cleaned['Close'],
    name='Candlestick'
)])
fig_cleaned_candlestick.update_layout(
    title='Candlestick Chart for NVDA (1 Year)',
    title_font=dict(
        color='white',
        size=24, 
        family="Arial, sans-serif", 
        weight='bold'  
    ),
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False,
    plot_bgcolor='black', 
    paper_bgcolor='black',
    font=dict(color="white"),
    xaxis=dict(
        gridcolor='white', 
        color='white',   
        ticks="outside",   
        ticklen=6, 
        tickwidth=1,
    ),
    yaxis=dict(
        gridcolor='white',
        color='white',
        ticks="outside", 
        ticklen=6, 
        tickwidth=2, 
    ),
    shapes=[
        dict(
            type='line',
            x0=df_cleaned.index[0],
            x1=df_cleaned.index[-1],
            y0=df_cleaned['Low'].min(),
            y1=df_cleaned['Low'].min(),
            line=dict(color='white', width=1)
        ),
        dict(
            type='line',
            x0=df_cleaned.index[0],
            x1=df_cleaned.index[-1],
            y0=df_cleaned['High'].max(),
            y1=df_cleaned['High'].max(),
            line=dict(color='white', width=1)
        ),
    ]
)

fig_cleaned_price_distribution = px.histogram(df_cleaned, x='Close', nbins=50, title="Price Distribution Chart for NVDA (1 Year)", labels={"Close": "Price (USD)"})
fig_cleaned_price_distribution.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white', 
    title_font=dict(
        color='white', 
        size=24, 
        family="Arial, sans-serif",  
        weight='bold'  
    ),
    xaxis_title="Price (USD)",
    yaxis_title="Frequency",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

fig_cleaned_price_volume = go.Figure()
fig_cleaned_price_volume.add_trace(go.Bar(
    x=df_cleaned.index, 
    y=df_cleaned['Volume'], 
    name='Volume',
    marker=dict(color='mediumpurple'),
    yaxis='y' 
))
fig_cleaned_price_volume.add_trace(go.Scatter(
    x=df_cleaned.index, 
    y=df_cleaned['Close'], 
    mode='lines', 
    name='Price (USD)',
    line=dict(color='deepskyblue'), 
    yaxis='y2'
))
fig_cleaned_price_volume.update_layout(
    title="Price and Volume Chart for NVDA (1 Year)",
    xaxis_title="Date",  # Đảm bảo trục x là 'Date'
    title_font=dict(
        color='white',
        size=24, 
        family="Arial, sans-serif",
        weight='bold'
    ),
    yaxis=dict(  # Trục Volume
        title="Volume (Shares)",
        showgrid=False,
        side="left"
    ),
    yaxis2=dict(  # Trục Price
        title="Price (USD)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(  # Chỉ khai báo legend 1 lần
        x=0.9, 
        y=1.25,
        xanchor='left',
        yanchor='top',  
        bgcolor='rgba(0, 0, 0, 0)',  
        font=dict(color='white')  
    ),
    bargap=0.1,
    template="plotly_dark",
    xaxis=dict(
        title="Date",  # Đảm bảo tiêu đề trục x là 'Date'
        showgrid=True,
        gridcolor='rgba(255,255,255,0.2)'  
    )
)

# 1. Tính SMA, EMA
# Tính SMA (Simple Moving Average) với khoảng 20 ngày và 50 ngày
df_cleaned['SMA20'] = df_cleaned['Close'].rolling(window=20).mean()
df_cleaned['SMA50'] = df_cleaned['Close'].rolling(window=50).mean()

# Tính EMA (Exponential Moving Average) với khoảng 20 ngày
df_cleaned['EMA20'] = df_cleaned['Close'].ewm(span=20, adjust=False).mean()    
fig_SMA_EMA = go.Figure()
fig_SMA_EMA.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Close'], mode='lines', name='NVDA Close Price', line=dict(color='blue', width=2.75)))
fig_SMA_EMA.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['SMA20'], mode='lines', name='SMA 20', line=dict(color='orange')))
fig_SMA_EMA.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['SMA50'], mode='lines', name='SMA 50', line=dict(color='green')))
fig_SMA_EMA.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['EMA20'], mode='lines', name='EMA 20', line=dict(color='red')))
fig_SMA_EMA.update_layout(
    title="NVDA Stock Price with SMA and EMA",
    title_font=dict(
        color='white',  
        size=24,
        family="Arial, sans-serif", 
        weight='bold'
    ),
    xaxis_title="Date",
    yaxis_title="Price",
    hovermode="x unified",
    template="plotly_dark",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

# 2. Tính RSI (Relative Strength Index)
delta = df_cleaned['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
rsi = 100 - (100 / (1 + rs))
df_cleaned['RSI'] = rsi
fig_RSI = go.Figure()
# Vẽ RSI
fig_RSI.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['RSI'], mode='lines', name='RSI', line=dict(color='purple', width=2.5)))
# Vẽ đường Overbought (70) và Oversold (30)
fig_RSI.add_trace(go.Scatter(x=df_cleaned.index, y=[70]*len(df_cleaned), mode='lines', name='Overbought (70)', line=dict(color='red', dash='dash')))
fig_RSI.add_trace(go.Scatter(x=df_cleaned.index, y=[30]*len(df_cleaned), mode='lines', name='Oversold (30)', line=dict(color='green', dash='dash')))
fig_RSI.update_layout(
    title="RSI of NVDA with Overbought and Oversold Levels",
    title_font=dict(
        color='white',
        size=24,
        family="Arial, sans-serif",
        weight='bold'
    ),
    xaxis_title="Date",
    yaxis_title="RSI Value",
    template="plotly_dark",
    hovermode="x unified",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

# 3. Tính lợi suất hàng ngày
df_cleaned['Return'] = df_cleaned['Close'].pct_change()
fig_returns = go.Figure()

fig_returns.add_trace(go.Histogram(
    x=df_cleaned['Return'].dropna(),
    nbinsx=50,
    name="Daily Returns",
    marker_color='blue',
    opacity=0.75
))
fig_returns.add_annotation(
    x=df_cleaned['Return'].mean(),  
    y=10,  
    text="Mean Return",  
    showarrow=True, 
    arrowhead=2,
    ax=0,
    ay=-50,
    font=dict(size=12, color="white"),
    bgcolor="black", 
)

fig_returns.update_layout(
    title="Distribution of NVDA Daily Returns",
    title_font=dict(
        color='white', 
        size=24,
        family="Arial, sans-serif", 
        weight='bold'
    ),
    xaxis_title="Daily Return",
    yaxis_title="Frequency",
    template="plotly_dark", 
    hovermode="closest",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
)

# 4. Tính độ biến động (Volatility) theo tháng
df_cleaned['Volatility'] = df_cleaned['Return'].rolling(window=30).std()  # rolling 30 ngày
fig_volatility = go.Figure()

# Vẽ biểu đồ độ biến động (Volatility)
fig_volatility.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Volatility'], mode='lines', name='30-day Volatility', line=dict(color='red')))

fig_volatility.update_layout(
    title="Volatility of NVDA Stock Price",
    title_font=dict(
        color='white',
        size=24,
        family="Arial, sans-serif", 
        weight='bold'
    ),
    xaxis_title="Date",
    yaxis_title="Volatility",
    template="plotly_dark",
    hovermode="x unified",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

df_cleaned['SMA20'] = df_cleaned['Close'].rolling(window=20).mean()
df_cleaned['Upper Band'] = df_cleaned['SMA20'] + (df_cleaned['Close'].rolling(window=20).std() * 2)
df_cleaned['Lower Band'] = df_cleaned['SMA20'] - (df_cleaned['Close'].rolling(window=20).std() * 2)
# Tạo figure mới
fig_bollinger = go.Figure()
# Vẽ giá cổ phiếu NVDA
fig_bollinger.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Close'], mode='lines', name='NVDA Close Price', line=dict(color='blue', width=2.5)))
# Vẽ Upper Band và Lower Band
fig_bollinger.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Upper Band'], mode='lines', name='Upper Band', line=dict(color='green', dash='dash')))
fig_bollinger.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Lower Band'], mode='lines', name='Lower Band', line=dict(color='red', dash='dash')))
fig_bollinger.update_layout(
    title="Bollinger Bands of NVDA Stock Price",
    title_font=dict(
        color='white',
        size=24,
        family="Arial, sans-serif",
        weight='bold' 
    ),
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_dark",
    hovermode="x unified",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)') 
)

# 10. Vẽ biểu đồ MACD và Signal Line
# Tính MACD và Signal Line
df_cleaned['EMA12'] = df_cleaned['Close'].ewm(span=12, adjust=False).mean()
df_cleaned['EMA26'] = df_cleaned['Close'].ewm(span=26, adjust=False).mean()
df_cleaned['MACD'] = df_cleaned['EMA12'] - df_cleaned['EMA26']
df_cleaned['Signal Line'] = df_cleaned['MACD'].ewm(span=9, adjust=False).mean()

histogram = df_cleaned['MACD'] - df_cleaned['Signal Line']

# Tạo figure mới
fig_macd = go.Figure()
# Vẽ MACD và Signal Line
fig_macd.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['MACD'], mode='lines', name='MACD', line=dict(color='blue')))
fig_macd.add_trace(go.Scatter(x=df_cleaned.index, y=df_cleaned['Signal Line'], mode='lines', name='Signal Line', line=dict(color='orange')))
fig_macd.add_trace(go.Bar(
    x=df_cleaned.index,
    y=histogram,
    name='MACD Histogram',
    marker_color=np.where(histogram > 0, 'green', 'red'),  # Màu xanh nếu MACD > Signal, ngược lại là đỏ
    opacity=0.3
))
fig_macd.update_layout(
    title="MACD and Signal Line of NVDA",
    title_font=dict(
        color='white',
        size=24,
        family="Arial, sans-serif",
        weight='bold' 
    ),
    xaxis_title="Date",
    yaxis_title="MACD Value",
    template="plotly_dark", 
    hovermode="x unified",
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)'), 
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # Header
# header = dbc.Navbar(
#     dbc.Container([
#         html.Div([
#             html.Small("Student name: Vu Hoang Dieu Linh", className="text-white"),
#             html.Small("Student ID: 24022387", className="text-white")
#         ], className="d-flex flex-column"),

#         html.Div([
#             html.H1(
#                 "NVDA Stock Analysis Dashboard",
#                 className="text-white fw-bold mb-0",
#                 style={"fontSize": "2.8rem", "fontWeight": "bold"}
#             )

#         ], className="d-flex flex-column text-center"),

#         html.Div([
#             # Tiêu đề Github repo
#             html.Div("Github repo", className="text-white fw-bold text-center mb-2"),  # giảm mb từ 3 xuống 2

#         #     # Hàng 1: 3 link ngắn, giảm khoảng cách cột xuống gx-2
#         #     dbc.Row([
#         #         dbc.Col(
#         #             html.Small(
#         #                 html.A("Introduction", href="https://github.com/your-repo/introduction", target="_blank", className="text-white text-end"),
#         #                 className="d-block"
#         #             ),
#         #             width="auto"
#         #         ),
#         #         dbc.Col(
#         #             html.Small(
#         #                 html.A("Data Analysis", href="https://github.com/your-repo/datacleaning", target="_blank", className="text-white text-center"),
#         #                 className="d-block"
#         #             ),
#         #             width="auto"
#         #         ),
#         #         dbc.Col(
#         #             html.Small(
#         #                 html.A("Future works", href="https://github.com/your-repo/futureworks", target="_blank", className="text-white text-start"),
#         #                 className="d-block"
#         #             ),
#         #             width="auto"
#         #         ),
#         #     ], justify="center", className="mb-2 gx-2"),  # mb giảm từ 3 xuống 2, gx giảm từ 4 xuống 2

#         #     # Hàng 2: 2 link dài, giảm khoảng cách cột và hàng
#         #     dbc.Row([
#         #         dbc.Col(
#         #             html.Small(
#         #                 html.A("Data Processing", href="https://github.com/your-repo/datacleaning", target="_blank", className="text-white text-end"),
#         #                 className="d-block"
#         #             ),
#         #             width="auto"
#         #         ),
#         #         dbc.Col(
#         #             html.Small(
#         #                 html.A("Interpretation & Conclusing", href="https://github.com/your-repo/conclusion", target="_blank", className="text-white text-start"),
#         #                 className="d-block"
#         #             ),
#         #             width="auto"
#         #         ),
#         #     ], justify="center", className="gx-2"),  # giảm gx từ 5 xuống 2

#         ], style={"maxWidth": "600px", "margin": "0", "textAlign": "right"})


#     ]),
#     color="black",
#     dark=True,
#     fixed="top",
#     className="py-2"
# )

header = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            # Cột trái: Thông tin sinh viên
            dbc.Col(
                html.Div([
                    html.Small("Student name: Vu Hoang Dieu Linh", className="text-white", style={"fontSize": "1rem"}),
                    html.Small("Student ID: 24022387", className="text-white", style={"fontSize": "1rem"})
                ], className="d-flex flex-column"),
                width="auto"
            ),

            # Cột giữa: Tiêu đề Dashboard, căn giữa tuyệt đối
            dbc.Col(
                html.Div([
                    html.H1(
                        "NVDA Stock Analysis Dashboard",
                        className="text-white fw-bold text-center",
                        style={"fontSize": "3rem", "margin": "0 auto"}
                    )
                ], className="d-flex justify-content-center"),
                width=True  # chiếm phần còn lại để đẩy 2 bên về đúng vị trí
            ),

            # Cột phải: GitHub Repo
            dbc.Col(
                html.Div([
                    html.A(
                        "GitHub repository",
                        href="https://github.com/dlxik/NVDA-Stock-Analysis",
                        target="_blank",
                        className="",
                        style={
                            "color": "#99ff33",  # Xanh ngọc
                            "textDecoration": "none",
                            "fontSize": "1.1rem"
                        }
                    )
                ], className="d-flex flex-column align-items-end"),
                width="auto"
            ),
        ], align="center", justify="between", className="w-100")
    ]),
    color="black",
    dark=True,
    fixed="top",
    className="py-2"
)


logo = html.Div([
    # Logo NVIDIA bên phải
    html.Img(src="/assets/NVIDIA-logo-BL.jpg", style={
        "width": "100px", 
        "height": "auto", 
        "position": "fixed",  # Giữ logo ở vị trí cố định
        "right": "10px",  # Cách từ bên phải một chút
        "top": "10px",  # Cách từ trên xuống một chút
        "zIndex": "5000"  # Đảm bảo logo luôn ở trên navbar
    }),

    # Logo UET bên trái
    html.Img(src="/assets/uet.png", style={
        "width": "40px", 
        "height": "auto", 
        "position": "fixed",  # Giữ logo ở vị trí cố định
        "left": "20px",  # Cách từ bên trái một chút
        "top": "20px",  # Cách từ trên xuống một chút
        "zIndex": "5000"  # Đảm bảo logo luôn ở trên navbar
    }),

    html.Img(src="/assets/iai_cropped.png", style={
        "width": "40px", 
        "height": "auto", 
        "position": "fixed",  # Giữ logo ở vị trí cố định
        "left": "70px",  # Cách từ bên trái một chút
        "top": "20px",  # Cách từ trên xuống một chút
        "zIndex": "5000"  # Đảm bảo logo luôn ở trên navbar
    }),

], className="logo-container")

# Tabs bar – ép full màn hình, dàn đều
tabs_bar = html.Div([
    dcc.Tabs(
        id="tabs",
        value="Introduction",
        children=[
            dcc.Tab(
                label="Introduction", 
                value="Introduction", 
                style={"flex": "1", "textAlign": "center", "backgroundColor": "white", "fontWeight": "normal"},
                selected_style={"backgroundColor": "white", "color": "black", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Data Processing", 
                value="Data Processing", 
                style={"flex": "1", "textAlign": "center", "backgroundColor": "white", "fontWeight": "normal"},
                selected_style={"backgroundColor": "white", "color": "black", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Data Analysis", 
                value="Data Analysis", 
                style={"flex": "1", "textAlign": "center", "backgroundColor": "white", "fontWeight": "normal"},
                selected_style={"backgroundColor": "white", "color": "black", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Interpretation & Conclusing", 
                value="Interpretation & Conclusing", 
                style={"flex": "1", "textAlign": "center", "backgroundColor": "white", "fontWeight": "normal"},
                selected_style={"backgroundColor": "white", "color": "black", "fontWeight": "bold"}
            ),
            dcc.Tab(
                label="Future Works", 
                value="Future Works", 
                style={"flex": "1", "textAlign": "center", "backgroundColor": "white", "fontWeight": "normal"},
                selected_style={"backgroundColor": "white", "color": "black", "fontWeight": "bold"}
            )
        ],
        style={
            "display": "flex",
            "width": "100vw",
            "minHeight": "5px"
        },
        colors={"background": "#f8f9fa", "border": "#d3d3d3", "primary": "blackca"}
    )
], style={
    "position": "fixed",
    "top": "73px",
    "width": "100%", 
    "maxWidth": "1200px",  
    "margin": "0 auto", 
    "zIndex": "2000",
    "backgroundColor": "#f8f9fa",
    "display": "flex",
    "flexWrap": "wrap",
    "padding": "0 10px"
})

# Nội dung từng tab
def tab_content(title, text):
    return html.Div([
        html.H2(title, className="text-center fw-bold"),
        html.P(text, className="text-center")
    ], style={"backgroundColor": "#ffffff", "padding": "30px"})

tab_layouts = {
   "Introduction": html.Div([

        # Khung 1 - Chứa text
        dbc.Card([
            dbc.CardBody([
                html.H4("Acknowledgements", className="text-white"),
                html.P([
                    "In the context of data playing an increasingly important role across various fields, the ability to collect, process, and analyze data has become an essential skill for Information Technology students, especially in areas related to Artificial Intelligence and Data Science. The Data Processing Programming course provides foundational knowledge on working with data through programming, utilizing supporting libraries, and developing analytical thinking to solve real-world problems.",
                    html.Br(),  # Dòng trống
                    "This report presents the process of completing the course project, in which I applied theoretical knowledge to build a specific data processing program. The content includes steps such as reading data, processing, visualization, and result evaluation. Through this project, I had the opportunity to reinforce my skills in working with data and relevant programming tools.",
                    html.Br(),  # Dòng trống
                    html.Br(),  # Dòng trống
                    "I would like to thank the instructors for their guidance and support throughout the semester, which enabled me to complete this project. The report was completed seriously based on my current understanding and capability. It may still contain shortcomings, and I look forward to receiving feedback and evaluation to further improve my knowledge."
                ], className="text-white")
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),

        # Khung 2 - Giới thiệu
        dbc.Card([
            dbc.CardBody([
                # html.H4("Giới thiệu", className="text-white"),
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.H4("Introduction", className="text-white"), 
                                html.P([
                                    "Nowadays, the international stock market plays a vital role in mobilizing capital for the global economy and offers attractive investment opportunities for investors. One of the prominent companies in the U.S. stock market is NVIDIA Corporation (NVDA), a global leader in computer graphics, artificial intelligence, and other advanced technology applications. NVDA stock attracts significant attention from investors not only because of the company's strong growth potential, but also due to NVIDIA’s rapid development and increasing influence across key industries.",
                                    html.Br(),  # Dòng trống
                                    html.Br(),  # Dòng trống
                                    "In this report, I conduct an analysis of the price fluctuations of NVIDIA Corporation's (NVDA) stock over the past year. Analyzing the stock price movements of NVIDIA helps to better understand the company’s financial situation and provides valuable information for investors to make informed investment decisions.",
                                ], className="text-white")
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        html.Div(
                            html.Img(src="/assets/NVIDIA-logo-BL.jpg", style={"width": "90%", "height": "auto"}),
                            style={"flex": "1", "alignSelf": "center", "marginLeft": "60px"}  # Phần logo chiếm nửa màn hình
                        )
                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),

        # Khung 3: mục tiêu
        dbc.Card([
            dbc.CardBody([
                html.H4("The objectives", className="text-white"),
                html.Ul([
                    html.Li("To collect and analyze NVDA stock price data from publicly available financial sources.", id="item1", className="text-white"),
                    html.Li("To calculate basic technical indicators such as SMA (Simple Moving Average), EMA (Exponential Moving Average), and RSI (Relative Strength Index), atc.", id="item2", className="text-white"),
                    html.Li("To visualize the analytical data and draw conclusions from observed trends and stock price patterns.", id="item3", className="text-white"),
                ]),
                html.P([
                    "The use of Python tools and popular libraries such as yfinance, Pandas, and Matplotlib facilitates accurate and efficient data collection, cleaning, and analysis.",
                ], className="text-white")
            ])
        ], style={"backgroundColor": "black", "marginBottom": "20px", "padding": "20px"}),

        # Khung 4: nội dung chính
        dbc.Card([
            dbc.CardBody([
                html.H4("Main contents", className="text-white"),
                html.Ul([
                    html.Li("Introduction: Provides an overview of the topic, objectives, and the approach taken in the report.", id="item1", className="text-white"),
                    html.Li("Data Processing: Describes the process of collecting raw data, handling missing values, and standardizing formats.", id="item2", className="text-white"),
                    html.Li("Data Analysis: Analyzes the data using technical indicators such as SMA, EMA, RSI,... to identify trends.", id="item3", className="text-white"),
                    html.Li("Interpretation & Concluding: Presents insights, interprets analysis results, and provides conclusions.", id="item3", className="text-white"),
                    html.Li("Future Works: Suggests potential improvements and future directions for further studies or applications.", id="item3", className="text-white"),
                ])
            ])
        ], style={"backgroundColor": "black", "marginBottom": "20px", "padding": "20px"}),

    ], style={"padding": "20px"}),

    "Data Processing": html.Div([

        # Khung 1 - thu thập dữ liệu
        dbc.Card([
            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.H4("Data Collection", className="text-white"),
                                html.P([
                                    "The stock data of NVIDIA Corporation (ticker: NVDA) was collected from Yahoo Finance (YF) for the period from June 2024 to June 2025, using the ",
                                    html.Code("yfinance", style={"color": "#d6336c", "fontWeight": "bold"}),
                                    " library in the Python programming language. The collected dataset includes key information such as: Date, Open, Close, High, Low, and Volume.",
                                    html.Br(),
                                    html.Br(),
                                    "The data collection process was carried out in the notebook ", 
                                    html.Code("nvda_data_download.ipynb", style={"color": "#1c7ed6", "fontWeight": "bold"}),
                                    " following the steps below:",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "1. Use ",
                                    html.Code("yf.Ticker()"),
                                    " to retrieve NVDA stock data from Yahoo Finance. The data is obtained using the ",
                                    html.Code("histoty()"),
                                    " method.",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "2. Save the collected data into a CSV file named ",
                                    html.Code("nvda_stock_data.csv", style={"color": "#2f9e44", "fontWeight": "bold"}),
                                    ".",
                                    " An illustration of the CSV file content after data collection is shown alongside. This file is also stored in the GitHub repository for reuse and verification purposes.",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "3. Visualize the data based on the fundamental information using the following charts: candlestick chart, price distribution, and price vs. trading volume."
                                ], className="text-white")
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        html.Div(
                            html.Img(src="/assets/raw_data.png", style={"width": "100%", "height": "auto"}),
                            style={"flex": "1", "alignSelf": "center", "marginLeft": "60px"}  # Phần logo chiếm nửa màn hình
                        )
                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),

        # khung 2: 3 charts
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=fig_raw_candlestick)
                ])
            ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
            
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=fig_raw_price_distribution)
                ])
            ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
        ]),
        dbc.Card([
            dbc.CardBody([
                dcc.Graph(figure=fig_raw_price_volume)
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),

        # khung 3: Làm sạch và tiền xử lý
        dbc.Card([
            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.H4("Data Cleaning and Preprocessing", className="text-white"),
                                html.P([
                                    "1. Check for Missing Values",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "The ",
                                    html.Code("isnull().sum()"),
                                    " function was used to identify the number of missing values in each column of the DataFrame.",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "If missing values were detected, they were replaced using the ",
                                    html.Code("ffill()"),
                                    " method (forward fill using the most recent valid value). ", 
                                    html.Br(),

                                    "2. Outlier Detection and Removal",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "A boxplot was used to visualize the distribution of stock prices (as shown in the figure). Based on the plot, outliers were identified and removed by filtering the data within the range between the ",
                                    html.Code("0.05", style={"color": "#FF00FF"}),
                                    " (lower bound) and ",
                                    html.Code("0.95", style={"color": "#FF00FF"}),
                                    " (upper bound) quantiles of the Close column.",
                                    
                                    html.Br(),
                                    "3. Date Conversion",
                                    html.Br(),
                                    html.Span("\u2003\u2003"),
                                    "The Date column was converted to datetime format for proper time-based analysis.",
                                    html.Br(),
                                    "All of the above steps were performed in the notebook ",
                                    html.Code("nvda_data_cleaning.ipynb", style={"color": "#1c7ed6", "fontWeight": "bold"}),
                                    ", and the cleaned data was saved to the file ",
                                    html.Code("nvda_stock_data_cleaned.csv", style={"color": "#2f9e44", "fontWeight": "bold"}),
                                    ".",
                                ], className="text-white")
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        html.Div(
                            html.Img(src="/assets/boxplot.png", style={"width": "90%", "height": "auto"}),
                            style={"flex": "1", "alignSelf": "center", "marginLeft": "60px"}  # Phần logo chiếm nửa màn hình
                        )
                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),

        html.H1("A Portion of the Cleaned NVDA Stock Data", style={'textAlign': 'center'}),  # Tiêu đề
        html.Table(
            # Tạo bảng từ DataFrame
            # Dùng các cột làm tiêu đề
            # Tạo các dòng dữ liệu từ DataFrame
            [html.Tr([html.Th(col) for col in df_cleaned_head.columns])] +
            [html.Tr([html.Td(df_cleaned_head.iloc[i][col]) for col in df_cleaned_head.columns]) for i in range(len(df_cleaned_head))],
            style={
                'width': '100%',
                'border-collapse': 'collapse',  # Đảm bảo bảng không bị dính vào nhau
                'border': '1px solid black',  # Đường viền của bảng
                'margin': '20px auto',  # Căn giữa bảng
                'padding': '10px',  # Khoảng cách giữa các ô
            },
        ),
            
    ], style={"padding": "20px"}),

    "Data Analysis": html.Div([
        # Dữ liệu sau khi làm sạch
        dbc.Card([
            dbc.CardBody([
                html.H2("The Cleaned NVDA Stock Data", className="text-white"),
                html.P("Data Following Cleaning and Preprocessing.", className="text-white"),
                # dcc.Graph(figure=fig_raw_candlestick)
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(figure=fig_cleaned_candlestick)
                        ])
                    ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
                    
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(figure=fig_cleaned_price_distribution)
                        ])
                    ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
                ]),
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig_cleaned_price_volume)
                    ])
                ], style={"marginBottom": "20px", "backgroundColor": "black"}),
            ])
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),
        

        # tính toán các chỉ số
        dbc.Card([
            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.H4("Technical Indicator Calculation", className="text-white"),
                                html.P([
                                    # html.Span("\u2003\u2003"),
                                    html.Br(),  # Dòng trống
                                    html.Ul([
                                        html.Li([
                                            "SMA (Simple Moving Average): is the arithmetic mean of the closing prices over a specific time period. It is commonly used to identify short-term and long-term market trends. This indicator helps reveal the overall direction of the market by smoothing out price fluctuations over time.",
                                            html.Div([
                                                dcc.Markdown(r'$$SMA_n = \frac{1}{n} \sum_{i=1}^{n} P_i$$', mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '25px'} 
                                            ),
                                            html.Div([
                                                dcc.Markdown(r'$$P_i$$ is the closing price on day i' , mathjax=True),
                                                dcc.Markdown(r'$$n$$ is the number of days used in the average calculation' , mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '15px'} 
                                            ),
                                        ], id="item2", className="text-white"),
                                        html.Li([
                                            "EMA (Exponential Moving Average): is a variation of the Simple Moving Average (SMA), where greater weight is assigned to more recent data points. This allows the EMA to respond more quickly to price changes compared to the SMA.",
                                            html.Div(
                                                dcc.Markdown(r'$$EMA_t = \left( P_t \times \alpha \right) + \left( EMA_{t-1} \times (1 - \alpha) \right)$$', mathjax=True),
                                                style={'text-align': 'center', 'font-size': '25px'}
                                            ),
                                            html.Div([
                                                dcc.Markdown(r'$$P_t$$ is the closing price on day t' , mathjax=True),
                                                dcc.Markdown(r'$$\alpha$$ is the smoothing factor' , mathjax=True),
                                                dcc.Markdown(r'$$EMA_{t-1}$$ is the EMA value of the previous day' , mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '15px'} 
                                            ),
                                        ], id="item2", className="text-white"),

                                        
                                    ]),
                                ], className="text-white"),
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig_SMA_EMA)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            # "position": "relative",  # Đặt vị trí là relative để điều chỉnh
                            "top": "-190px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "40%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "100px"  # Đặt chiều cao
                        }),
                                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ]),

            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.P([
                                    html.Br(),  # Dòng trống
                                    html.Ul([
                                        html.Li([
                                            "RSI (Relative Strength Index): is a technical indicator used to identify overbought or oversold market conditions. RSI values range from 0 to 100 and are commonly interpreted using the thresholds of 70 (overbought) and 30 (oversold).",
                                            html.Div(
                                                dcc.Markdown(r'$$RSI = 100 - \left( \frac{100}{1 + RS} \right)$$', mathjax=True),
                                                style={'text-align': 'center', 'font-size': '25px'}
                                            ),
                                            html.Div([
                                                dcc.Markdown(r'$$RS$$: Relative Strength' , mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '15px'} 
                                            ),
                                        ], id="item2", className="text-white"),

                                        html.Li([
                                            "Daily Return: is the percentage change in a stock's price between two consecutive trading days. It is an important metric for measuring short-term price volatility.",
                                            html.Div(
                                                dcc.Markdown(r'$$\text{Return}_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$', mathjax=True),
                                                style={'text-align': 'center', 'font-size': '25px'}
                                            ),
                                            html.Div([
                                                dcc.Markdown(r'$$P_t$$: the closing price of day t' , mathjax=True),
                                                dcc.Markdown(r'$${P_{t-1}}$$: the closing price of the previous day' , mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '15px'} 
                                            ),
                                        ], id="item2", className="text-white"),

                                        html.Li([
                                            "Volatility: measures the degree of fluctuation in a stock's price over a specific period. Higher volatility indicates greater risk. It is typically calculated as the standard deviation of daily returns.",
                                            html.Div(
                                                dcc.Markdown(r'$$\text{Volatility}_t = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (\text{Return}_i - \text{Mean Return})^2}$$', mathjax=True),
                                                style={'text-align': 'center', 'font-size': '25px'}
                                            ),
                                            html.Div([
                                                dcc.Markdown(r'$$\text{Return}_i$$: the daily return on day i' , mathjax=True),
                                                dcc.Markdown(r'$$\text{Mean Return}$$: the average return over the past n days' , mathjax=True),
                                            ], style={'text-align': 'center', 'font-size': '15px'} 
                                            ),
                                        ], id="item2", className="text-white"),
                                    ]),
                                ], className="text-white"),
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig_RSI)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            # "position": "relative",  # Đặt vị trí là relative để điều chỉnh
                            "top": "-200px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "40%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "100px"  # Đặt chiều cao
                        }),
                                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ]),
        
        ], style={"marginBottom": "20px", "backgroundColor": "black"}),
            
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig_returns)
                    ])
                ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
                
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig_volatility)
                    ])
                ], style={"backgroundColor": "black", "height": "auto", "marginBottom": "20px"}), width=6),
            ]),
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=fig_bollinger)
                ])
            ], style={"marginBottom": "20px", "backgroundColor": "black"}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=fig_macd)
                ])
            ], style={"marginBottom": "20px", "backgroundColor": "black"}),
    
        ], style={"padding": "20px"}),
    
    "Interpretation & Conclusing": html.Div([
        # diễn giải
        dbc.Card([
            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.H4("Interpretation", className="text-white"),
                                html.P([
                                    dbc.Card(
                                        dbc.CardBody([
                                            html.H4("1. SMA and EMA", className="card-title fw-bold"),
                                            
                                            html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li([
                                                    html.Span("October 2024 & May 2025: "),
                                                    html.Span("EMA 20-day (red) crosses above SMA 20-day (orange) and SMA 50-day (green) → trend reversal upward.", className="text-white")
                                                ]),
                                                html.Li([
                                                    html.Span("January – March 2025: "),
                                                    html.Span("EMA drops below SMA → short-term downtrend signal.", className="text-white")
                                                ])
                                            ]),
                                            
                                            html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li("EMA/SMA crossovers effectively predicted price trend reversals."),
                                                html.Li("From May to June 2025, the stock price rose sharply, and both EMA and SMA were trending upward → confirmed bullish trend."),
                                                html.Li([
                                                    html.Span("✅ "),
                                                    html.Span("A strong buy signal appeared in late April 2025.", className="text-success"),
                                                ])
                                            ])
                                        ]),
                                        style={"backgroundColor": "#1e1e1e", "color": "white", "marginBottom": "20px", "borderRadius": "12px", "boxShadow": "0 4px 10px rgba(0,0,0,0.5)"}
                                    )
                                ], className="text-white"),
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig_SMA_EMA)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            # "position": "relative",  # Đặt vị trí là relative để điều chỉnh
                            "top": "-200px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "55%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),
                                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ]),

            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Biểu đồ
                        dbc.Card([ 
                            dbc.CardBody([ 
                                dcc.Graph(figure=fig_RSI)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            "top": "-200px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "70%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),

                        # Phần bên phải: Văn bản
                        html.P([ 
                            html.Br(), 
                            html.Br(),
                            html.Br(), 
                            html.Br(), 
                            dbc.Card(
                                dbc.CardBody([ 
                                    html.H4("2. RSI (Relative Strength Index)", className="card-title fw-bold"), 
                                    html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}), 
                                    html.Ul([ 
                                        html.Li([ 
                                            html.Span("RSI > 70 "), 
                                            html.Span("occurred multiple times — most notably in October 2024, March 2025, and May 2025.", className="text-white") 
                                        ]), 
                                        html.Li([ 
                                            html.Span("RSI < 30 "), 
                                            html.Span("appeared in April 2025, followed by a strong price rebound.", className="text-white") 
                                        ]) 
                                    ]), 
                                    html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}), 
                                    html.Ul([ 
                                        html.Li("The current RSI is around 65–70, approaching the overbought zone."), 
                                        html.Li("The uptrend continues, but signs of weakening should be closely monitored."), 
                                        html.Li([ 
                                            html.Span("⚠️ "), 
                                            html.Span("Strong upward momentum, but nearing the risk zone for a potential correction.", className="text-warning") 
                                        ]) 
                                    ]) 
                                ]), 
                                style={ 
                                    "backgroundColor": "#1e1e1e", 
                                    "color": "white", 
                                    "marginBottom": "20px", 
                                    "borderRadius": "12px", 
                                    "boxShadow": "0 4px 10px rgba(0,0,0,0.5)" 
                                } 
                            ) 
                        ], className="text-white"),
                    ],
                    style={
                        "display": "flex", 
                        "justifyContent": "space-between",  # Đảm bảo phần tử bên trái và bên phải cách nhau đều
                        "alignItems": "center", 
                        "width": "100%"  # Bố trí Flexbox
                    }
                )
            ]),
        
            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.P([
                                    html.Br(), 
                                    html.Br(), 
                                    dbc.Card(
                                        dbc.CardBody([
                                            html.H4("3. Daily Return Distribution", className="card-title fw-bold"),

                                            html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li("The histogram follows a normal distribution, with a slight left skew."),
                                                html.Li("There are several days with extreme fluctuations of up to ±15%.")
                                            ]),

                                            html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li("The average daily return is close to zero, indicating strong volatility in the medium term, with no clear bullish or bearish bias across the whole period."),
                                                html.Li([
                                                    html.Span("⚠️ "),
                                                    html.Span("Attention should be paid to the instability during some highly volatile trading sessions.", className="text-warning")
                                                ])
                                            ])
                                        ]),
                                        style={"backgroundColor": "#1e1e1e", "color": "white", "marginBottom": "20px", "borderRadius": "12px", "boxShadow": "0 4px 10px rgba(0,0,0,0.5)"}
                                    )
                                ], className="text-white"),
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig_returns)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            # "position": "relative",  # Đặt vị trí là relative để điều chỉnh
                            "top": "-190px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "60%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),
                                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ]),

            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Biểu đồ
                        dbc.Card([ 
                            dbc.CardBody([ 
                                dcc.Graph(figure=fig_volatility)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            "top": "-200px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "70%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),

                        # Phần bên phải: Văn bản
                        html.P([ 
                            html.Br(), 
                            html.Br(),
                            html.Br(), 
                            html.Br(), 
                            dbc.Card(
                                dbc.CardBody([ 
                                    html.H4("4. Volatility", className="card-title fw-bold"),

                                    html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}),
                                    html.Ul([
                                        html.Li("Low volatility (~0.02) at the beginning of 2025, followed by a sharp spike in March, then gradually declined through June 2025.")
                                    ]),

                                    html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}),
                                    html.Ul([
                                        html.Li("High volatility occurred before and during the price surge → consistent with the principle \"volatility precedes breakout.\""),
                                        html.Li("In the current phase: Volatility is decreasing, suggesting the price may be entering a stabilization zone."),
                                        html.Li([
                                            html.Span("✅ "),
                                            html.Span("A suitable period for holding if the price continues to rise steadily.", className="text-success")
                                        ])
                                    ])
                                ]), 
                                style={ 
                                    "backgroundColor": "#1e1e1e", 
                                    "color": "white", 
                                    "marginBottom": "20px", 
                                    "borderRadius": "12px", 
                                    "boxShadow": "0 4px 10px rgba(0,0,0,0.5)" 
                                } 
                            ) 
                        ], className="text-white"),
                    ],
                    style={
                        "display": "flex", 
                        "justifyContent": "space-between",  # Đảm bảo phần tử bên trái và bên phải cách nhau đều
                        "alignItems": "center", 
                        "width": "100%"  # Bố trí Flexbox
                    }
                )
            ]),

            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Văn bản
                        html.Div(
                            children=[
                                html.P([
                                    html.Br(), 
                                    html.Br(), 
                                    dbc.Card(
                                        dbc.CardBody([
                                            html.H4("5. Bollinger Bands", className="card-title fw-bold"),

                                            html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li("The price broke above the upper band in May 2025, indicating a clear breakout."),
                                                html.Li("Prior to that, the price hovered near the lower band, forming a solid base.")
                                            ]),

                                            html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}),
                                            html.Ul([
                                                html.Li("The price is currently staying close to the upper band, suggesting that buying pressure remains strong."),
                                                html.Li("No significant signs of weakening have been observed."),
                                                html.Li([
                                                    html.Span("✅ "),
                                                    html.Span("A breakout has occurred, and the uptrend is being sustained.", className="text-success")
                                                ])
                                            ])
                                        ]),
                                        style={"backgroundColor": "#1e1e1e", "color": "white", "marginBottom": "20px", "borderRadius": "12px", "boxShadow": "0 4px 10px rgba(0,0,0,0.5)"}
                                    )
                                ], className="text-white"),
                            ],
                            style={"flex": "2", "textAlign": "left"}  # Phần văn bản chiếm nửa màn hình
                        ),
                        # Phần bên phải: Logo
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig_bollinger)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            # "position": "relative",  # Đặt vị trí là relative để điều chỉnh
                            "top": "-190px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "60%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),
                                    ],
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "width": "100%"}  # Bố trí Flexbox
                ),
            ]),

            dbc.CardBody([
                html.Div(
                    children=[
                        # Phần bên trái: Biểu đồ
                        dbc.Card([ 
                            dbc.CardBody([ 
                                dcc.Graph(figure=fig_macd)
                            ])
                        ], style={
                            "marginBottom": "20px",
                            "backgroundColor": "black",
                            "top": "-190px",  # Dịch xuống 50px
                            "left": "0px",  # Dịch sang trái 30px
                            "width": "70%",  # Đặt chiều rộng phần tử là 70% của vùng chứa
                            "height": "20px"  # Đặt chiều cao
                        }),

                        # Phần bên phải: Văn bản
                        html.P([ 
                            html.Br(), 
                            html.Br(),
                            html.Br(), 
                            html.Br(), 
                            dbc.Card(
                                dbc.CardBody([ 
                                    html.H4("6. MACD (Moving Average Convergence Divergence)", className="card-title fw-bold"),

                                    html.H5("Observations:", className="fw-bold", style={"marginTop": "20px"}),
                                    html.Ul([
                                        html.Li("MACD crossed above the Signal Line in late April 2025 and has maintained a positive gap since."),
                                        html.Li("The histogram has increased sharply and remained above zero.")
                                    ]),

                                    html.H5("Remarks:", className="fw-bold", style={"marginTop": "20px"}),
                                    html.Ul([
                                        html.Li("This is a strong buy signal, especially with confirmation from other indicators."),
                                        html.Li([
                                            html.Span("✅ "),
                                            html.Span("The uptrend is clearly confirmed by the MACD.", className="text-success")
                                        ])
                                    ])
                                ]), 
                                style={ 
                                    "backgroundColor": "#1e1e1e", 
                                    "color": "white", 
                                    "marginBottom": "20px", 
                                    "borderRadius": "12px", 
                                    "boxShadow": "0 4px 10px rgba(0,0,0,0.5)" 
                                } 
                            ) 
                        ], className="text-white"),
                        html.Br(),
                    ],
                    style={
                        "display": "flex", 
                        "justifyContent": "space-between",  # Đảm bảo phần tử bên trái và bên phải cách nhau đều
                        "alignItems": "center", 
                        "width": "100%"  # Bố trí Flexbox
                    }
                )
            ]),

        ], style={"marginBottom": "20px", "backgroundColor": "black"}),
        
        dbc.Card(
            dbc.CardBody([
                html.H4("Conclusing", className="card-title fw-bold"),

                html.H5("Main Trend:", className="fw-bold", style={"marginTop": "20px"}),
                html.P("A strong bullish trend has been observed since April 2025.", className="text-white"),
                
                html.H5("Investment Recommendation", className="fw-bold", style={"marginTop": "20px"}),
                html.Ul([
                    html.Li("Existing investors are advised to continue holding their positions. Partial profit-taking may be considered if RSI exceeds the 75 threshold."),
                    html.Li("New investors may consider opening a buy position if the stock experiences a slight pullback and RSI returns to a safer level (around 55–60)."),
                    html.Li("A stop-loss should be placed below the nearest support level (based on the 50-day SMA) to protect capital in case of an unexpected reversal."),
                
                ]),
                html.H5("Overall:", className="fw-bold", style={"marginTop": "20px"}),
                html.P("NVDA appears to be entering a strong bullish trend, confirmed by multiple key technical indicators such as SMA, EMA, RSI, and Bollinger Bands. However, beyond technical factors, investors should also consider the broader economic and geopolitical environment, including the U.S. Federal Reserve’s interest rate policies, U.S.–China trade tensions, as well as the global AI development trend and U.S. government tech subsidies. These factors may significantly impact NVDA's growth prospects."),
                html.P("Therefore, it is recommended that investors combine technical analysis with close monitoring of macroeconomic conditions to develop a proactive and effective investment strategy in the short to medium term."),
                
            ]),
            style={
                "backgroundColor": "black",
                "color": "white",
                "marginBottom": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.5)"
            }
        )
    
        ], style={"padding": "20px"}),

    "Future Works": html.Div([

        dbc.Card(
            dbc.CardBody([
                html.H4("Future Works", className="card-title fw-bold"),

                html.P(
                    "Although this report has provided a comprehensive technical analysis of NVDA stock over a one-year period, there are several potential directions for future research and application to enhance the quality and depth of analysis:",
                    className="text-white", style={"marginTop": "20px"}
                ),

                html.Ul([
                    html.Li("Incorporating advanced technical indicators such as the Ichimoku Cloud, ADX, and Stochastic Oscillator to gain a more detailed view of trend direction and market strength."),
                    html.Li("Combining technical and fundamental analysis, by integrating factors such as earnings reports, industry benchmarks, and monetary policy to form a more holistic investment perspective."),
                    html.Li("Applying machine learning models like Random Forest, XGBoost, or LSTM neural networks to improve stock price trend prediction in volatile market conditions."),
                    html.Li("Developing an automated analysis dashboard using platforms like Dash or Streamlit for better data visualization and enhanced user interaction."),
                    html.Li("Building risk management models and portfolio optimization tools to recommend personalized asset allocation strategies based on individual investor risk profiles.")
                ]),

                html.P(
                    "These directions not only help improve the robustness of the analytical system but also pave the way for building more practical and insightful decision-support tools in an increasingly dynamic market environment.",
                    className="text-white", style={"marginTop": "20px"}
                )
            ]),
            style={
                "backgroundColor": "black",
                "color": "white",
                "marginBottom": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.5)"
            }
        )

    ], style={"padding": "20px"}),
}

# Nội dung
tab_contents = html.Div(
    id="tab-content",
    style={
        "paddingTop": "150px",  # chỉnh cao hơn (hoặc 140px nếu cần)
        "backgroundColor": "#ffffff"
    }
)


# App layout
app.layout = html.Div([
    header,
    logo,
    tabs_bar,
    tab_contents
])

# Callback
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value")
)
def render_content(tab):
    return tab_layouts.get(tab, html.P("Tab không tồn tại.", className="text-center"))

if __name__ == "__main__":
    app.run(debug=True)
