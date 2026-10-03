
from src.parameters import C_M, G_NA, G_K, G_L, E_NA, E_K, E_L


def I_Na(V, m, h):
    return G_NA * (m ** 3) * h * (V - E_NA)


def I_K(V, n):
    return G_K * (n ** 4) * (V - E_K)


def I_leak(V):
    return G_L * (V - E_L)


def dVdt(V, m, h, n, I_ext):
    return (I_ext - I_Na(V, m, h) - I_K(V, n) - I_leak(V)) / C_M