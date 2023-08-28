import json

# Our test data, population_data.csv, is a long list of about 12000 dictionaries
# each containing 4 fields: "Country Code", "Country Name", "Year" and "Value".
#
# There are also multiple entries for each country, different years.
#
# I know this because I inspected the file beforehand using the commands:
#   head population_data.csv (just to see what's what)
#   cat population_data.csv | grep -icE '\"Country Code\"' (count the records)
#   cat population_data.csv | grep -iE '\"Country Code\"' (checked for repeats)

# Open the file and load pertinent data
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Now let's render 2010's population data
for item in pop_data:
    if item['Year'] == '2010':
        country_name = item['Country Name']
        population = item['Value']
        print(country_name, ":", population)
