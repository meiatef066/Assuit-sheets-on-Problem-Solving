TO_check_if_print=0
def fun(n,i):
  global TO_check_if_print # he is the global var i`m not decleae new var in fun 
  if(i==n+1):
    return
  if not i%2:
   print(i)
   TO_check_if_print=1
  fun(n,i+1)
n= int(input())
# for i in range(1,n+1):
#   print(i)
fun(n,1)
if TO_check_if_print==0:
  print (-1)
