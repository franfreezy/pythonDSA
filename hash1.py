#nyc_weather.csv contains new york city weather for first few days in the month of
# January. 
#Write a program that can answer following,
#What was the average temperature in first week of Jan
#What was the maximum temperature in first 10 days of Jan
#Figure out data structure that is best for this problem

import pandas as pd


df=pd.read_csv(r"nyc_weather.csv", index_col="date")
my_dict=df.to_dict()


print(my_dict)
     







