import numpy

def geom_median(data,maxiter):
    
    #Implementation of the Weiszfeld's algorithm
    #to find the geometric median.
  
    #Source: Vardi, Yehuda, and Cun-Hui Zhang. 
    #        "A modified Weiszfeld algorithm for the 
    #        Fermat-Weber location problem."  
  
    n,m = numpy.shape(data); 
  
    #initialize our median.  We must initialize
    #randomly.  We do not want y to be in the 
    #original data. Method may not converge if so.
    y = numpy.random.rand(2)
  
    #number of iterations
    for i in range(maxiter):
        
        top = [0 for j in data]
        bottom = [0 for j in data]
        #we want to do these operations for each
        #point in the dataset
        for k in range(n):
      
            top[k] = data[k,:]/numpy.linalg.norm(data[k,:] - y, ord = 2)
            bottom[k] = 1/numpy.linalg.norm(data[k,:] - y, ord = 2 )
      
        y = numpy.sum(top, axis = 0)/numpy.sum(bottom)
    
  
  
    return(y)
  

  
