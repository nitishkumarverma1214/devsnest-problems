def decreasing_order(n):
    if not n:
        return
    print(n)
    decreasing_order(n-1)
    
def increasing_order(n):
    if n==0:
        return
    increasing_order(n-1)
    print(n)

decreasing_order(10)
increasing_order(10)