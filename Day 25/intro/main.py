# import csv
#
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas


data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))
print(type(data["temp"]))

# Convert data to dictionary.
data_dict = data.to_dict()
print(data_dict)

# Convert data['temp'] to list.
temp_list = data["temp"].to_list()
print(temp_list)

# Mean of temperatures (average of temp).
print(data["temp"].mean())
# Max of temperature.
print(data["temp"].max())

# Get data in column.
print(data["condition"])
print(data.condition)

# Get data in row.
print(data[data.day == "Monday"])
# Get max temp row.
print(data[data.temp == data.temp.max()])

# Get the Monday temp and convert to Fahrenheit.
monday = data[data.day == "Monday"]
monday_temp_C = int(monday.temp)
monday_temp_F = monday_temp_C * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch.
student_dict = {
    "student": ["Jagadeesh", "Amy", "Angela", "James"],
    "score": [62, 55, 65, 75],
}
student_data = pandas.DataFrame(student_dict)
print(student_data)
student_data.to_csv("student_data.csv")
