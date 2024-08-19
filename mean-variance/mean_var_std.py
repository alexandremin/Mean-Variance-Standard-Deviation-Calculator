import numpy as np



def calculate(list):
    
    intlist = np.array(list)
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    my_list = intlist.reshape(3,3)
   
    mean_axis1 = np.mean(my_list, axis=0).tolist()
    mean_axis2 = np.mean(my_list, axis=1).tolist()
    mean_flattened = intlist.mean().tolist()
    
    var_axis1 = np.var(my_list, axis=0).tolist()
    var_axis2 = np.var(my_list, axis=1).tolist()
    var_flattened = intlist.var().tolist()
    
    std_axis1 = np.std(my_list, axis=0).tolist()
    std_axis2 = np.std(my_list, axis=1).tolist()
    std_flattened = intlist.std().tolist() 
    
    max_axis1 = np.max(my_list, axis=0).tolist()
    max_axis2 = np.max(my_list, axis=1).tolist()
    max_flattened = intlist.max().tolist()
    
    min_axis1 = np.min(my_list, axis=0).tolist()
    min_axis2 = np.min(my_list, axis=1).tolist()
    min_flattened = intlist.min().tolist()
    
    sum_axis1 = np.sum(my_list, axis=0).tolist()
    sum_axis2 = np.sum(my_list, axis=1).tolist()
    sum_flattened = intlist.sum().tolist()
    
    calculations = {
  'mean': [mean_axis1, mean_axis2, mean_flattened],
  'variance': [var_axis1, var_axis2, var_flattened],
  'standard deviation': [std_axis1, std_axis2, std_flattened],
  'max': [max_axis1, max_axis2, max_flattened],
  'min': [min_axis1, min_axis2, min_flattened],
  'sum': [sum_axis1, sum_axis2, sum_flattened]
}
    
    
    return calculations