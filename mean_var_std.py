import numpy as np

def calculate(list):
    # If a list containing less than 9 elements is passed into the function, 
    # it should raise a ValueError exception with the message: "List must contain nine numbers." 
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    newlist = np.array(list).reshape(3, 3)
    calculations = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
    }

    calculations['mean'].append(np.mean(newlist, axis=0).tolist())
    calculations['mean'].append(np.mean(newlist, axis=1).tolist())
    calculations['mean'].append(np.mean(newlist))

    calculations['variance'].append(np.var(newlist, axis=0).tolist())
    calculations['variance'].append(np.var(newlist, axis=1).tolist())
    calculations['variance'].append(np.var(newlist))

    calculations['standard deviation'].append(np.std(newlist, axis=0).tolist())
    calculations['standard deviation'].append(np.std(newlist, axis=1).tolist())
    calculations['standard deviation'].append(np.std(newlist))
    
    calculations['max'].append(np.max(newlist, axis=0).tolist())
    calculations['max'].append(np.max(newlist, axis=1).tolist())
    calculations['max'].append(np.max(newlist))

    calculations['min'].append(np.min(newlist, axis=0).tolist())
    calculations['min'].append(np.min(newlist, axis=1).tolist())
    calculations['min'].append(np.min(newlist))
    
    calculations['sum'].append(np.sum(newlist, axis=0).tolist())
    calculations['sum'].append(np.sum(newlist, axis=1).tolist())
    calculations['sum'].append(np.sum(newlist))

    return calculations