n = int(input().strip())
no_3=n//3
no_5=n//5
no_15=n//15
if n%3==0:
    no_3-=1
if n%5==0:
    no_5-=1
if n%15==0:
    no_15-=1
to_3=no_3*3*(no_3+1)//2
to_5=no_5*5*(no_5+1)//2
to_15=no_15*15*(no_15+1)//2
print(to_3+to_5-to_15)
