# Code for indvidually finding rain data for one location, and creating a summary

# Open the .json file and load it to a variable
import json

with open ('precipitation.json') as file:
    precipitation_data =  json.load(file)

# Create an empty list with choosing only the entrie with station name Seattle
precipitation_seattle = []
for list_entry in precipitation_data:
    if list_entry["station"] == "GHCND:US1WAKG0038":
        precipitation_seattle.append(list_entry)

# The date is split by '-' to separate and group by month using a for loop
precipitation_seattle_monthly = []
for i in range(1, 13):
    precipitation_monthly = 0
    for list_entry in precipitation_seattle:
        split_date = list_entry["date"].split('-')
        if int(split_date[1]) == i:
            precipitation_monthly = precipitation_monthly + int(list_entry["value"])
    precipitation_seattle_monthly.append(precipitation_monthly)
print(precipitation_seattle_monthly)

# Save results in a .json file as result of part 1
with open('result1.json','w') as file:
    json.dump(precipitation_seattle_monthly, file)

# Calculate the total rain for the year, per station under the for loop
precipitation_seattle_yearly_total = 0
for list_entry in precipitation_seattle:
    precipitation_seattle_yearly_total = precipitation_seattle_yearly_total + int(list_entry["value"])
print(precipitation_seattle_yearly_total)

# Relative rain as a percentage of yearly total per station, using a for loop with the monthly data
precipitation_relative_monthly = []
for list_entry in precipitation_seattle_monthly:
    precipitation_monthlypercentage = (list_entry/precipitation_seattle_yearly_total) * 100
    precipitation_relative_monthly.append(f'{precipitation_monthlypercentage}%')
print(precipitation_relative_monthly)

# Summary dictionary with below mentioned variables
summery_precipitation_info = {
'station': 'GHCND:US1WAKG0038',
'state': 'WA',
'totalMonthlyPrecipitation': precipitation_seattle_monthly,
'relativeMonthlyPrecipitation': precipitation_relative_monthly,
'totalYearlyPrecipitation': precipitation_seattle_yearly_total
}

# Save results in a .json file as result of part 2
with open('result2.json','w') as file:
    json.dump(precipitation_relative_monthly, file)
    json.dump(precipitation_seattle_yearly_total, file)



    
    