for a in range(0,1000):
  for b in range(0,1000):
    for c in range(0,1000):
      if a<b and b<c and a+b+c==1000 and a*a+b*b==c*c:
        print(a)
        print(b)
        print(c)
        print(a*b*c)