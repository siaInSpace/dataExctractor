import matplotlib.pyplot as plt
f = open("Launch_P-1B.csv", "r")
INDEX = ["startTime", "endTime", "acc_x", "acc_y", "acc_z", "gyr_x",
         "gyr_y", "gyr_z", "accGyr_temp", "bmp_temp", "pressure", "height"]


def timeConverter(data):  # 2018-03-22 03:22:11.140776
    data = data.split(" ")
    data.remove(data[0])
    data = data[0].split(":")
    data[2] = float(data[2]) + float(data[0])*3600
    data[2] = float(data[2]) + float(data[1])*60
    return data[2]
