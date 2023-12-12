class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.live= timeToLive
        self.expire = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expire[tokenId] = currentTime+self.live
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.expire and self.expire[tokenId] > currentTime:
            self.expire[tokenId] = currentTime+self.live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for val in self.expire.values():
            if val>currentTime:
                count+=1
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)