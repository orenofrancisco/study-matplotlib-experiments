import csv
import matplotlib.pyplot as plt

from datetime import datetime

def graph_this(domain, codomains, title, filename):
    # To improve reusability and not type as much, I made this function
    # While not as flexible as rewriting everything again, it saves time
    fig = plt.figure(dpi=128, figsize=(10, 6))

    for item in codomains:
        plt.plot(dates_temp, item, alpha=0.5, linewidth=2)
    
    # Let's give it a bit of color
    plt.title(title, size=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=12)

    # Save the graph
    plt.savefig(filename)


with open('montevideo_weather_data.csv') as f:
    reader = csv.reader(f)

    # We have to skip to line 4 to get the headers
    # I am not particularily interested in them but we have to iterate
    # over them to get to the data
    for _ in range(4):
        headers = next(reader)
    
    # Uncomment this to see the headers of the dataset
    """
    for index, title in enumerate(headers):
        print(index, title)
    """

    dates_temp = []
    highest_temp = []
    lowest_temp = []
    dates_sun = []
    sunrise = []
    sundown = []
    dates_uv = []
    uv_index_max = []

    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        
        # Date+Temperature data fetch
        try:
            dates_t = date
            high_temp = float(row[1])
            low_temp = float(row[2])
        except:
            pass
        else:
            dates_temp.append(date)
            highest_temp.append(high_temp)
            lowest_temp.append(low_temp)

        # Sunrise/Sundown data synthesis
        try:
            dates_s = date
            
            t_sunrise = row[3]
            t_sunrise = t_sunrise[-5:]
            t_sunrise = datetime.strptime(t_sunrise, '%H:%M')

            t_sundown = row[4]
            t_sundown = t_sundown[-5:]
            t_sundown = datetime.strptime(t_sundown, '%H:%M')
        except:
            pass
        else:
            dates_sun.append(dates_s)
            sunrise.append(t_sunrise)
            sundown.append(t_sundown)
    
        # UV Index data synthesis
        try:
            date_uv = date
            t_uv_max = float(row[5])
        except:
            pass
        else:
            dates_uv.append(date_uv)
            uv_index_max.append(t_uv_max)
    
    graph_this(domain=dates_temp,
            codomains=[highest_temp, lowest_temp], 
            title="Temperature variation in Montevideo, Uruguay", 
            filename="images/015_temperature_montevideo.png")

    graph_this(domain=dates_sun,
            codomains=[sunrise, sundown],
            title="Sunrise and sundown in Montevideo, Uruguay",
            filename="images/015_sunrise_and_sundown_in_mvd.png")

    graph_this(domain=dates_uv,
            codomains=[uv_index_max],
            title="UV Index max, daily, in Montevideo, Uruguay",
            filename="images/015_uv_max_daily_in_mvd.png")
