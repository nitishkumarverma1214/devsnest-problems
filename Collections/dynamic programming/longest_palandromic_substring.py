class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        # initialize diagonal 0 with 1
        mat = [[ 1 if j==i else 0 for j in range(n)]for i in range(n) ]
        
        start =0;end =1
        daigonal = 1
        while(daigonal <n):
            i ,j = 0,daigonal
            while j<n:
                if daigonal ==1 and s[i]==s[j]:
                    mat[i][j] = 1
                    start,end = i,j+1
                   
                elif s[i] == s[j] and mat[i+1][j-1]:
                    mat[i][j] = 1
                    start,end = i,j+1
                        
                
                i+=1
                j+=1

            daigonal +=1


       
        return s[start:end]


lps = Solution().longestPalindrome("jfbnhnjamsfsbsslcaaivnzryrrkcqmektqjnymeifxvvskicpxxrztysetlpucxfqccmeyptxxziqhacxatxjynmbblssyaxvcmbtyrtqfwxrwsgfrinfkczktytwglbrskeogamecvihkywnljnqfmrrnqcvopcoyroncwzhdqzvwdbtjmcocwljjvipabzorajqgiabqjeyasbrjvyjtdvgupqtmydfgdczaodyokxxarfboxifcltizhhntciffijclljvdfgpsojwmupgtrbquuzjdefnmxtcaborisjcsavucmuovlksonzvmmuvujzirioxdcadeioravjoyxhrqevfwmxacimtvbmfweqpvfijyuqrjfgejrnlmhvbbmbvviilsothgvaqgqtllonrqbsltwpikfrckdhttxzmbqmbhbjjwfddnrfwtafgjtuqyatkpcavokouftqwdzfclkckwzfwlozksgkrcyimvdhfrzlqqxnfhjkwfiewwqmbfyjdjematsvusmqxzwfyukqwlfzzyzlkqvgmq")
print(lps)

lps = Solution().longestPalindrome("j")
print(lps)