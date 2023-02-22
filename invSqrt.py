# http://www.lomont.org/papers/2003/InvSqrt.pdf



# float InvSqrt(float x)
# {
# float xhalf = 0.5f*x;
# int i = *(int*)&x; // get bits for floating value
# i = 0x5f3759df - (i>>1); // gives initial guess y0
# x = *(float*)&i; // convert bits back to float
# x = x*(1.5f-xhalf*x*x); // Newton step, repeating increases accuracy
# return x;
# }
def invSqrt(x):
    xHalf = 0.5 * x
    