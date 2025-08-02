# STOCK VISUALIZER
import tkinter as tk
from tkinter import ttk
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

window = tk.Tk()
window.title("Stock Visualizer")
window.geometry("800x700")

style = ttk.Style(window)
style.configure('TLabel', font=('Arial', 12), background='#f0f0f0')
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=8)

stock_Label = ttk.Label(window, text="Enter a stock ticker")
stock_Label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

stock_input = ttk.Entry(window)
stock_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Create the figure and axes once
fig = Figure(figsize=(12, 6), dpi=100)
plot = fig.add_subplot(111)

# Create canvas and toolbar once
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10)

toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()
toolbar.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

def button_click():
    stock_symbol = stock_input.get()
    stock = yf.Ticker(stock_symbol.upper())
    stock_historical = stock.history("1mo")

    x = stock_historical.index
    y = stock_historical["Close"]

    # Clear previous plot
    plot.clear()

    # Plot new data
    plot.plot(x, y, label=f"Trendline for {stock_symbol.upper()}")
    plot.set_title(f"Closing prices chart for {stock_symbol.upper()}")
    plot.set_xlabel("Date")
    plot.set_ylabel("Price")
    plot.legend()

    # Refresh canvas
    canvas.draw()

stock_button = ttk.Button(window, text="Visualize Stock", command=button_click)
stock_button.grid(row=0, column=2, padx=10, pady=10)

window.mainloop()
