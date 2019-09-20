class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        if len(items) == 0:
            return []
        
        stuScore = {}
        for pair in items:
            if pair[0] not in stuScore:
                stuScore[pair[0]] = [pair[1]]
                
            else:
                stuScore[pair[0]].append(pair[1])
                
                
        res = self.getAve(stuScore)
        return sorted(res, key =lambda x:x[0])  
    
    
    def getAve(self, stuScore):
        res = []
        for student in stuScore:
            if len(stuScore[student]) <= 5:
                res.append([student, self.ave(stuScore[student])])
            else:
                scoreList = stuScore[student]
                scoreList.sort(reverse = True)
                res.append([student, self.ave(scoreList[:5])])
                
        return res 
    
    def ave(self, nums):
        return sum(nums) // 5

            
        