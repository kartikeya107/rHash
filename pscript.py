from hashUtil import HashUtility

hashUtil = HashUtility()
while(1):
    string = raw_input("Enter a string to get hash:")
    hashValue = hashUtil.hash(string)
    if(hashValue == -1):
        print "Invalid string"
    else:
        print hashValue
    print ;
    string = input("Enter a hash to get the string back:")
    reverseHash = hashUtil.reverseHash(string);
    if(reverseHash == -1):
        print "Invalid string"
    else:
        print reverseHash
    
