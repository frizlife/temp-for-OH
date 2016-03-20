import matplotlib.pyplot as plt
import pandas as pd
import scipy
import random
import math
import numpy as np
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq
from operator import sub

data = pd.read_csv('un.csv', header=False)

data= data[data.lifeMale.notnull() & data.lifeFemale.notnull() & data.infantMortality.notnull() & data.GDPperCapita.notnull()] #removes null values

b = data[['lifeMale', 'lifeFemale', 'infantMortality', 'GDPperCapita']] #converting to numpy representation in ND frame

print "Data values"
print b

for k in range (1, 11):
    centroids, distortion = kmeans(b.values, k)
    #print kmeans(b.values, k)
    
print ""
print("Centroid locations")
print centroids

#distance between each point and each cluster centroid
centroid_distance = np.zeros((len(centroids), len(b.index)), dtype = np.object) #create matrix to store results
print centroid_distance
print type(centroid_distance)


for i_centroid, centroid in enumerate(centroids):
    for i_data, data_point in enumerate(b):
        #print i_centroid
        #print centroid
        print i_data
        print data_point
        print centroids[i_data, data_point]
        print b[i_data, data_point]
        #distance = sum([(a-b)**2 for a,b in zip(i_centroid, centroid)])
        #centroid_distance[i_data, i_centroid] = distance

#print centroid_distance
'''
print dist
print len(dist)
print ance
print len(ance)
zz = zip(dist, ance)
print ""
print "ZZZZZ"
'''

'''        
        #distance =  (centroids[i_data, i_centroid] - b.values[i_data, i_centroid])
        [(i_centroid, i_data) for i_centroid in enumerate(centroids) for i_data in enumerate(b) if i_centroid<>i_data dist.append(centroids[i_data, i_centroid] - b.values[i_data, i_centroid])]
        #print centroids[i_data, i_centroid]
        #print b.values[i_data, i_centroid]
        #centroid_distance[i_data, i_centroid] = distance
'''
'''
        distance = centroids[i_data] - b.iloc[i_data]
        #print distance
        distance_list = np.asarray(distance)
        distance_list.reshape(shape)
        #print type(distance_list)
        #print distance_list[i_data]
        #centroid_distance[i_data, i_centroid] = distance_list[i_data]
        #print centroid_distance
'''
"""
print ""
print "Centroid distance"
print centroid_distance

#closest centroid for each point
id, z = vq(b.values, centroids)
print""
print("Closest centroid for each data point:")
print id

wcss = np.zeros(len(centroids))
for i_data, data_point in enumerate(b):
     centroid_num = id[i_data]
     #print centroid_num
     #distance = [(centroids[centroid_num] - b.values[i_data])**2 for i_data in enumerate(b)]
     #distance = centroids[centroid_num] - b.values[i_data]
     distance = np.linalg.norm(centroids[centroid_num] - b.values[i_data])
     wcss += distance

print ""
print "Within Cluster Sum of Squares:"
print wcss
"""