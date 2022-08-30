from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       
        res =[]
        cur=[]
        def generate(opening,closing):
            if opening==closing and closing+opening == 2*n:
                res.append(''.join(cur))
                return
            
            if closing>opening or opening>n:
                return 
            
            
            for ch in ['(',')']:
                if ch=='(' :
                    cur.append('(')
                    generate(opening+1,closing)
                    cur.pop()
                else:
                    cur.append(')')
                    generate(opening,closing+1)
                    cur.pop()


        generate( opening=0,closing = 0)
        return res

def main():
    n = 2
    print(Solution().generateParenthesis(n))   
if __name__ == '__main__':
    main()