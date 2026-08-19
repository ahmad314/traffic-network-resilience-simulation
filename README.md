# Network Resilience Simulation: Road Conflation & Traffic Jams

This repository implements a Cellular Automata (CA) model to simulate network resilience under traffic congestion. Utilizing the Nagel-Schreckenberg model, the simulation evaluates vehicle dynamics during lane merging and induced bottlenecks.

## Background & Methodology

The simulation divides a road into discrete cells and models vehicle behavior through four fundamental rules: acceleration (up to a limit $v_{max}$), braking (to avoid collisions), randomization/dawdling (representing human reaction delay), and forward movement[cite: 3]. 

The primary scenarios evaluated include:
1. **Street Conflation:** Simulating two lanes ("green" and "red") merging into a single lane. Priority rules resolve merge conflicts:
   * **Rule 1:** The vehicle closest to the conflation point proceeds first.
   * **Rule 2:** The "green" lane maintains strict priority over the "red" lane.
2. **Traffic Jam & Resilience:** An artificial bottleneck is induced by blocking a specific cell for 10 timesteps. The system's resilience is quantified by plotting throughput and average velocity evolution over time as the jam clears.

## Key Findings

* **Density Impact:** Average traffic velocity drops significantly as initial vehicle count increases.
* **Rule Variations:** While both priority rules adequately handle conflation, assigning strict priority to a single lane (Rule 2) yields a marginally smoother throughput recovery following a bottleneck event.
