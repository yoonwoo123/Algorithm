# memoization , 재귀x
def fibo(a):
   fi = [0,1]
   for i in range(2, n+1):
       fi.append(fi[i-2] + fi[i-1])

   return fi[n]

n = int(input())

print(fibo(n))