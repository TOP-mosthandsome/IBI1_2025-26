import numpy as np
import matplotlib.pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vaccination_rates = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.figure(figsize=(6, 4), dpi=150)
for vaccination_rate in vaccination_rates:
    vaccinated = int(N * vaccination_rate / 100)
    I = 1
    R = vaccinated
    S = N - I - R
    I_list = [I]
    for time in range(time_steps):
        infection_probability = beta * I / N
        if S > 0:
            new_infections = np.random.choice(
                [0, 1],
                size=S,
                p=[1 - infection_probability, infection_probability]
            )
            number_new_infections = np.sum(new_infections)
        else:
            number_new_infections = 0
        if I > 0:
            new_recoveries = np.random.choice(
                [0, 1],
                size=I,
                p=[1 - gamma, gamma]
            )
            number_new_recoveries = np.sum(new_recoveries)
        else:
            number_new_recoveries = 0

        S = S - number_new_infections
        I = I + number_new_infections - number_new_recoveries
        R = R + number_new_recoveries
        I_list.append(I)
    plt.plot(I_list, label=str(vaccination_rate) + "%")
plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()