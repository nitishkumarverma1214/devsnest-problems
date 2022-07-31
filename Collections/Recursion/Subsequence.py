def Subsequence(string,ans):

    if len(string)==0:
        print(ans)
        return ""
    
    Subsequence(string[1:],ans)
    Subsequence(string[1:],ans+string[0])
   


Subsequence("abc","")