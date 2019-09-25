# seq: sequence in which value is to be searched
# v: value to search
# l: starting index of slice 
# r: ending index of slice 

def bsearch(seq,v,l,r):
    # empty slice
    if(r-l==0):
        return False
    
    mid=(l+r)//2

    if(v==seq[mid]):
        return True
    #left half
    if(v<seq[mid]):
        return (bsearch(seq,v,l,mid))
    #right half
    else:
        return (bsearch(seq,v,mid+1,r))

#----main----
print('Enter sequence: ')
arr=[int(x) for x in input().split()]
val=int(input('Enter value to search: '))
print(bsearch(arr,val,0,len(arr)))