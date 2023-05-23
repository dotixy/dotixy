import numpy as np
from typing import List

import logging

logger = logging.getLogger(__name__)

class generator:
    def __init__ (
            self,
            ngeneration : int = 100
    ):
        self.ngeneration = ngeneration
        logger.info('Generator initialized successfully..')

    def generate(self) -> np.array:
        return np.random.rand(self.ngeneration)