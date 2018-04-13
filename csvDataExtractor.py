import matplotlib.pyplot as plt
f = open("Launch_P-1B.csv", "r")
INDEX = ["startTime", "endTime", "acc_x", "acc_y", "acc_z", "gyr_x",
         "gyr_y", "gyr_z", "accGyr_temp", "bmp_temp", "pressure", "height"]
# currIndex =  ,ax/ms2,ay/ms2,az/ms2,ba/m,bp/pa,bt/degc,gps,gx/dsec,gy/dsec,gz/dsec,it/degc,t1,t2
# currIndex =
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


data = []
line = f.readline()
while line != "":
    data.append(readline(line))
    line = f.readline()

for i in data[0:5]:
    for j in i:
        print(j)
