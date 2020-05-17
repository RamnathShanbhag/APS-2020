#Bob has a strange counter. At the first second, it displays the number . Each second, the number displayed by the counter decrements by 1 until it 1 reaches .
#The counter counts down in cycles. In next second, the timer resets to 2*initial number for the prior cycle and continues counting down. 

def strangeCounter(t):
    r=3
    while(t>r):
        t-=r
        r*=2
    return(r-t+1)

t=int(input())
res=strangeCounter(t)
print(res)


