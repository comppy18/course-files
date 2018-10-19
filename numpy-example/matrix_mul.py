import numpy, time
n=1024
a=numpy.ones((n,n))
b=numpy.ones((n,n))
c=numpy.zeros((n,n))
t1=time.clock()
#for i in range(n):
#   for j in range(n):
#       for k in range(n):
#           c[i,j]+=a[i,k]*b[k,j]
t2=time.clock()
#print("Loop timing",t2-t1 )
c = numpy.dot(a, b)
t3=time.clock()
print("Loop timing",t3-t2 )
