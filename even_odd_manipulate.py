# def even_odd_manipulate(n):
#     while n!=1:
#         if not n%2:
#             n=n//2

#         else:
#             n=3*n+1
#         print(n,end=" ")
            
# n=int(input())
# even_odd_manipulate(n)
def sum_divisors(n):
    sum = 0
    divisor=1
  # Return the sum of all divisors of n, not including n
    while divisor<n:
      if n%divisor==0:
        sum+=divisor
      divisor += 1
    return sum
print(sum_divisors(36))