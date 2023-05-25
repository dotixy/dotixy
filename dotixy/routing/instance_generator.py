import numpy as np
from typing import List

import logging

logger = logging.getLogger(__name__)

class instance_generator:
    def __init__(
            self,
            num_customers: int = 100,
            num_vehicles: int = 5,
            capacity: int = 10
    ):
        self.num_customers = num_customers
        self.num_vehicles = num_vehicles
        self.capacity = capacity
        logger.info('Generator initialized successfully..')

    def generate(self, seed = None) -> List[List[float]]: 
        np.random.seed(seed)
        locations = np.round(np.random.rand(self.num_customers, 2) * 100)  # Generate random (x, y) coordinates for customers (between 0-100)
        demands = np.random.randint(1, self.capacity + 1, size=self.num_customers) // 2   # Generate random demands for customers (between 1-vehicle_capacity/2 -> can be updated...)
        depot = np.round(np.random.rand(2) * 100)  # Generate random (x, y) coordinates for the depot (between 0-100)
        depot = np.append(depot, 0)  # Depot has no demand

        instance = [depot.tolist()]  # Add depot as the first location in the instance
        customers = [locations[i].tolist() + [demands[i]] for i in range(self.num_customers)]
        instance.extend(customers)

        return instance
