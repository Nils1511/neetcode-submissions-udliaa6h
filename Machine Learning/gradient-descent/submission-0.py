class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        while iterations > 0:
            x = init
            der = 2 * x
            new = x - learning_rate * der
            init = new
            iterations -= 1
        return round(init, 5)
        
    