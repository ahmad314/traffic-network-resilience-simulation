import numpy as np
import pandas as pd
import random

def sim_timestep_merge(positions, pb=0.2, vmax=5, ncells=100, merge_start=40, merge_end=60, rule=1, jam_pos=None, current_time=None, jam_start=None, jam_end=None):
    """
    Executes a single timestep of the Nagel-Schreckenberg traffic model.
    """
    pos_new = {}
    car_list = sorted(positions.items(), key=lambda x: x[1])

    for i, (car, pos) in enumerate(car_list):
        front_pos = car_list[i + 1][1] if i < len(car_list) - 1 else pos + vmax + 1
        gap = front_pos - pos - 1
        v = min(gap, vmax)

        if random.random() < pb:
            v = max(v - 1, 0)

        if merge_start <= pos + v <= merge_end:
            competing_car = None
            for other_car, other_pos in positions.items():
                if other_car != car and merge_start - vmax <= other_pos <= merge_end and abs(other_pos - (pos + v)) <= 1:
                    competing_car = (other_car, other_pos)
                    break

            if competing_car:
                if rule == 1:
                    if pos < competing_car[1]:
                        v = 0
                    elif pos == competing_car[1] and random.random() < 0.5:
                        v = 0
                elif rule == 2:
                    if car.startswith('R') and competing_car[0].startswith('G'):
                        v = 0
                    elif car.startswith('G') and competing_car[0].startswith('R'):
                        v = min(gap, vmax)

        if jam_pos and current_time is not None and jam_start <= current_time <= jam_end:
            if pos < jam_pos <= pos + v:
                v = max(0, jam_pos - pos - 1)

        next_pos = max(pos, pos + v)
        if next_pos < ncells:
            pos_new[car] = next_pos

    return pos_new

def run_merge_simulation(nsteps, positions, **kwargs):
    """
    Runs the simulation over a specified number of steps and returns a DataFrame.
    """
    records = [{'time': 0, **positions}]
    current_positions = positions.copy()
    
    for t in range(1, nsteps + 1):
        current_positions = sim_timestep_merge(current_positions, current_time=t, **kwargs)
        records.append({'time': t, **current_positions})
        
    df = pd.DataFrame(records)
    df.set_index('time', inplace=True)
    return df
