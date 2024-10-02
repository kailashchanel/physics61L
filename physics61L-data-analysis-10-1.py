# import csv
from pandas import *
# read csv file to a list of dictionaries
angles = [10, 20, 30, 45, 60]
trials = 5

for angle in angles:
    averages = []
    for i in range(trials):
        data = read_csv(f"{str(angle)}-trial-{str(i + 1)}.csv")
        
        status = data["Latest: GateState"].tolist()
        time = data["Latest: Time (s)"].tolist()

        avg_period = 2 * ((time[-2] - time[0]) / (len(time) / 2))

        print(f"\nAverage Period for {str(angle)}-trial-{str(i + 1)}: {avg_period}")

        averages.append(avg_period)

    print(f"\nAverage Period Over All Trials for {str(angle)} degrees: {sum(averages) / len(averages)}")