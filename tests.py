import numpy as np
import matplotlib.pyplot as plt

data = [[0.97666667, 0.62493333, 0.548,      0.548,      0.62493333],
 [0.548,      0.548,      0.97666667, 0.97666667, 0.62493333],
 [0.6272,     0.5892,     0.61853333, 0.626,      0.48266667],
 [0.84346667, 0.74493333, 0.91493333, 0.87773333, 0.82933333],
 [0.71813333, 0.8204,     0.85173333, 0.7948,     0.71826667],
 [0.85786667, 0.816,      0.9012,     0.8244,     0.90373333],
 [0.9272,     0.9288,     0.9164,     0.93533333, 0.944     ],
 [0.95946667, 0.93653333, 0.93466667, 0.9496,     0.95253333],
 [0.95973333, 0.93213333, 0.93906667, 0.96066667, 0.92773333],
 [0.9592,     0.95493333, 0.9516,    0.95106667, 0.94546667]]

test_no = [1,2,5,10,15,25,50,100,200,400]

data_classic = [0.62493333, 0.62493333, 0.626, 0.91493333, 0.85173333, 0.90373333, 0.944, 0.95946667,0.96066667,0.9592]


fig, ax = plt.subplots()
ax.set_title('Precision depending on the number of trees ')
ax.set_xlabel('Number of trees')
ax.set_ylabel('Precision')
label = ["1","2","5","10","15","25","50","100","200","400"]
ax.set_xticklabels(label)

pic1 = ax.boxplot(data)
array = np.arange(1,len(test_no)+1)
pic2 = ax.plot(array,data_classic,'o',label='classic version')#
ax.legend([pic1["boxes"][0], pic2[0]], ['my version', 'classic version'], loc='lower right')
plt.show()
