# Working with multiple figure windows and subplots

import csv
import numpy as np
from matplotlib import dates
from datetime import datetime
import matplotlib.pyplot as plt

with open('tracker.csv') as file:
    csvr = csv.reader(file)
    plt.figure('exercisin\'')
    plt.ylabel("Exercises Done")
    plt.xlabel("time Y-M-D")
    
    t = True
    data = []
    for row in csvr:
        if t:
            l = len(row) - 1
            t = False
            data.append(row)
        else:
            r = []
            for e, i in enumerate(row):
                if e != l:
                    r.append(float(i))
                else:
                    r.append(i)
            data.append(r)

    data = np.array(data)
    ds = data[1:,-1]
    for i in range(l):
        plt.plot(   dates.date2num([datetime.strptime(date, '%Y-%m-%d') for date in ds]),
                    data[1:,i],
                    label=data[0,i])
    plt.legend()
    plt.show()
