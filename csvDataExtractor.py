import matplotlib.pyplot as plt
f = open("Launch_P-1B.csv", "r")
INDEX = ["startTime", "endTime", "acc_x", "acc_y", "acc_z", "gyr_x",
         "gyr_y", "gyr_z", "accGyr_temp", "bmp_temp", "pressure", "height"]
f.readline()


def timeConverter(data):
    """convert from date format to seconds"""
    data = data.split(" ")
    data.remove(data[0])
    data = data[0].split(":")
    data[2] = float(data[2]) + float(data[0])*3600
    data[2] = float(data[2]) + float(data[1])*60
    return data[2]


def readline(line):
    """convert from a line to a array in a predefined index"""
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
    """removes start time from time values"""
    t0 = sortedData[0][0]
    for i in range(len(sortedData)):
        sortedData[i][0] = sortedData[i][0] - t0
        sortedData[i][1] = sortedData[i][1] - t0
    return sortedData


def toSingeArray(sortedTimelessData, index):
    tempArray = []
    for i in range(len(sortedTimelessData)):
        tempArray.append(sortedTimelessData[i][index])
    return tempArray


data = []
line = f.readline()
while line != "":
    data.append(readline(line))
    line = f.readline()
data.sort()
data = removeStartTime(data)
