import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        result = []
        for num in z:
            result.append(round(1 / (1 + math.e ** (-num)), 5))

        return result

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        result = []

        for num in z:
            if num < 0:
                result.append(float(0))
            else:
                result.append(float(num))

        return result
