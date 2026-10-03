import sys
import os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src import gating
from src.parameters import V_REST


def test_steady_state_at_rest():
    m0 = gating.steady_state(gating.alpha_m, gating.beta_m, V_REST)
    h0 = gating.steady_state(gating.alpha_h, gating.beta_h, V_REST)
    n0 = gating.steady_state(gating.alpha_n, gating.beta_n, V_REST)

    assert 0.03 < m0 < 0.08, f"m0={m0} outside expected range"
    assert 0.5 < h0 < 0.7, f"h0={h0} outside expected range"
    assert 0.25 < n0 < 0.4, f"n0={n0} outside expected range"
    print(f"OK: m0={m0:.4f}, h0={h0:.4f}, n0={n0:.4f}")


def test_no_singularity_crash():
    """alpha_m and alpha_n must not raise/NaN at their singular voltages
    (V=-40 for alpha_m, V=-55 for alpha_n)."""

    for V in [-40.0, -55.0]:
        am = gating.alpha_m(V)
        an = gating.alpha_n(V)
        assert np.isfinite(am), f"alpha_m({V}) is not finite: {am}"
        assert np.isfinite(an), f"alpha_n({V}) is not finite: {an}"
    print("OK: no singularity crashes at V=-40, V=-55")


if __name__ == "__main__":
    test_steady_state_at_rest()
    test_no_singularity_crash()
    print("All checks passed.")