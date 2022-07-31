
m=9 ; n=27
dash=n//2 -1 # counter for '-'
sym =1 #counter for  '.|.'
name = "Devsnest!"
res =[]
name_dash = (n-len(name))//2
for i in range(m//2):
    res.extend(['-'*dash,'.|.'*sym,'-'*dash,"\n"])
    dash-=3
    sym+=2
res.extend(['-'*name_dash,name,'-'*name_dash,"\n"])
dash =3; 
sym-=2
for i in range(m//2):
    res.extend(['-'*dash,'.|.'*sym,'-'*dash,"\n"])
    dash+=3
    sym-=2
res = "".join(res)
print(res)