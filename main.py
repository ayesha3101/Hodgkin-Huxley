from src.simulate import run_simulation
from src.plotting import plot_voltage_trace, plot_gating_variables


def stimulus_fn(t):
    """Current pulse: 10 uA/cm^2 between t=5ms and t=6ms, else 0."""
    return 10.0 if 5.0 <= t <= 6.0 else 0.0


if __name__ == "__main__":
    t, V, m, h, n = run_simulation(t_max=50, dt=0.01, stimulus_fn=stimulus_fn)
    plot_voltage_trace(t, V, save_path="voltage_trace.png")
    plot_gating_variables(t, m, h, n, V=V, save_path="gating_variables.png")
    print(f"Peak voltage reached: {V.max():.2f} mV")
    print(f"Spike occurred: {'Yes' if V.max() > 0 else 'No'}")