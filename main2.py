import random

class QueueSimulation:
    def __init__(self, interval, num_simulations):
        self.interval = interval
        self.num_simulations = num_simulations
        self.total_waiting_time = 0
        self.total_service_time = 0

    def simulate(self):
        for _ in range(self.num_simulations):
            # Random number of people arriving during the interval
            num_people = random.randint(1, 10)

            # Simulate each person in the queue
            for _ in range(num_people):
                service_time = random.uniform(1, 5)  # Random service time
                self.total_service_time += service_time

                # Calculate waiting time (cumulative waiting time for all people)
                self.total_waiting_time += self.total_service_time

    def calculate_average_waiting_time(self):
        # Average waiting time per person
        average_waiting_time = self.total_waiting_time / self.total_service_time
        return average_waiting_time

if __name__ == "__main__":
    interval = 60  # Example: 60 minutes
    num_simulations = 1000  # Example: 1000 simulations

    simulation = QueueSimulation(interval, num_simulations)
    simulation.simulate()

    average_waiting_time = simulation.calculate_average_waiting_time()
    print(f"Average Waiting Time: {average_waiting_time:.2f} minutes")
