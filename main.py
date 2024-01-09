import matplotlib.pyplot as plt
import numpy as np

def simulate_drunken_walk(steps):
    x = np.zeros(steps)
    y = np.zeros(steps)

    for i in range(1, steps):
        angle = np.random.uniform(0, 2 * np.pi)
        x[i] = x[i - 1] + np.cos(angle)
        y[i] = y[i - 1] + np.sin(angle)

    return x, y

def calculate_distances(x, y):
    distances = np.sqrt(x**2 + y**2)
    average_distance = np.mean(distances)
    max_distance = np.max(distances)
    return average_distance, max_distance

def main(simulations, steps):
    all_distances = []

    for _ in range(simulations):
        x, y = simulate_drunken_walk(steps)
        average_distance, max_distance = calculate_distances(x, y)
        all_distances.append((average_distance, max_distance))

        # Plot the path for one of the simulations
        if _ == 0:
            plt.plot(x, y, label="Drunken Walk")
            plt.title('Drunken Walk Simulation')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.legend()
            plt.show(block=False)
            plt.pause(0.1)  # Add a delay to allow the user to view the plot

    plt.show()  # Close the last plot window

    avg_distances, max_distances = zip(*all_distances)
    avg_distance_mean = np.mean(avg_distances)
    max_distance_mean = np.mean(max_distances)

    print(f'Average distance over {simulations} simulations: {avg_distance_mean:.2f}')
    print(f'Maximum distance over {simulations} simulations: {max_distance_mean:.2f}')

if __name__ == "__main__":
    simulations = 1000
    steps = 1000
    main(simulations, steps)
