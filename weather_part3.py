# Code for finding rain data for all given locations, and creating a summary

# Open the .json file and load it to a variable
import json

with open ('precipitation.json') as file:
    precipitation_data =  json.load(file)

# Open, strip and split the .csv file and create lists with data from its columns
with open('stations.csv') as station_file:
    stations_data = station_file.read()

station_names = []
location_names = []
state_names = []
with open('stations.csv') as file:
    headers = file.readline()
    for line in file:      
        column = line.strip().split(',')
        station_names.append(column[2])
        location_names.append(column[0])
        state_names.append(column[1])

# Dictionary for later in the code outside the loop
summary_precipitation_overall = {}       

# Loop to calculate total rain in all the stations 
precipitation_yearly_total = 0
for list_entry in precipitation_data:
    precipitation_yearly_total = (precipitation_yearly_total + int(list_entry["value"]))
print(precipitation_yearly_total)

# Overall loop to apply the whole code for every station 
for i in range(len(station_names)):
    station_name = station_names[i]
    location_name = location_names[i]
    state_name = state_names[i]
    precipitation_station = []
    # A loop that checks the name of each station against the station in the list
    for list_entry in precipitation_data:
        if list_entry["station"] == station_name:
            precipitation_station.append(list_entry)

    # The date is split by '-' to separate and group by month using a for loop
    precipitation_station_monthly = []
    for i in range(1, 13):
        precipitation_monthly = 0
        for list_entry in precipitation_station:
            split_date = list_entry["date"].split('-')
            if int(split_date[1]) == i:
                precipitation_monthly = (precipitation_monthly + int(list_entry["value"]))
        precipitation_station_monthly.append(precipitation_monthly)
    print(precipitation_station_monthly)

    # Calculate the total rain for the year, per station under the for loop
    precipitation_station_yearly_total = 0
    for list_entry in precipitation_station:
        precipitation_station_yearly_total = (precipitation_station_yearly_total + int(list_entry["value"]))
    print(precipitation_station_yearly_total)

    # Relative rain as a percentage of yearly total per station, using a for loop with the monthly data 
    precipitation_relative_monthly = []
    for list_entry in precipitation_station_monthly:
        precipitation_monthlypercentage = (list_entry/precipitation_station_yearly_total) * 100
        precipitation_relative_monthly.append(f'{precipitation_monthlypercentage}%')
    print(precipitation_relative_monthly)

    # Relative yearly rain for each station as a percentage of total rain for every location
    for list_entry in precipitation_station_monthly:
        precipitation_relative_station = (list_entry/precipitation_yearly_total) * 100
    print(precipitation_relative_station)

    # Summary dictionary with variables coded for above
    summary_precipitation_station = {
        'station': station_name,
        'state': state_name,
        'totalMonthlyPrecipitation': precipitation_station_monthly,
        'relativeMonthlyPrecipitation': precipitation_relative_monthly,
        'totalYearlyPrecipitation': precipitation_station_yearly_total,
        'relativeYearlyPrecipitation': precipitation_relative_station
        }
    
    # A dictionary nesting the previous one grouping by location name
    summary_precipitation_overall[location_name] = summary_precipitation_station

#Saving the results as a .json file
with open('result3.json','w') as file:
    json.dump(summary_precipitation_overall, file, indent =5)
        
