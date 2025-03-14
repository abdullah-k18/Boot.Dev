def new_collection(initial_docs):
    arr = initial_docs.copy()
    def copy(string):    
        arr.append(string)
        return arr
    return copy
