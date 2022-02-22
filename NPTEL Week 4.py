#Nptel Week 4
#Merge Sort
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j < m+n : 
        if j==n:
            c.append(a[i])
            i+=1
        elif i==m:
            c.append(b[j])
            j+=1
        elif (a[i]<=b[j]):
            c.append(a[i])
            i+=1
        elif (a[i]>=b[j]):
            c.append(b[j])
            j+=1
    return(c)
print(merge([2,4,6],[1,3,5]))


#Recursive Merge Sort
def mergerec(a,l,r):
    if r-l<=1:
        return(a[l:r])
    if r-l>1:
        mid=(l+r)//2
        l=mergerec(a,l,mid)
        r=mergerec(a,mid,r)
    return(merge(l,r))
print(mergerec([2,4,6,1,3,5],0,6))
#T=2T(n/2)+n
#T=O(nlogn)

#Quick sort
def Quicksort(a,l,r):
    if r-l<=1:
        return()
    yellow=l+1
    for green in range(l+1,r):
        if a[green]<=a[l]:
            (a[yellow],a[green])=(a[green],a[yellow])
            yellow+=1
    (a[l],a[yellow-1])=(a[yellow-1],a[l])
    Quicksort(a, l, yellow-1)
    Quicksort(a, yellow, r)
    return(a)
print(Quicksort([2,4,6,1,3,5],0,6))
#Worst case T(n)=O(n^2)
#Average case T(n)=O(n logn)
