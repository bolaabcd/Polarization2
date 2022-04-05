import numpy as np

# f(x,k) part of the belief-update functions 

def line_update(x : float, k : float):
    return x*k

def modulus_update(x : float, k : float):
    k=0.5*k+0.5 # g(k)
    
    sigx = None
    if type(x) is float: 
        sigx = -1
        if x >= 0:
            sigx = 1
    else:
        sigx = np.copy(x)
        sigx[sigx >= 0] = 1
        sigx[sigx <  0] = -1

    y = sigx*(-abs(abs(x)-k)+k)
    return y

def non_norm_quadratic_update(x : float, k : float):
    k=k+1 # g(k)
    y = -x*(abs(x)-k)
    return y

def quadratic_update(x : float, k : float):
    return non_norm_quadratic_update(x, k)/2

def non_norm_cubic_update(x : float, k : float):
    k=k+1 # g(k)
    y = -x*(x-k)*(x+k)
    return y

def cubic_update(x : float, k : float):
    return non_norm_cubic_update(x, k)/4

def non_norm_interpolated_update(x : float, k : float):
    y = ((k+1)*(k-1)*x**3+(-k**2+k+1)*x)
    return y

def interpolated_update(x : float, k : float):
    return non_norm_cubic_update(x, k)/1.5

def invalid_cubic(x : float, k: float):
    # sigx = None
    # if type(x) is float: 
    #     sigx = -1
    #     if x >= 0:
    #         sigx = 1
    # else:
    #     sigx = np.copy(x)
    #     sigx[sigx >= 0] = 1
    #     sigx[sigx <  0] = -1
    return x**3 #* sigx

def bad_exponential(x: float, k:float):
    sigx = None
    if type(x) is float: 
        sigx = -1
        if x >= 0:
            sigx = 1
    else:
        sigx = np.copy(x)
        sigx[sigx >= 0] = 1
        sigx[sigx <  0] = -1
    return np.e**(-np.abs(x)**(-1.0))*sigx