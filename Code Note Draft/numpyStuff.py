import numpy as np
#Numpy works like a more efficient array library, for the most part
#a Numpy array differs in functionality to a basic python array
parray = np.array([[1],[2],[3]]) #there are also various attributes to each array beyond type
parray.ndim #the dimension of an array, i.e. number of subarrays in its array
parray.shape #the shape of each dimension, i.e. number of elements in each subarray
parray.size #the total size of array, i.e. combinatoric amount of elements (product of shape array)
parray.dtype #the type of all elements in the array

#there are also some performance oriented attributes you can look at
parray.itemsize #details the number of bytes of a single item in the array
parray.nbytes #details the total number of bytes used for the array (generally expected to be equal to itemsize*size)

#array indexing and slicing works the same as regular python
parray[0] #will output array([1])
parray[-1] # will output array([3])
parray[0:-1] #will ouput array([[1],[2]])

#multiple dimension arrays work similarly as well
parray[0,1] #will spit out an error! there is no second element in the first dimension
parray[0:2,0] #will output array([1,2])


#now for the matlab-like methods!

#when you want to reshape an array and copy it
p2array = parray.copy()
p2array = p2array.reshape(1,3) #converts our old array (which resembled a column vector), into a row vector, array([1,2,3])

#concatenation is also supported, however both arrays must be the same type
np.concatenate([parray,parray])  # [[1],[2],[3],[1],[2],[3]] 
np.concatenate([p2array,p2array])# [1,2,3,1,2,3]
#you can even concatenate along an arbitrary axis, same 0-base index
np.concatenate([parray,parray],axis=1)# array([[1,1],[2,2],[3,3]])
#however there's the clearer functions of 
#np.vstack, np.hstack,and np.dstack which act as vertical, horizontal, and depth stacking respectively (axis 0,1,2 concatenation)

#splitting arrays works as follows
#for a given array and a set of n split points, np.split() will output n+1 arrays cut at the given points
np.split(p2array,[1,2])#[1] [2] [3] 
#np.split also has np.hsplit,np.vsplit, and np.dstack which act like the stack equivalents

#generating arrays of specific properties
np.zeros ((3,4)) #3 arrays with 4 zeroes each
np.ones((3,3,3)) #3 arrays with 3 subarrays with 3 ones each
np.empty((5)) #5 items in an array, np.empty has unpredictable behavior (besides really small numbers appearing)
np.arange(0,10,1) #creates a numpy array with the given range, super useful with reshape
np.linspace(0,np.pi+np.pi,100)#cleanly goes between two ranges, behavior is especially preferred vs. arange for irrationals/not-nice-floats



