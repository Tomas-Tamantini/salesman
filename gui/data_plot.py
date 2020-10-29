from matplotlib import pyplot as plt


def plot(num_iterations, costs, temperatures):
    iterations = list(range(num_iterations))
    fig, ax_cost = plt.subplots()
    ax_cost.set_xlabel('Iterations')
    ax_cost.set_ylabel('Distance', color='tab:blue')

    ax_temp = ax_cost.twinx()
    ax_temp.set_ylabel('Temperature', color='tab:red')

    ax_cost.plot(iterations, costs, color='tab:blue')
    ax_temp.plot(iterations, temperatures, color='tab:red')

    plt.tight_layout()
    plt.show()
