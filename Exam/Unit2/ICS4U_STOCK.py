# import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import time as now_time

# Class to get stock data
class StockData:
    def __init__(self, symbol='', start_date='', end_date=''):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

# Class to get historical stock data
class HistoricalStockData(StockData):
    def __init__(self, symbol='', start_date='', end_date='', historical_data=None):
        super().__init__(symbol, start_date, end_date)
        self.historical_data = historical_data
    
    # Get historical stock data
    def get_historical_data(self):
        self.historical_data = yf.download(self.symbol, start=self.start_date, end=self.end_date) #download the stock data
    
    # search the stock data and display the historical data
    def plot(self):
        # get the historical data
        self.get_historical_data()
        # display the historical data
        self.historical_data['Close'].plot()
        plt.title(f'{self.symbol} Stock Price from {self.start_date} to {self.end_date}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

def TimeChecker(time):
    if len(time) != 10: # check the length of the input
        return False
    elif str(time[4]) != '-' or str(time[7]) != '-': # check the format of the input
        return False
    elif time.count('-') != 2: # check the times of '-'
        return False
    # Split the date into year, month, and day
    year, month, day = time.split('-')
    # Check if year, month, and day are all digits
    if not (year.isdigit() and month.isdigit() and day.isdigit()): 
        return False
    # Convert year, month, and day to integers
    year, month, day = map(int, [year, month, day])
    # Get the current time
    now = now_time.localtime()
    current_year, current_month, current_day = now.tm_year, now.tm_mon, now.tm_mday
    if  year>= 1970 and year <= current_year and month >= 1 and month <= 12: # check the year and month
        # check the now year data
        if year == current_year:
            if month > current_month:
                return False
            elif month == current_month:
                if day > current_day:
                    return False
        # check the day
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day >= 1 and day <= 31:
                return True
        elif month in [4, 6, 9, 11]:
            if day >= 1 and day <= 30:
                return True
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if day >= 1 and day <= 29:
                    return True
            else:
                if day >= 1 and day <= 28:
                    return True
    return False

print('Please type the start date and end date in the format of yyyy-mm-dd')
while True: # loop to get the start date and end date
    while True:
        start_date = input('Please type the start date: ')
        if TimeChecker(start_date):
            break
        else:
            print('Invalid input')
    while True:
        end_date = input('Please type the end date: ')
        if TimeChecker(end_date):
            break
        else:
            print('Invalid input')
    # check start date must be earlier than end date
    if start_date < end_date:
        break
    print('Invalid input: start date must be earlier than end date')

msft = HistoricalStockData("MSFT", start_date, end_date)
msft.plot()

aapl = HistoricalStockData("AAPL", start_date, end_date)
aapl.plot()

exit()