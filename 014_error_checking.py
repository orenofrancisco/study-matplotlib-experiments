import csv
import matplotlib.pyplot as plt

from datetime import datetime

def f_to_c(temp=0.0):
    return (temp - 32) / 1.8

with open('death_valley_weather_data.csv') as f:
    reader = csv.reader(f)

    # Uncomment this if you wish to read the headers
    headers = next(reader)
    """
    for index, title in enumerate(headers):
        print(index, title.strip())
    """

    dates = []
    highest_temp = []
    lowest_temp = []

    for row in reader:
        try:
            # There are empty datapoints so we must fetch all
            # the data at once and handle skip missing points
            # together
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            f_high_temp = int(row[1])
            f_low_temp = int(row[3])
        except:
            # Only ValueError type exceptions are expected
            continue
        else:
            # Format the date before appending it
            dates.append(current_date)

            # I cannot read Fahrenheit so I made an auxiliary function above       
            # to convert to Celcius, the standard unit for temperature
            c_high_temp = f_to_c(f_high_temp)
            highest_temp.append(c_high_temp)

            c_low_temp = f_to_c(f_low_temp)
            lowest_temp.append(c_low_temp)

    # Let's plot it!
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highest_temp, c='red', alpha=0.5)
    plt.plot(dates, lowest_temp, c='blue', alpha=0.5)
    plt.fill_between(dates, highest_temp, lowest_temp, facecolor='blue', alpha=0.1)

    # Let's give it a bit of color
    plt.title("Daily high/low temperatures, 2014 - Death Valley, CA, USA", size=20)
    plt.xlabel('', fontsize=16)
    # This next command reformats the labels as dates, so they don't step on each other
    fig.autofmt_xdate()
    plt.ylabel("Temperature (C)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Let's see our work now
    plt.show()
