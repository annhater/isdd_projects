##################################
# Main script for adv_md package  #
##################################


#1. Initialization of the parameters

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import random as rd

#define constants
L = 5

# Define a fixed set of attractors and their weights
num = 10
w_i = [rd.uniform(0.5, 1) for _ in range(num)]
x_i = [rd.randint(-L, L) for _ in range(num)]
y_i = [rd.randint(-L, L) for _ in range(num)]
# define the energy potential formula
def energy_potential(x,y):
  energy = 0 # accumulate the sum
  for i in range(num):
    energy += -w_i[i] * np.exp(-((x-x_i[i])**2)-((y-y_i[i])**2))
  return(energy)

# define the Monte-Carlo simulation space, grid(X,Y)
X = np.arange(-L,L + 0.01, 0.01) # 0.01 increment
Y = np.arange(-L,L +0.01, 0.01)
X_space, Y_space = np.meshgrid(X,Y)
grid = np.column_stack([X_space.ravel(), Y_space.ravel()]) # grid = coordinates matrix

# calculate energies for points in matrix
energies = []
for x_coord, y_coord in grid:
     energies.append(energy_potential(x_coord, y_coord))

# check the energies
np.set_printoptions(legacy = '1.25') # if print, set normal float printing mode
energies


# we need to the energies list into a 2D array to match X_space and Y_space
# the shape should be (len(Y), len(X)), which is (2*L*100+1, 2*L*100+1)
Z = np.array(energies).reshape(len(Y), len(X))


# contour plot of the energy potential
contour = plt.contourf(X_space, Y_space, Z, levels = 100, cmap='viridis')
plt.colorbar(contour, label='Energy Potential')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Energy Potential Landscape')
plt.grid(True)
plt.show()



# define Metropolis Monte-Carlo test function
def mcc_test(f2, f1, T):
  #f1 = CURRENT ENERGY
  #f2 = Nex tenergy
  #T = temp
  #condition 1
  #si la valeur du potentiel f2 de la position i + 1 est inférieure
  #à la valeur du potentiel f1 de la position i
  if f2 < f1:
    return True
  # condition 2
  # si le nouveau potentiel est plus haut
  else:
    delta_E = f2 - f1
    # Calcul de la probabilité d'acceptation
    p = np.exp(-delta_E / T)
    # nombre aléatoire r entre 0 et 1
    r = rd.random()
  # si e^(-delta_E / T) > r, on accepte
  if p > r:
    return True
  else:
    return False

def move(x, y, step_size):
    # Random step, using uniform to allow float step_size
    x_step = rd.uniform(-step_size, step_size)
    y_step = rd.uniform(-step_size, step_size)

    # New position
    new_x = x + x_step
    new_y = y + y_step

    # Boundary conditions: stay inside [-L, L]
    new_x = np.clip(new_x, -L, L)
    new_y = np.clip(new_y, -L, L)

    return new_x, new_y

# simulation param
T = 0.5
n_etapes = 1000
x_act, y_act = 0.0, 0.0 # start coords

# save the trajectory for visualisation
traj_x = [x_act]
traj_y = [y_act]

for _ in range(n_etapes):
    f1 = energy_potential(x_act, y_act) # we calculate current energy (f1)
    x_prop, y_prop = move(x_act, y_act, step_size=0.5) # we check if we move
    f2 = energy_potential(x_prop, y_prop) # we calculate next energy (f2)
    if mcc_test(f1, f2, T):  # we check mcc_test
        # if accepted, we change the position
        x_act, y_act = x_prop, y_prop

    # we save the new coords
    traj_x.append(x_act)
    traj_y.append(y_act)



# visualize the path

# plot the path
plt.contourf(X_space, Y_space, Z, levels=50, alpha=0.8)
plt.plot(traj_x, traj_y, color='white', marker='o', markersize=3, linewidth=1)
plt.legend()
plt.show()   

#compare the real global minimum with the one predicted by mmc
global_min_energy = np.min(energies)
global_min_index = np.argmin(energies)
global_min_x = grid[global_min_index, 0]
global_min_y = grid[global_min_index, 1]

print(f"Global Minimum Energy: {global_min_energy}")
print(f"Global Minimum (X, Y) coordinates: ({global_min_x}, {global_min_y})")



#lists for every MC sim
final_x_coords = []
final_y_coords = []
final_energies = []

#run MC sims
num_simulations = 50

for i in range(num_simulations):
    x_act, y_act = 0.0, 0.0

    # Monte Carlo simulation for a single run
    for _ in range(n_etapes):
        f1 = energy_potential(x_act, y_act) # current energy
        x_prop, y_prop = move(x_act, y_act, step_size=0.5) # proposed move
        f2 = energy_potential(x_prop, y_prop) # energy at proposed position

        if mcc_test(f1, f2, T):  # check mcc_test
            # if accepted, update position
            x_act, y_act = x_prop, y_prop

    # After n steps, save the final coordinates and energy for this simulation
    final_x_coords.append(x_act)
    final_y_coords.append(y_act)
    final_energies.append(energy_potential(x_act, y_act))


#compare either via distance (spacial difference)
#or via energy difference
#results table, statistics on n iterations

spatial_distances = []
energy_differences = []

for i in range(num_simulations):
    final_x = final_x_coords[i]
    final_y = final_y_coords[i]
    final_energy = final_energies[i]

    # spatial difference (distance)
    spatial_dist = np.sqrt((final_x - global_min_x)**2 + (final_y - global_min_y)**2)
    spatial_distances.append(spatial_dist)

    # energy difference
    energy_diff = np.abs(final_energy - global_min_energy)
    energy_differences.append(energy_diff)

print(f"Spatial Distances: {spatial_distances}")
print(f"Energy Differences: {energy_differences}")



# Statistics
spatial_mean = np.mean(spatial_distances)
spatial_std = np.std(spatial_distances)
spatial_median = np.median(spatial_distances)

energy_mean = np.mean(energy_differences)
energy_std = np.std(energy_differences)
energy_median = np.median(energy_differences)

statistics_data = {
    'Metric': ['Spatial Distance', 'Energy Difference'],
    'Mean': [spatial_mean, energy_mean],
    'Standard Deviation': [spatial_std, energy_std],
    'Median': [spatial_median, energy_median]
}

# save stats as df
statistics_df = pd.DataFrame(statistics_data)
print("Statistical Metrics:")
print(statistics_df)