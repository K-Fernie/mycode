#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import time
import matplotlib.pyplot as plt

def main():
    
    print("Assistant Manager running....")
    time.sleep(2)

    labels = 'Beets', 'Bears', 'Battlestar Galactica', 'Identity Theft'
    sizes=['20', '40','10','20' ]
    explode = (0,0.1,0,0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig("/home/student/mycode/graphing/schrute4Ever.pdf")
    # save a copy to "~/static" (the "files" view)
    print("Your beet farm is ready!")

main()

