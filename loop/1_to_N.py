# 
def fun(n,i):
  if(i==n+1):
    return
  print(i)
  fun(n,i+1)
n= int(input())
# for i in range(1,n+1):
#   print(i)
fun(n,1)
