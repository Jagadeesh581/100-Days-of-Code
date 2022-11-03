import pandas


squirrels_data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Black"])
gray_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Cinnamon"])

squirrels_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrels_count, gray_squirrels_count, cinnamon_squirrels_count],
}

squirrels_df = pandas.DataFrame(squirrels_dict)
squirrels_df.to_csv("squirrels_data.csv")
