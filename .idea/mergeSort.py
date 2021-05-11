
def mergeTwo(ArrA,ArrB):
    ABJoin = [0]*(len(ArrA)+len(ArrB))

    a, b = 0,0

    while a<len(ArrA) and b<len(ArrB):
        if ArrA[i]<ArrB[b]:
            ABJoin[a+b]=ArrA[a]
            a+=1
        else:
            ABJoin[a+b]=ArrB[a]
            b+=1


    while a<len(ArrA):
        ABJoin[a+b]=ArrA[a]
        a+=1

    while b < len(ArrB):
        ABJoin[a+b]=ArrB[b]
        b+=1



def mergeS(array,left,right):

    if left<right:
        mid = left + (right-left)/2
        ArrA = mergeS(array,left,mid)
        ArrB = mergeS(array,mid+1,right)
        return mergeTwo(ArrA,ArrB)
    elif left==right:
        return [array[left]]







if __name__ == '__main__':
    print("This is the main page---")
    arr = [34,12,56,1,4,34]
    print(mergeS(arr,0,len(arr)-1))