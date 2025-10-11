# NVDA-Stock-Analysis  

Stock Data Processing and Analysis of **NVIDIA (NVDA)** from June 2024 to June 2025.  
This project is the final assignment for the Data Processing Programming (DPP) course at University of Engineering and Technology (UET), VNU.

## Overview

This repository demonstrates how to collect, clean, and analyze historical stock price data using Python.  
The analysis includes:  
- Retrieving data from Yahoo Finance with `yfinance`  
- Cleaning and preprocessing time-series data  
- Computing key technical indicators: SMA, EMA, RSI, MACD  
- Visualizing stock price trends and indicators  
- Evaluating performance metrics such as return, volatility, and max drawdown  

⚠️ Note: This project is for educational purposes only and does not provide financial advice.

## Features

- Fetch NVDA stock data covering June 2024 – June 2025  
- Data cleaning and preprocessing (handle missing values, align timestamps, etc.)  
- Calculate technical indicators:  
  - Simple Moving Average (SMA)  
  - Exponential Moving Average (EMA)  
  - Relative Strength Index (RSI)  
  - Moving Average Convergence Divergence (MACD)  
- Compute performance metrics: returns, volatility, maximum drawdown  
- Plot and visualize time-series, indicators, and comparative charts  
- Include source code, Jupyter notebooks, and datasets  

## Project Structure

NVDA-Stock-Analysis/
├── assets/ # Static files (images, plots, etc.)
├── app.py # Optional frontend / dashboard app
├── nvda_data_download.ipynb # Notebook: data retrieval
├── nvda_data_cleaning.ipynb # Notebook: data cleaning & preprocessing
├── nvda_data_analysis.ipynb # Notebook: analysis & visualization
├── nvda_stock_data.csv # Raw historical data
├── nvda_stock_data_cleaned.csv # Cleaned/preprocessed data
├── README.md # This file
└── LICENSE # License file (if any)

## Environment Requirements

You’ll need Python and these libraries (among others):

- pandas  
- numpy  
- matplotlib / seaborn  
- plotly  
- requests  
- yfinance  
- (Optional) flask or fastapi  

You can install dependencies via:

```bash
pip install pandas numpy matplotlib seaborn plotly requests yfinance
```
Or if you have a requirements.txt:
```bash
pip install -r requirements.txt
```

## How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/dlxik/NVDA-Stock-Analysis.git
cd NVDA-Stock-Analysis
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Jupyter notebooks in order
- `nvda_data_download.ipynb` → fetch data  
- `nvda_data_cleaning.ipynb` → clean & preprocess data  
- `nvda_data_analysis.ipynb` → analyze & visualize

### 5. (Optional) Run the web app
```bash
python app.py
```

## Future Improvements
- Support multiple stock tickers (not only NVDA)  
- Add predictive models such as ARIMA, LSTM, or Prophet  
- Build an interactive dashboard using Dash or Streamlit  
- Automate daily/weekly data updates  
- Deploy the project on cloud platforms (Heroku, AWS, or GCP)

## Contributing

Contributions are always welcome!  
You can:
- Open issues to report bugs or suggest new features  
- Submit pull requests with improvements  
- Help refine documentation and visualizations  

Please follow standard GitHub contribution practices.

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute the code with proper credit.

