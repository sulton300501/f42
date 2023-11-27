bosh = [2,1]
x=2


bosh.sort()
arr = []


for i in range(len(bosh)-2):
    if bosh[i]==x:
        son = bosh[i]
        bosh[i]=bosh[i+1]
        bosh[i+1]=son

print(bosh)
