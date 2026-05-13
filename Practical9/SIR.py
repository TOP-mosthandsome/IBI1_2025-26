import numpy as np
import matplotlib.pyplot as plt
N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
S_list = [S]
I_list = [I]
R_list = [R]
for time in range(1000):
    infection_probability = beta * I / N
    new_infections = np.random.choice(
        [0, 1],
        size=S,
        p=[1 - infection_probability, infection_probability]
    )
    number_new_infections = np.sum(new_infections)
    new_recoveries = np.random.choice(
        [0, 1],
        size=I,
        p=[1 - gamma, gamma]
    )
    number_new_recoveries = np.sum(new_recoveries)
    S = S - number_new_infections
    I = I + number_new_infections - number_new_recoveries
    R = R + number_new_recoveries
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label="susceptible")
plt.plot(I_list, label="infected")
plt.plot(R_list, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.show()