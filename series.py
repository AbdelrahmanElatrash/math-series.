

def fibonacci(n):
    """
    Args:
        param1 : the int number
    Returns:
        retun a number debend a fibonacci Sequence
        The Fibonacci Sequence is the series of numbers:
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    
     Raises:
          any number less than 0 will return 0
    """
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
    """
    Args:
        param1 : the int number
    Returns:
        retun a number debend a  Lucas Numbers
        The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and
           2, 1, 3, 4, 7, 11, 18, 29, ...
     Raises:
          any negative  number not acsept 
    """
    if n <0 :
         return "no negative number"
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)
     




def sum_series(x,y=0,z=1):
    """
    Args:
        param1 : the int number
        param2 : int with defult value 0
        param3  : int with defult value 1
    
    Returns:
        if defulte 
            retun a number debend a fibonacci Sequence
            The Fibonacci Sequence is the series of numbers:
                0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

        Calling it with the optional arguments 2 and 1 will produce values from the lucas
            The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and
                2, 1, 3, 4, 7, 11, 18, 29, ...
     Raises:
          any negative  number not acsept 
    """
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
    

print(lucas(-2))
