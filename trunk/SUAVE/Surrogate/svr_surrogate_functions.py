# svr_surrogate_functions.py
#
# Created:  May 2016, M. Vegh
# Modified:


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------


from SUAVE.Core import Data
from sklearn import svm
from Surrogate_Problem import Surrogate_Problem

import numpy as np
import time


def build_svr_models(obj_values, inputs, constraints, kernel = 'rbf', C = 1E5, epsilon =.01):
    #now build surrogates based on these
    t1=time.time()

    # start a training data object
    clf             = svm.SVR(kernel=kernel, C=C, epsilon = epsilon)
    obj_surrogate   = clf.fit(inputs, obj_values) 
    constraints_surrogates = []
   
    #now do this for every constraint
    
    for j in range(len(constraints[0,:])):
        clf                  = svm.SVR(kernel=kernel, C=C, epsilon = epsilon)
        constraint_surrogate = clf.fit(inputs, constraints[:,j]) 
        constraints_surrogates.append(constraint_surrogate)
     
    t2=time.time()
    print 'time to set up = ', t2-t1
    surrogate_function                        = Surrogate_Problem()
    surrogate_function.obj_surrogate          = obj_surrogate
    surrogate_function.constraints_surrogates = constraints_surrogates
    
    return obj_surrogate, constraints_surrogates, surrogate_function    
    
def check_svr_accuracy(x, data_inputs, data_outputs): #set up so you can frame as an optimization problem
    
    #use log base 10 inputs to find parameters
    Cval= 10**x[0]
    eps = 10**x[1]
    #prevent negative values

    y = []
    for j in range (len(data_outputs[0,:])): #loop over data
        clf         = svm.SVR(C=Cval,  epsilon = eps)
        y_surrogate = clf.fit(data_inputs[0:-1,:], data_outputs[0:-1,j]) #leave out last data point for surrogate fit
        y.append(y_surrogate.predict(data_inputs[-1,:])[0])
    y = np.array(y)
    y_real = data_outputs[-1,:]
   
    diff = (y_real-y)/y_real
    output= np.linalg.norm(diff)
    return output
        

