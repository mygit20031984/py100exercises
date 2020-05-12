import pandas
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
data = pandas.concat([data1,data2])

data.to_csv("sampledata_1.txt", index=None)