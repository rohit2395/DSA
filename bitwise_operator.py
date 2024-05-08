class CountSetBits:
    tbl = [0] * 256
    def __init__(self):
        CountSetBits.tbl[0]=0
        for i in range (1,256,1):
            CountSetBits.tbl[i] = CountSetBits.tbl[i&(i-1)]+1 #Brian Kerningham Algorithm
            print(str(i) + " | " + str(CountSetBits.tbl[i]))

    def count(self,N):
        return CountSetBits.tbl[N&255] + \
                CountSetBits.tbl[(N>>8)&255] + \
                CountSetBits.tbl[(N>>16)&255] + \
                CountSetBits.tbl[N>>24]


a=True
b=False
x=1 #01
y=2 #10
#x&y 00
print(x|y)
print(a&b)
if a | b:
    print(True)
else:
    print(False)

#Find all the set bits in a number
countSetBits=CountSetBits()
print("No of set bits : " + str(countSetBits.count(17)))