import numpy as np
import matplotlib.pyplot as plt
#0 = susceptible
#1 = infected
#2 = recovered
population = np.zeros((100, 100))
# Choose one random row and one random column as the starting outbreak location.
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
#Set the infection probability beta to 0.3
#Set the recovery probability gamma to 0.05
beta = 0.3
gamma = 0.05
#Create an empty list to save population pictures at selected times.
pictures = []
#Repeat the simulation for time steps from 0 to 100.
for time in range(101):
    if time in [0, 10, 50, 100]:
        pictures.append(population.copy())
    #Find the positions of all infected people.
    infected_points = np.where(population == 1)
    new_population = population.copy()
    #Go through each infected person.
    #Get the row and column of the infected person.
    for i in range(len(infected_points[0])):
        row = infected_points[0][i]
        col = infected_points[1][i]
        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:
                #Skip the infected person's own cell.
                if row_change == 0 and col_change == 0:
                    continue
                #Calculate the neighbour's row and column.
                neighbour_row = row + row_change
                neighbour_col = col + col_change
                #Check that the neighbour's row is inside the grid.
                if neighbour_row >= 0 and neighbour_row < 100:
                    if neighbour_col >= 0 and neighbour_col < 100:
                        if population[neighbour_row, neighbour_col] == 0:
                            random_number = np.random.random()
                            if random_number < beta:
                                new_population[neighbour_row, neighbour_col] = 1
        random_number = np.random.random()
        #If the random number is less than gamma,change this infected person to recovered.
        if random_number < gamma:
            new_population[row, col] = 2
    population = new_population.copy()
plt.figure(figsize=(8, 8), dpi=150)
#Create the first subplot and show the population at time 0.
plt.subplot(2, 2, 1)
plt.imshow(pictures[0], cmap="viridis", interpolation="nearest")
plt.title("time 0")
#Create the second subplot and show the population at time 10.
plt.subplot(2, 2, 2)
plt.imshow(pictures[1], cmap="viridis", interpolation="nearest")
plt.title("time 10")
#Create the third subplot and show the population at time 50.
plt.subplot(2, 2, 3)
plt.imshow(pictures[2], cmap="viridis", interpolation="nearest")
plt.title("time 50")
#Create the fourth subplot and show the population at time 100.
plt.subplot(2, 2, 4)
plt.imshow(pictures[3], cmap="viridis", interpolation="nearest")
plt.title("time 100")
#Show the figure.
plt.show()
