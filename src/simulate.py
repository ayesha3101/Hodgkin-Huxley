import numpy as np
from src import gating
from src.model import dVdt
from src.parameters import V_REST


def euler_step(V, m, h, n, I_ext, dt):
    dV = dVdt(V, m, h, n, I_ext)
    dm = gating.alpha_m(V) * (1 - m) - gating.beta_m(V) * m
    dh = gating.alpha_h(V) * (1 - h) - gating.beta_h(V) * h
    dn = gating.alpha_n(V) * (1 - n) - gating.beta_n(V) * n

    V_new = V + dt * dV
    m_new = m + dt * dm
    h_new = h + dt * dh
    n_new = n + dt * dn

    return V_new, m_new, h_new, n_new


def run_simulation(t_max, dt, stimulus_fn):
    t = np.arange(0, t_max, dt)
    n_steps = len(t)

    V = np.zeros(n_steps)
    m = np.zeros(n_steps)
    h = np.zeros(n_steps)
    n = np.zeros(n_steps)

    # Initial conditions: resting voltage, gates at their steady-state
    # values for that voltage (NOT 0 or 1).
    V[0] = V_REST
    m[0] = gating.steady_state(gating.alpha_m, gating.beta_m, V_REST)
    h[0] = gating.steady_state(gating.alpha_h, gating.beta_h, V_REST)
    n[0] = gating.steady_state(gating.alpha_n, gating.beta_n, V_REST)

    for i in range(1, n_steps):
        I_ext = stimulus_fn(t[i - 1])
        V[i], m[i], h[i], n[i] = euler_step(
            V[i - 1], m[i - 1], h[i - 1], n[i - 1], I_ext, dt
        )

    return t, V, m, h, n