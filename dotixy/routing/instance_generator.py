import numpy as np
from typing import List

import logging

logger = logging.getLogger(__name__)

class instance_generator:
    def __init__(
            self,
            num_customers: int = 100,
            num_vehicles: int = 5,
            capacity: int = 10,
            seed: int = None
    ):
        self.num_customers = num_customers
        self.num_vehicles = num_vehicles
        self.capacity = capacity
        self.seed = seed
        np.random.seed(seed)
        logger.info('Generator initialized successfully..')

    def generate(self) -> List[List[float]]:
        locations = np.random.rand(self.num_customers, 2)  # Generate random (x, y) coordinates for customers
        demands = np.random.randint(1, self.capacity + 1, size=self.num_customers)  # Generate random demands for customers
        depot = np.random.rand(2)  # Generate random (x, y) coordinates for depot

        instance = []
        instance.append(depot.tolist())  # Add depot as the first location in the instance

        for i in range(self.num_customers):
            customer = [demands[i]] + locations[i].tolist()
            instance.append(customer)  # Add each customer to the instance

        return instance
