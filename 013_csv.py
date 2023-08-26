import csv
import matplotlib.pyplot as plt

with open('weather_data.csv') as f:
    reader = csv.reader(f)

    # Uncomment this if you wish to read the headers
    headers = next(reader)
    """
    for index, title in enumerate(headers):
        print(index, title.strip())
    """

    highs = []
    for row in reader:
        highs.append(int(row[1]))

    # Let's plot it!
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # Let's give it a bit of color
    plt.title("Daily high temperatures, July 2014", size=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Let's see our work now
    plt.show()
