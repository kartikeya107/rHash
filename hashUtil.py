class HashUtility:
    
    def __init__(self):
        self.alphabets = "acdegilmnoprstuw"

    def letterIndex(self, c):
        return self.alphabets.index(c)

    def hash(self, string):
        hashValue = 7
        try:
            for c in string:
                hashValue = hashValue*37 + self.letterIndex(c)
        except:
            hashValue = -1
            
        return hashValue

    def reverseHash(self, hashValue):
        rHash = ""
        try:
            while hashValue>0:
                d = hashValue%37
                rHash = rHash + self.alphabets[d]
                hashValue = hashValue/37

            rHash = rHash[len(rHash)-2::-1]

        except:
            rHash = -1

        return rHash
