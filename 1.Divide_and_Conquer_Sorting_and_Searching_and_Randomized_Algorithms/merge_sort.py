
def split(x:list)->tuple:
    n = int(len(x)/2)
    
    return x[:n], x[n:]

def sort(x:list)->list:
    if len(x) == 1:
        return x
        if x[0]>x[1]:
            return [x[1], x[0]]
        else:
            return x
    else:
        pass

def merge_sort(x:list):
    y, z = split(x)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if len(x)>1 and len(y)>1:
        pass
    else:
        if len(x)==1:
            pass
        elif len(y)