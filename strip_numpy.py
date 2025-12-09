def strip_numpy_types(obj):
    """
    Converts NumPy data types to Python native types.
    """
    import numpy as np # Assumed import for np types

    # Case 1: NumPy Array
    if isinstance(obj, np.ndarray):
        if obj.size == 1:
            # A size-1 array is converted to a scalar using .item()
            return obj.item()
        else:
            # Multi-dimensional arrays are converted to a native list using tolist()
            return obj.tolist()
    
    # Case 2: NumPy Scalar
    elif isinstance(obj, (np.integer, np.floating, np.bool_)):
        # NumPy scalars (int, float, bool) are converted to native types using .item()
        return obj.item()
    
    # Case 3: List (Recursive Processing)
    elif isinstance(obj, list):
        # Recursively process each item in the list
        return [strip_numpy_types(item) for item in obj]
    
    # Case 4: Tuple (Recursive Processing)
    elif isinstance(obj, tuple):
        # Recursively process each item and return a new tuple
        return tuple(strip_numpy_types(item) for item in obj)
    
    # Case 5: Dictionary (Recursive Processing)
    elif isinstance(obj, dict):
        # Recursively process both keys and values in the dictionary
        return {key: strip_numpy_types(value) for key, value in obj.items()}
    
    # Case 6: Other Python Native Types
    else:
        # Other Python native types are returned as is
        return obj
