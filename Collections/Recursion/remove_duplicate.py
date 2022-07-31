def remove_duplicate(string):

    if len(string)==1:
        return string

    res = remove_duplicate(string[1:])

  
    if  string[0] != res[0]:
        return string[0]+res
    else: 
        return res

print(remove_duplicate("dsddas"))