import numpy as np
import matplotlib.pyplot as plt
# 0 = susceptible
# 1 = infected
# 2 = recovered
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05
pictures = []
for time in range(101):
    if time in [0, 10, 50, 100]:
        pictures.append(population.copy())
    infected_points = np.where(population == 1)
    new_population = population.copy()
    for i in range(len(infected_points[0])):
        row = infected_points[0][i]
        col = infected_points[1][i]
        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:
                if row_change == 0 and col_change == 0:
                    continue
                neighbour_row = row + row_change
                neighbour_col = col + col_change
                if neighbour_row >= 0 and neighbour_row < 100:
                    if neighbour_col >= 0 and neighbour_col < 100:
                        if population[neighbour_row, neighbour_col] == 0:
                            random_number = np.random.random()
                            if random_number < beta:
                                new_population[neighbour_row, neighbour_col] = 1
        random_number = np.random.random()
        if random_number < gamma:
            new_population[row, col] = 2
    population = new_population.copy()
plt.figure(figsize=(8, 8), dpi=150)
plt.subplot(2, 2, 1)
plt.imshow(pictures[0], cmap="viridis", interpolation="nearest")
plt.title("time 0")
plt.subplot(2, 2, 2)
plt.imshow(pictures[1], cmap="viridis", interpolation="nearest")
plt.title("time 10")
plt.subplot(2, 2, 3)
plt.imshow(pictures[2], cmap="viridis", interpolation="nearest")
plt.title("time 50")
plt.subplot(2, 2, 4)
plt.imshow(pictures[3], cmap="viridis", interpolation="nearest")
plt.title("time 100")
plt.show()