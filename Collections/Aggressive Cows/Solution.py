from aggressiveCowSol import aggressiveCows
if __name__ == '__main__':
    fileobj = open("Collections\Aggressive Cows\input.txt",'r')

    tc = int(fileobj.readline())
    for t in range(tc):
        noOfStalls, noOfCows = map(int,fileobj.readline().split())
        #taking input for no of cow
        stalls = list(map(int,fileobj.readline().split()))
        #sorting the stalls
        stalls.sort()

        print(aggressiveCows(stalls,noOfCows))

