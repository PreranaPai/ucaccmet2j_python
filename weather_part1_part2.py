import json

with open ('precipitation.json') as file:
    precipitation_data =  json.load(file)

precipitation_seattle = []
for list_entry in precipitation_data:
    if list_entry["station"] == "GHCND:US1WAKG0038":
        precipitation_seattle.append(list_entry)

precipitation_seattle_monthly = []
for i in range(1, 13):
    precipitation_monthly = 0
    for list_entry in precipitation_seattle:
        split_date = list_entry["date"].split('-')
        if int(split_date[1]) == i:
            precipitation_monthly = precipitation_monthly + int(list_entry["value"])
    precipitation_seattle_monthly.append(precipitation_monthly)
print(precipitation_seattle_monthly)

with open('result1.json','w') as file:
    json.dump(precipitation_seattle_monthly, file)

precipitation_seattle_yearly_total = 0
for list_entry in precipitation_seattle:
    precipitation_seattle_yearly_total = precipitation_seattle_yearly_total + int(list_entry["value"])
print(precipitation_seattle_yearly_total)

precipitation_relative_monthly = []
for list_entry in precipitation_seattle_monthly:
    precipitation_monthlypercentage = (list_entry/precipitation_seattle_yearly_total) * 100
    precipitation_relative_monthly.append(f'{precipitation_monthlypercentage}%')
print(precipitation_relative_monthly)

summery_precipitation_info = {
'station': 'GHCND:US1WAKG0038',
'state': 'WA',
'totalMonthlyPrecipitation': precipitation_seattle_monthly,
'relativeMonthlyPrecipitation': precipitation_relative_monthly,
'totalYearlyPrecipitation': precipitation_seattle_yearly_total
}

with open('result2.json','w') as file:
    json.dump(precipitation_relative_monthly, file)
    json.dump(precipitation_seattle_yearly_total, file)



    
    