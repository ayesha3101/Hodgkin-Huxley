"""
All voltages in mV, currents in uA/cm^2, conductances in mS/cm^2,
capacitance in uF/cm^2, time in ms.

Note on voltage convention: this file uses the modern convention where
V_rest = -65 mV (absolute membrane potential).
"""

# Membrane capacitance (uF/cm^2)
C_M = 1.0

# Maximum ionic conductances (mS/cm^2)
G_NA = 120.0   # sodium
G_K = 36.0     # potassium
G_L = 0.3      # leak

# Reversal potentials
E_NA = 50.0
E_K = -77.0
E_L = -54.387

# Resting membrane potential (mV)
V_REST = -65.0