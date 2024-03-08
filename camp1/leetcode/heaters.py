class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def isvalid(val):
            house = 0
            heater = 0
            while house<len(houses) and heater<len(heaters):
                if abs(houses[house]-heaters[heater])<=val:
                    house+=1
                else:
                    heater+=1
            
            return heater < len(heaters)
                
        l = 0
        r = max(abs(houses[0]-heaters[-1]), abs(houses[-1]-heaters[0]))
        # r = 100
        ans = 0

        while l<=r:
            mid = (l+r)//2
            print(mid, isvalid(mid))
            if isvalid(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        
        return ans


            


