"""
csvDataExtractor.py
Creator: Sindre Aalhus
Version: 1.4
Program to retrive data from a csv file, remodell the structure of the file and plot the result
"""

import matplotlib.pyplot as plt
f = open("Launch_P-1B.csv", "r")
finalIndex = ["startTime", "endTime", "acc_x", "acc_y", "acc_z", "gyr_x",
              "gyr_y", "gyr_z", "accGyr_temp", "bmp_temp", "pressure", "height"]
f.readline()


def timeConverter(data):
    """Convert from date format to seconds

    Arguments:
        data {list} -- the list of data to convert time data to correct format
    """
    data = data.split(" ")
    data.remove(data[0])
    data = data[0].split(":")
    data[2] = float(data[2]) + float(data[0])*3600
    data[2] = float(data[2]) + float(data[1])*60
    return data[2]


def readline(line):
    """Convert from a line to a array in a predefined index

    Arguments:
        line {string} -- the line to convert
    """
    tempArray = []
    line = line.split(",")
    line.remove(line[0])
    line.remove(line[6])
    line.remove(line[6])
    ind = [0, 1, 2, 6, 7, 8, 9, 5, 4, 3]
    tempArray.append(timeConverter(line[10]))
    tempArray.append(timeConverter(line[11]))
    for i in ind:
        tempArray.append(float(line[i]))
    return tempArray


def removeStartTime(sortedData):
    """Removes start time from time values

    Arguments:
        sortedData {list} -- the data sorted with lowest time first
    """
    t0 = sortedData[0][0]
    for i in range(len(sortedData)):
        sortedData[i][0] = sortedData[i][0] - t0
        sortedData[i][1] = sortedData[i][1] - t0
    return sortedData


def toSingleArray(sortedTimelessData, index):
    """convert a index of data to a single array

    Arguments:
        sortedTimelessData {list} -- a list sorted and removed lowest time from all values
        index {int} -- the index of the list to convert
    """
    tempArray = []
    for i in range(len(sortedTimelessData)):
        tempArray.append(sortedTimelessData[i][index])
    return tempArray


def afterAndBeforeArray(data, t_start, t_end):
    """remove data before t_start and after t_end

    Arguments:
        data {list} -- the list to remove some data from
        t_start {int} -- the time value to remove all data before
        t_end {int} -- the time value to remove all data after
    """
    tempArray = []
    for i in range(len(data)):
        if data[i][0] >= t_start and data[i][0] <= t_end:
            tempArray.append(data[i])
    return tempArray


def plot(data, index):
    """Plot data with x as time axis

    Arguments:
        data {list} -- the list of data to plot
        index {int} -- the index of the list to plot
    """
    plt.figure(finalIndex[index])
    # plt.scatter(toSingleArray(data, 0), toSingleArray(data, index))
    plt.plot(toSingleArray(data, 0), toSingleArray(data, index))


def main():
    """Main function
    """
    data = []
    line = f.readline()
    while line != "":
        data.append(readline(line))
        line = f.readline()
    data.sort()
    data = removeStartTime(data)
    data = afterAndBeforeArray(data, 300, 800)
    for i in range(2, len(data[0])):
        plot(data, i)
    plt.show()  # looked at data, seems luanch at t = 300++ a bit and crash at 800--


main()
