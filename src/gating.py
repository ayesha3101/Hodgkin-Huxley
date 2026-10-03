
import numpy as np


def alpha_m(V):
    """Opening rate for the Na+ activation gate m."""
    # Guard the V = -40 singularity (denominator -> 0) with a tiny epsilon
    denom = 1 - np.exp(-(V + 40.0) / 10.0)
    denom = np.where(np.abs(denom) < 1e-7, 1e-7, denom)
    return 0.1 * (V + 40.0) / denom


def beta_m(V):
    """Closing rate for the Na+ activation gate m."""
    return 4.0 * np.exp(-(V + 65.0) / 18.0)


def alpha_h(V):
    """Opening rate for the Na+ inactivation gate h."""
    return 0.07 * np.exp(-(V + 65.0) / 20.0)


def beta_h(V):
    """Closing rate for the Na+ inactivation gate h."""
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


def alpha_n(V):
    """Opening rate for the K+ activation gate n."""
    denom = 1 - np.exp(-(V + 55.0) / 10.0)
    denom = np.where(np.abs(denom) < 1e-7, 1e-7, denom)
    return 0.01 * (V + 55.0) / denom


def beta_n(V):
    """Closing rate for the K+ activation gate n."""
    return 0.125 * np.exp(-(V + 65.0) / 80.0)


def steady_state(alpha_fn, beta_fn, V):
    a = alpha_fn(V)
    b = beta_fn(V)
    return a / (a + b)