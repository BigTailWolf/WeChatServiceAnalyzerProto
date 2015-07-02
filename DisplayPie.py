#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def displayPie(keys, values, title_msg):

    x = np.char.array(keys)
    y = np.array(values)

    total = y.sum()

    percent = 100.0 * y / total if total else [0,] * len(y)

    matplotlib.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})

    patches, texts, pct = plt.pie(y, labels = x, autopct = u'%1.2f%%', shadow = True, startangle = 180, radius = 0.8)
    xlabels = [u'{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, percent)]

    plt.title('Just a figure', bbox={'facecolor':'0.8', 'pad':5})
    plt.legend(patches, xlabels, loc='center left', bbox_to_anchor=(-0.1, 0.2),
               fontsize=8)

    plt.show()


if __name__ == '__main__':

    keys   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov','Dec']
    values = [234, 64, 54,10, 0, 1, 0, 9, 2, 1, 7, 7]
    displayPie(keys, values, 'Just a figure')

