import os
import pickle
import matplotlib.pyplot as plt

INDEX = ["startTime", "endTime", "acc_x", "acc_y", "acc_z", "gyr_x",
         "gyr_y", "gyr_z", "accGyr_temp", "bmp_temp", "pressure", "height"]


def pickleLoad(dirPath):
    """Loads all pickle files in a directory to a list"""
    data = []
    files = os.listdir(dirPath)
    for f in files:
        path = dirPath + "/" + f
        data.append(pickle.load(open(path, "rb")))
    return data


def sortData(data):
    """sort data into a specific index"""
    sortedData = []
    for i in data:
        for j in i:
            temp = []
            i2c = j["i2c"]
            temp.append(j["time"])
            temp.append(i2c[0])
            temp.append(i2c[1][0]["x"])
            temp.append(i2c[1][0]["y"])
            temp.append(i2c[1][0]["z"])
            temp.append(i2c[1][1]["x"])
            temp.append(i2c[1][1]["y"])
            temp.append(i2c[1][1]["z"])
            temp.append(i2c[1][2])
            temp.append(i2c[2])
            temp.append(i2c[3])
            temp.append(i2c[4])
            sortedData.append(temp)
    return sortedData


def sortByTime(data):
    """sort the data by start time"""
    data.sort()
    return data


def removeStartTime(data):
    """Removes the lowest time from all time elements"""
    data.sort()
    startTime = data[0][0]  # lowest time is the first time after sort
    for i in range(len(data)):
        data[i][0] = data[i][0] - startTime
        data[i][1] = data[i][1] - startTime
    return data


def soloList(data, index):
    """convert all values in a index in a list to a single list"""
    x = []
    for i in data:
        x.append(i[index])
    return x


def plot(data, x, yIndex):
    """Plot a figure with x, list from yIndex"""
    plt.figure(INDEX[yIndex])
    plt.plot(x, soloList(data, yIndex))
    print("Plotted", INDEX[yIndex], sep=": ")


def scatter(data, x, yIndex):
    """scatter data with x, list from yIndex"""
    plt.figure(INDEX[yIndex])
    plt.scatter(x, soloList(data, yIndex))
    print("Plotted", INDEX[yIndex], sep=": ")


data = pickleLoad("./data")
data = sortData(data)
data = sortByTime(data)
data = removeStartTime(data)
x = soloList(data, 0)
for i in range(2, len(data[0])):
    plot(data, x, i)
print("Display all plots: ")
plt.show()
print("Done")
