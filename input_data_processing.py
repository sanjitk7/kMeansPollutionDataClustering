import csv
import json

def prep_data():
    with open ("city_population.json") as read_json:
        data  = json.load(read_json)
    print(data)

    with open ('air_quality_PM10_2012.csv',encoding="utf-8", errors="ignore") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        population_dict = dict()
        pm10_dict = dict()
        for row in readCSV:
            if row[1] in data:
                if row[9] != "Null":
                    pm10_dict[row[1]] = row[9]
                    population_dict[row[1]] = data[row[1]]

        print(population_dict)
        print(pm10_dict)
        print(len(population_dict))
        print(len(pm10_dict))

        return population_dict, pm10_dict



