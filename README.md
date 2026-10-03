# Hodgkin-Huxley Neuron Simulation

A from-scratch implementation of the **Hodgkin-Huxley model**, a mathematical model that explains how a biological neuron produces an action potential (spike).

## The concept

A neuron receives signals and changes its membrane voltage. When the voltage reaches a certain level, ion channels open and close, allowing **sodium (Na⁺)** and **potassium (K⁺)** ions to move across the membrane. This produces the characteristic spike of a neuron.

The Hodgkin-Huxley model represents this process using four variables:

* `V` - membrane voltage
* `m` - sodium activation
* `h` - sodium inactivation
* `n` - potassium activation

These variables change over time according to a set of differential equations.

This is also where the connection to **AI** comes in. Artificial neural networks were inspired by biological neurons, although artificial neurons are much simpler. A typical artificial neuron takes inputs, processes them, and produces an output, while the Hodgkin-Huxley model describes the actual biological processes that cause a neuron to fire.

This makes the project a small bridge between **neuroscience, computational modeling, and AI**, and provides a foundation for understanding **spiking neural networks**, where information is represented using neuron-like spikes.

## What this project does

The simulation:

1. Starts the neuron at its resting state.
2. Applies an external current.
3. Calculates sodium, potassium, and leak currents.
4. Updates `V`, `m`, `h`, and `n` over time.
5. Plots the neuron's voltage and gating variables.

The model is a **single-compartment (point neuron)**, so it focuses on how one neuron behaves over time rather than modeling its physical shape or spatial structure.

## Setup

```bash
pip install -r requirements.txt
```

Libraries used:

* **NumPy** - numerical calculations and time-series data
* **Matplotlib** - plotting the simulation results

## Project structure

```text
hh_simulation/
├── requirements.txt
├── main.py              <- runs the simulation
├── src/
│   ├── parameters.py    <- Hodgkin-Huxley constants
│   ├── gating.py        <- ion-channel rate equations
│   ├── model.py         <- ionic currents and dV/dt
│   ├── simulate.py      <- Euler integration
│   └── plotting.py      <- plots the results
└── tests/
    └── test_gating.py   <- basic tests for gating equations
```

## Project Status

### Implemented

- Standard Hodgkin-Huxley parameters
- Sodium, potassium, and leak current equations
- Six α/β gating rate functions
- Steady-state gating functions
- Full membrane voltage equation
- Euler integration for membrane dynamics
- Complete simulation loop
- Membrane voltage and gating-variable plots
- End-to-end simulation through `main.py`
- Spike generation and membrane response visualization

## Results

The simulation successfully reproduces the characteristic action potential of a neuron. The membrane voltage changes over time as the sodium and potassium channels open and close, producing a spike similar to the biological firing behavior described by the Hodgkin-Huxley model.

## How It Connects to AI

The Hodgkin-Huxley model is a mathematical model of how neurons process electrical signals. This provides a useful connection to AI because artificial neural networks are also inspired by biological neurons.

While standard neural networks use simplified mathematical neurons, the Hodgkin-Huxley model represents a much more detailed biological neuron, including ion channels, membrane voltage, and time-dependent dynamics.

This project explores the biological side of the idea behind neural computation: **how electrical activity in real neurons can be modeled mathematically and simulated computationally.**

