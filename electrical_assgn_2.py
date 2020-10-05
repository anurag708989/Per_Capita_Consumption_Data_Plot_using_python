import numpy as np
import matplotlib.pyplot as plt
############################# Per-Capita Consumption ####################################################################################
x2=int(input("Enter Year"))
y2=float(input("Enter Per-Capita Consumption in correspondin year"))
x1=np.array([1947,1950,1956,1961,1966,1974,1979,1985,1990,1997,2002,2007,2012,2013,2014,2015,2016,2017,2018,2019])
y1=np.array([16.3,18.2,30.9,45.9,73.9,126.2,171.6,228.7,329.2,464.6,671.9,559.2,883.6,914.4,957,1010.0,1075,1122,1149,1181])
plt.xlabel("YEAR")
plt.ylabel("Per-Capita Consumption (in KWH)")
plt.title("Per-Capita Consumption Year Wise")
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.scatter(x2,y2,color="black")
plt.scatter(x1,y1,color="orange")
plt.show()

############################ Per -Capita Consumption State Wise #############################################################################
x3=np.array(['Dadra ','D&D','Goa','Guj','Cht','Mh','MP','Pudu','TN','AP','Telan','Kr','Ker','Laks','Pb','Hr','DL','HP','UK','Ch','J&K','RJ','UP','Od','SK','Jh','WB','A&N ','BH','ArP','Meg','Miz','Naga','Tri','AM','Mani'])
y3=np.array([15783,7965,2466,2279,2016,1307,989,1784,1847,1319,1551,1367,763,633,2028,1975,1574,1340,1454,1128,1282,1166,585,1622,806,915,665,370,272,648,832,523,345,470,339,326])
x4=input("enter your Area/State")
y4=float(input("Enter Per-Capita of your State or Area"))
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.bar(x3,y3,color='orange')
plt.bar(x4,y4,color='red')
plt.xlabel("STATES")
plt.ylabel("Per-Capita Consumption(KWH/year)")
plt.title("Per-Capita Consumption Statewise")
plt.show()
