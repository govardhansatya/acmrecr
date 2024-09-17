 #x-finding difference between sum of squares and square of sum of first 100 natural numbers
a=sum([i*i for i in range(100)])
b=sum([ior i in range(100)])  
c=b*b
if a>c:
    x=a-c
    print(x)  
else:
    x=c-a 
    print(x)
