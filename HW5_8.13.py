from numpy import empty,array,arange
from pylab import plot,show,title

G=6.6738e-11
M=1.9891e30
r0=4.4368e12
vy0=6.1218e3

t0 = 0.0
N =15000  
H = 7*24*3600 
t1= N*H   
delta = 1e3/365*7  

def f(r):
    [x,y] = r[0:2]
    [vx,vy] = r[2:4]
    ax=-G*M*x*(x**2+y**2)**(-1.5)
    ay=-G*M*y*(x**2+y**2)**(-1.5)
    return array([vx,vy,ax,ay],float)

tpoints = arange(t0,t1,H)
rpoints = []
r = array([r0,0,0,vy0],float)

# Do the "big steps" of size H
for t in tpoints:

    rpoints.append(r[0:2])

    # Do one modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    # The array R1 stores the first row of the
    # extrapolation table, which contains only the single
    # modified midpoint estimate of the solution at the
    # end of the interval
    R1 = empty([1,4],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))

    # Now increase n until the required accuracy is reached
    error = 2*delta
    while error>delta:

        n += 1
        h = H/n

        # Modified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)

        # Calculate extrapolation estimates.  Arrays R1 and R2
        # hold the two most recent lines of the table
        R2 = R1
        R1 = empty([n,4],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon
        error = (epsilon[0]**2+epsilon[1]**2)**0.5

    # Set r equal to the most accurate estimate we have,
    # before moving on to the next big step
    r = R1[n-1]

rr=array(rpoints)

plot(rr[:,0],rr[:,1])

title('Pluto')
show()
