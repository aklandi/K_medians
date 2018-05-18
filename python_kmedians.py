import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import make_moons
from geom_median import geom_median

#Test on the iris data if you choose.
# I've also uploaded the Pokemon data.  You will read that in similar to the iris data.

#
# param: data - the data we want to calculate the total within sum of abs. diff.
# param: clusters - the cluster assignments for each data point
# param: k - the number of clusters
#
# return: the total within sum of absolute differences
#
def within_sum(data, clusters, k):

    xbar = 0
    inside = [0 for i in range(k)]

    #calculate the median for each cluster
    #subtract the median from each point in a cluster
    #and add
    for i in range(k):
        dt = data[clusters == i,:]
        med = 
        n,m = 
        repeated = numpy.array([med for j in range(n)])
        inside[i] = 

    return inside

#
# param: data - the data we want the total sum of absolute differences
#
# return: the total sum of absolute differences
#
def tot_sum(data):
    
    #need to calculate the total average for each cluster
    #then create a matrix for both
    avg = numpy.mean(data, axis = 0)
    n,m = numpy.shape(data)
    r = numpy.array([avg for i in range(n)])
  
    #then do the total sum of absolute differences formula
    return( numpy.sum( numpy.abs( (data - r) ) ) )

#
# param: data - the data we want to calculate between sum of squares
# param: clusters - the cluster assignments
# param: k - the number of clusters
#
# return: the between cluster sum of squares
#  
def between_sum(data, clusters, k):  
  
  inside = 
  totes = 
  
  return( totes - inside )
  
def my_kmedians(data, k, maxiter):
    
    #determine dimensions of data
    numIndiv, numFetrs = numpy.shape(data)
  
    #initialize the centers to be some random
    #subset of the data
    centers = 
    #initialize a vector for cluster assignments
    clusterAssignments = [ 0 for j in range(numIndiv) ]
    #initialize the distance
    d = [ 0 for j in range(k) ]
    
    #we'll iterate the number of times you deem necessary
    for iter in range(maxiter):
    
        #this loop will iterate over all data points
        #we'll calculate the distance from all centers
        #then assign the data point to the cluster whose
        #center is the smallest distance
        for i in range(numIndiv):
      
            #determine distances to all centers
            for j in range(k):
        
                d[j] = 
        
            #assign the point to the cluster with the 
            #smallest distance
            clusterAssignments[i] = 
        
        
        #now update the new centers by calculating 
        #the new means
        for j in range(k):
            indx = numpy.array(clusterAssignments) == j
            centers[j,:] = 
    

    #calculate the within sum of squares. 
    #we want points to be more similar within clusters
    #so we expect this to be smaller than between
    within = 
  
    #calculate the between sum of squares.
    #we want points to be less similar between clusters
    #so we expect this to be larger than the within 
    between = 
  
    tot = tot_sum(data)
  
    #To check effectiveness, look at betweenSS/sum(withinSS)
    #if it's large, then success!  You should be asking, how large
    #is too large
    ratio = 
  
    #return both the cluster assignments and the final centroids
    return {"assign":numpy.array(clusterAssignments), "center":centers, "w":within,"b":between,"F_ratio":ratio}
  
kmed = my_kmedians(X,2,100)

cluster_assign = kmed["assign"]
clus1 = X[cluster_assign == 0,:]
clus2 = X[cluster_assign == 1,:]

fig2 = plt.figure(2)
plt.scatter(clus1[:,0],clus1[:,1],color = 'red', marker = 'o')
plt.scatter(clus2[:,0],clus2[:,1],color = 'blue', marker = '+')
 
fig2.show()