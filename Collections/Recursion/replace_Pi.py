def replace_Pi_value(string):
    if not string:
        return
    
    if string[:2] =='pi':
        print(3.14,end="")
        replace_Pi_value(string[2:])
    else:
        print(string[0],end="")
        replace_Pi_value(string[1:])

   
   




string="pipxpppiiixxxpi"
replace_Pi_value(string)