# Instance Generator
import numpy as np
import matplotlib.pyplot as plt
from typing import List

import logging

logger = logging.getLogger(__name__)

class instance_generator:
    def __init__(self, num_customers: int = 100, num_vehicles: int = 5, capacity: int = 10):
        self.num_customers = num_customers
        self.num_vehicles = num_vehicles
        self.capacity = capacity
        logger.info('Generator initialized successfully..')

    def generate(self, seed=None, visualize=False) -> List[List[float]]:
        np.random.seed(seed)
        locations = np.round(np.random.rand(self.num_customers, 2) * 100)
        demands = np.random.randint(1, self.capacity + 1, size=self.num_customers) // 2
        # Generate a random offset between -10 and 10 for both x and y coordinates
        offset = np.random.randint(-10, 10, size=2)
        # Apply the offset to the center of the map
        depot = np.array([50, 50]) + offset
        depot = np.append(depot, 0)

        instance = [depot.tolist()]
        customers = [locations[i].tolist() + [demands[i]] for i in range(self.num_customers)]
        instance.extend(customers)

        if visualize:
            self.visualize(instance)

        return instance

    def generate_clustered(self, nof_cluster: int, seed=None, visualize=False) -> List[List[float]]:
        np.random.seed(seed)
        locations = []
        demands = []

        # calculate the number of rows and columns for the grid
        rows = cols = int(nof_cluster ** 0.5)

        # create internal grid (leaving space for customers around each cluster center)
        x = np.linspace(10, 90, rows)
        y = np.linspace(10, 90, cols)

        # get grid intersection points as cluster centers
        cluster_centers = np.array([[i, j] for i in x for j in y])

        num_customers_in_cluster = self.num_customers // nof_cluster
        remaining = self.num_customers % nof_cluster  # Remaining customers after division

        for i, center in enumerate(cluster_centers):
            # Add remaining customers to the first cluster
            if i == 0:
                num_customers_in_this_cluster = num_customers_in_cluster + remaining
            else:
                num_customers_in_this_cluster = num_customers_in_cluster

            cluster_locations = np.round(center + np.random.randn(num_customers_in_this_cluster, 2) * 10)
            locations.extend(cluster_locations.tolist())

            cluster_demands = np.random.randint(1, self.capacity + 1, size=num_customers_in_this_cluster) // 2
            demands.extend(cluster_demands.tolist())

            # Stop generating more clusters if we've reached the number of customers
            if len(locations) >= self.num_customers:
                break

        # It's possible we have generated more locations and demands than the number of customers, so we cut the excess
        locations = locations[:self.num_customers]
        demands = demands[:self.num_customers]

        # Generate a random offset between -10 and 10 for both x and y coordinates
        offset = np.random.randint(-10, 10, size=2)
        # Apply the offset to the center of the map
        depot = np.array([50, 50]) + offset
        depot = np.append(depot, 0)

        instance = [depot.tolist()]
        customers = [locations[i] + [demands[i]] for i in range(len(locations))]

        instance.extend(customers)

        if visualize:
            self.visualize(instance)

        return instance

    def visualize(self, instance: List[List[float]]):
        plt.figure()
        plt.scatter(*zip(*[x[:2] for x in instance[1:]]), c='b', label='Customers')
        plt.scatter(*instance[0][:2], c='r', label='Depot')
        plt.title('CVRP Instance')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()


