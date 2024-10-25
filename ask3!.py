a =input("Δώσε το a: ")
k =int(input("Δώσε το k: "))
a = list(a)
i = 0
c = len(a)//k
d = len(a)%k
L=[]
list(L)
if d!=0:
        c+=1
while i<c:
    b =''.join(a[i*k:((i+1)*k)])
    L.insert(i,b)
    i=i+1
L = map(int,L)
print(sum(L))



