from yahoo_fin.stock_info import get_data, get_day_most_active
import pandas as pd


nio_weekly = get_data("NIO",start_date="12/21/2020", end_date="01/23/2021", index_as_date = True, interval="1mo")
print(nio_weekly)

nio_active = get_day_most_active()
print(nio_active)