import numpy as np
import matplotlib.pyplot as plt

import operator
import collections as col

myList = []

engDictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


def read_file():
    with open('speer.txt') as f:
        string = f.read()
        string = string.upper()
        myList.extend(string)


def get_frequency():
    for x in engDictionary.keys():
        count = myList.count(x)
        print(str(x) + " = " + str(count))
        engDictionary[x] = count


def show_plot():
    keys = list(engDictionary.keys())
    values = list(engDictionary.values())
    y_pos = np.arange(len(keys))

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, keys)
    plt.ylabel('Count')
    plt.title('N = ' + str(len(myList)))

    plt.show()


def show_plot_sorted():
    diction = sorted(engDictionary.items(), key=operator.itemgetter(1), reverse=True)
    diction = col.OrderedDict(diction)

    keys = list(diction.keys())
    values = list(diction.values())
    y_pos = np.arange(len(keys))

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, keys)
    plt.ylabel('Count')
    plt.title('N = ' + str(len(myList)))

    plt.show()



read_file()
get_frequency()
# show_plot_sorted()
show_plot()


