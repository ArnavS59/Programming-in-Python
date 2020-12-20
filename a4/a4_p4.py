# a4_p4

totalreads,count,totalsum=0,0,0
while True:
    inp=int(input())
    if inp==-9 or totalreads==10:
        break
    else:
        totalsum+=inp
        count+=1
    totalreads+=1

print("The average is" ,totalsum//count)
