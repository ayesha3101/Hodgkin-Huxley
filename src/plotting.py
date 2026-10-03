import matplotlib.pyplot as plt


def plot_voltage_trace(t, V, save_path=None):
    """
    Plot membrane voltage V against time t.
       
    """
    plt.figure(figsize=(9, 4))
    plt.plot(t, V, color="tab:blue", linewidth=1.5)
    plt.xlabel("Time (ms)")
    plt.ylabel("Membrane potential (mV)")
    plt.title("Hodgkin-Huxley: Membrane Voltage")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_gating_variables(t, m, h, n, V=None, save_path=None):
    if V is not None:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
        ax1.plot(t, V, color="tab:blue", linewidth=1.5)
        ax1.set_ylabel("Membrane potential (mV)")
        ax1.set_title("Hodgkin-Huxley: Voltage and Gating Variables")
        ax1.grid(alpha=0.3)
    else:
        fig, ax2 = plt.subplots(figsize=(9, 4))

    ax2.plot(t, m, label="m (Na+ activation)", color="tab:orange")
    ax2.plot(t, h, label="h (Na+ inactivation)", color="tab:green")
    ax2.plot(t, n, label="n (K+ activation)", color="tab:red")
    ax2.set_xlabel("Time (ms)")
    ax2.set_ylabel("Gating variable (0-1)")
    ax2.legend(loc="upper right")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()