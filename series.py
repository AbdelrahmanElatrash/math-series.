#  let arr=[];
#     arr.push(0,1);
#     if(n==0){
#         arr=[0];
#     }else if(n==1){
#         arr=[0,1]
#     }else{
#         while (arr[arr.length-1]<n){
#             arr.push(arr[arr.length-2]+arr[arr.length-1])
#         }
#         if(arr[arr.length-1]>=n){
#             arr.pop();
#         }
#     }
    
    
#     return arr[arr.length-1] ;
   
# }

def fibonacci(n):
    
    arr=[0,1]
    if n==0:
       arr=[0]
    elif n==1:
        arr=[0,1]
    else:
        while arr[-1]<n:
            
            arr.append(arr[-2] + arr[-1])

        if  arr[-1] >=n:
                    arr.pop()

    return arr[-1]




def lucas(n):
     
    if n == 0:
        return 2
    if n == 1:
        return 1
   
    return lucas(n - 1) + lucas(n - 2)
     




def sum_series(x,y=0,z=1):
    if y==0 and z==1:
        return fibonacci(x)
    elif y==2 and z==1:
         return lucas(x)
    elif x==y :
         return y 
    elif x==z:
         return z
    else :
         return sum_series(x-1,y,z)+ sum_series(x-2,y,z)