
#first approach
# def gcd(m,n):
#     #assuming m>=n
#     if m<n:
#         (m,n) = (n,m)
#     if (m%n)==0:
#         return n
#     else:
#         diff = m-n
#         return gcd(max(n,diff),min(n,diff))

# improvement
# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     while(m%n)!=0:
#         diff = m-n
#         (m,n)=(max(n,diff),min(n,diff))

#final improved version
def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    if (m%n)==0:
        return n
    else:
        return gcd(n,m%n)

#main
a,b=input("Enter two numbers to calculate GCD: ").split()
a=int(a)
b=int(b)
print('GCD: ',gcd(a,b))