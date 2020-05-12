import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
print(data)
data_2 = data['x'] + data['y']
print(data_2)
data_2.to_csv("sampledata_x_2.txt", index=None)
