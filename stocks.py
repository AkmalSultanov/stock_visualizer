#STOCK VISUALIZER APP
import tkinter as tk
import yfinance as yf
from matplotlib import pyplot as plt

window = tk.Tk()
window.title("Stock Visualizer")
window.geometry("600x400")

stock_Label = tk.Label(window, text = "Enter a stock ticker")
stock_Label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
stock_input = tk.Entry(window)
stock_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
def button_click():
    stock_symbol = stock_input.get() 
    stock = yf.Ticker(stock_symbol.upper())
    stock_historical = stock.history("1mo")
    # print(f"Stock info for symbol '{stock_symbol.upper()}'")
    # print(stock_historical)
    x = stock_historical.index  # dates
    y = stock_historical["Close"]  # closing prices
    plt.plot(x,y,label=f"Trendline for {stock_symbol.upper()}")
    plt.title(f"Dates vs Closing Prices for {stock_symbol.upper()}")
    plt.xlabel("Dates for a period of 1 month")
    plt.ylabel("Closing Prices")
    plt.legend()
    plt.show()


stock_button = tk.Button(window, text="Visualize Stock", command=button_click)
stock_button.grid(row=0, column=2, padx=10, pady=10)


window.mainloop()