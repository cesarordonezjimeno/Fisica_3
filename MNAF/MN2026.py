# Example 1
def raiznsima(a, n, niter, tol):
    """
    Calcula una aproximación de la raíz n-ésima de a mediante la iteración
    Parámetros de entrada:
        a (float)    : radicando
        n  (int)     : índice del radical
        niter (int)  : número máximo de iteraciones
        tol (float)  : tolerancia; se para cuando |x(k+1) - x(k)| < tol
    Salida:
        xkm1  : aproximación de la raíz n-ésima de a
    """
    xk = a             # Valor inicial
    c1 = 1 - 1 / n     # Constantes
    c2 = a / n
    for i in range (niter):    # Bucle para calcular 
        xk1 = xk * c1 + c2 / xk ** (n - 1)
        if abs(xk1 - xk) < tol:
            break
        xk = xk1
    return xk1
print (raiznsima(5,2,100,1E-6))

#Example 2
def euclides(D, d):
    """
    Calcula una aproximación de la raíz n-ésima de a mediante la iteración
    Parámetros de entrada:
        D  (int)    : valor entero
        d  (int)    : valor entero 
    Salida:
        xkm1  : aproximación de la raíz n-ésima de a
    """
    c, r = divmod (D, d)
    while r != 0:
        D, d = d, r
        c, r = divmod (D, d)
        return d


