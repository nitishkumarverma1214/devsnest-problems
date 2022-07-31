class Solution:
    def __init__(self):
        self.memo = {}


    def correctTime(self,time,interval):
        if time in self.memo:
            return self.memo[time]
        if time ==0:
            return []
        if time <0:
            return None
        
        leasttime = None
        for minute in interval:
            way = self.correctTime(time-minute,interval)
            if way!=None:
                path = way + [minute]
                if leasttime == None or len(leasttime) > len(path):
                    leasttime = path
        self.memo[time] = leasttime
        return leasttime

    def convertTime(self, current: str, correct: str) -> int:
        cur_hour,cur_min = map(int,current.split(":"))
        cor_hour,cor_min = map(int,correct.split(":"))
        minutes =(cor_hour-cur_hour)*60 +(cor_min -cur_min)
        
        res = self.correctTime(minutes,[60,15,5,1])
        return res



res = Solution().convertTime(current = "02:30", correct = "04:35")
print(res)