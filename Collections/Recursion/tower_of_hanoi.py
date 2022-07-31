def tower_of_hanoi(disk,src,dest,helper):
    if disk ==0:
        return
    
    tower_of_hanoi(disk-1,src,helper,dest)
    print("Move from "+src+"--->"+dest)
    tower_of_hanoi(disk-1,helper,dest,src)

    


tower_of_hanoi(3,'A','C','B')