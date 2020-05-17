#A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

x=int(input()) #testcases
for i in range(x):
    [n,m,s]=[int(j) for j in input().split()]
    val= (n+m+s-1)%n
    if val==0:
        print(n)
    else:
        print(val)
