import numpy as np

# f(x,k) part of the belief-update functions 

def line_update(x : float, k : float) -> float: # also works with numpy array.
    y = x*k
    return y

def modulus_update(x : float, k : float) -> float: # also works with numpy array.
    g_k = 0.5*k + 0.5
    
    sigx = None
    if type(x) is float: 
        sigx = -1
        if x >= 0:
            sigx = 1
    else:
        sigx = np.copy(x)
        sigx[sigx >= 0] = 1
        sigx[sigx <  0] = -1

    y = sigx*(-abs(abs(x)-g_k)+g_k)
    return y

def non_norm_quadratic_update(x : float, k : float): # also works with numpy array.
    g_k = k + 1 
    y = -x*(abs(x)-g_k)
    return y

def quadratic_update(x : float, k : float): # also works with numpy array.
    return non_norm_quadratic_update(x, k)/2

def non_norm_cubic_update(x : float, k : float): # also works with numpy array.
    g_k = k + 1
    y = -x*(x - g_k)*(x + g_k)
    return y

def cubic_update(x : float, k : float): # also works with numpy array.
    return non_norm_cubic_update(x, k)/4

def non_norm_interpolated_update(x : float, k : float): # also works with numpy array.
    y = (k + 1)*(k - 1)*x**3 + (-k**2 + k + 1)*x
    return y

def interpolated_update(x : float, k : float): # also works with numpy array.
    return non_norm_interpolated_update(x, k)/1.5

def slow_cubic(x : float, k: float): # also works with numpy array.
    y = k*x**3
    return y

def bad_exponential(x: float, k:float): # also works with numpy array.
    sigx = None
    if type(x) is float: 
        sigx = -1
        if x >= 0:
            sigx = 1
    else:
        sigx = np.copy(x)
        sigx[sigx >= 0] = 1
        sigx[sigx <  0] = -1
    y = np.e**(-np.abs(x)**(-1.0))*sigx
    return y

def sig(x: float, k:float): # also works with numpy array.
    sigx = None
    if type(x) is float: 
        sigx = -1
        if x > 0:
            sigx = 1
        elif x == 0:
            sigx = 0
    else:
        sigx = np.copy(x)
        sigx[sigx > 0] = 1
        sigx[sigx <  0] = -1
        sigx[sigx == 0] = 0
    y = sigx#*k
    return y
