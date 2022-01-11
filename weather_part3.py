import json

with open ('precipitation.json') as file:
    precipitation_data =  json.load(file)

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

summary_precipitation_overall = {}       

precipitation_yearly_total = 0
for list_entry in precipitation_data:
    precipitation_yearly_total = precipitation_yearly_total + int(list_entry["value"])
print(precipitation_yearly_total)

for i in range(len(station_names)):
    station_name = station_names[i]
    location_name = location_names[i]
    state_name = state_names[i]
    precipitation_station = []
    for list_entry in precipitation_data:
        if list_entry["station"] == station_name:
            precipitation_station.append(list_entry)

    precipitation_station_monthly = []
    for i in range(1, 13):
        precipitation_monthly = 0
        for list_entry in precipitation_station:
            split_date = list_entry["date"].split('-')
            if int(split_date[1]) == i:
                precipitation_monthly = precipitation_monthly + int(list_entry["value"])
        precipitation_station_monthly.append(precipitation_monthly)
    print(precipitation_station_monthly)

    precipitation_station_yearly_total = 0
    for list_entry in precipitation_station:
        precipitation_station_yearly_total = precipitation_station_yearly_total + int(list_entry["value"])
    print(precipitation_station_yearly_total)

    precipitation_relative_monthly = []
    for list_entry in precipitation_station_monthly:
        precipitation_monthlypercentage = (list_entry/precipitation_station_yearly_total) * 100
        precipitation_relative_monthly.append(f'{precipitation_monthlypercentage}%')
    print(precipitation_relative_monthly)

    for list_entry in precipitation_station_monthly:
        precipitation_relative_station = (list_entry/precipitation_yearly_total)
    print(precipitation_relative_station)

    
    summary_precipitation_station = {
        'station': station_name,
        'state': state_name,
        'totalMonthlyPrecipitation': precipitation_station_monthly,
        'relativeMonthlyPrecipitation': precipitation_relative_monthly,
        'totalYearlyPrecipitation': precipitation_station_yearly_total,
        'relativeYearlyPrecipitation': precipitation_relative_station
        }
    
    summary_precipitation_overall[location_name] = summary_precipitation_station

with open('result3.json','w') as file:
    json.dump(summary_precipitation_overall, file, indent =5)
        
