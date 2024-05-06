import numpy as np

def calculate(list):
    # If a list containing less than 9 elements is passed into the function, 
    # it should raise a ValueError exception with the message: "List must contain nine numbers." 
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    newlist = np.array(list).reshape(3, 3)
    calculations = {}
    operation = {
    'mean': 'mean',
    'variance': 'var',
    'standard deviation': 'std',
    'max': 'max',
    'min': 'min', 
    'sum': 'sum'
    }
    
    # The getattr() method returns the value of the named attribute of an object
    for key, method in operation.items():
        calculations[key] = [
        getattr(newlist, method)(axis=0).tolist(),
        getattr(newlist, method)(axis=1).tolist(),
        getattr(newlist, method)()
        ]

    return calculations