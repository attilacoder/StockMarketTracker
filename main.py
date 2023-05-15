import requests
import pandas as pd
import dearpygui.dearpygui as dpg



def window_close(sender, data):
    dpg.stop_dearpygui()
def fetch_data(sender,data):
    ticker = dpg.get_value(inputs["ticker"])
    print(ticker)
    stock_data = get_stock_data(ticker)
    dpg.set_value(text,value=stock_data)
    # dpg.add_line_series(plots["graph"], "price", list(range(len(stock_data))), stock_data)
def get_stock_data(ticker):
    api_key = "0GB21CPIA67X72N8"

    request = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}'

    response = requests.get(request)

    data = response.json()
    df = pd.DataFrame(data['Time Series (Daily)']).T
    
    return df

inputs = {}
plots = {}
dpg.create_context()
dpg.create_viewport(title="Stock Data")
dpg.setup_dearpygui()
dpg.maximize_viewport()

with dpg.window(label="Stock Data",height=3000,width=3000):
    dpg.add_text("Enter a stock ticker:")
    inputs["ticker"] = dpg.add_input_text(label="Stock Symbol", default_value="AAPL")
    dpg.add_button(label="Graph",callback=fetch_data)
    dpg.add_button(label="Close", callback=window_close)
    text = dpg.add_text(label="data")
    plots["graph"] = dpg.add_plot(label="graph")


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()