l = ['n','5','f','a']
def ReverseArray (arr):
 i=0
 a=0
 b=0

 while(i<len(arr)/2):
  a=arr[0+i]
  b=arr[len(arr)-1-i]
  arr[0+i]=b
  arr[len(arr)-i-1]=a
  i+=1

 print(arr)

ReverseArray(l)




 

