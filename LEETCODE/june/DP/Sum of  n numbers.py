
'''
dp=[0]*(n)
dp[0]=0
for i in range(1,n):
    dp[i]=dp[i-1]+i
return dp[n]
'''