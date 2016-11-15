import sys
from hashUtil import HashUtility

args = sys.argv
if(len(args)>1):
    hashValue = int(args[1])
    hashUtil = HashUtility()
    print(hashUtil.reverseHash(hashValue))
else:
    print("Please input a hash value")

