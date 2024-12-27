#Staircase Problem
def count_ways(n):
    if(n==0 or n==1):
        return 1
    table = []
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input("Enter the number of steps: "))
print("Number of ways:",count_ways(n))
