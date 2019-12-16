import numpy as np


class Logger:
    def __init__(self, patterns, universe_size, probability_of_ones, n_generations):
        self.data = {
            "universe_size": universe_size,
            "probability_of_ones": probability_of_ones,
            "n_generations": n_generations,
            "all_attempts": {}
        }
        self.generation_attempts = {}
        for pattern in patterns:
            self.data["all_attempts"][pattern['name']] = []
            self.generation_attempts[pattern['name']] = 0

    def add_occure(self, pattern_name):
        self.generation_attempts[pattern_name] += 1

    def add_occurrences_from_generation(self):
        for pattern in self.generation_attempts:
            self.data["all_attempts"][pattern].append(self.generation_attempts[pattern])
        self._reset_generation_attempts()

    def _reset_generation_attempts(self):
        for pattern in self.generation_attempts:
            self.generation_attempts[pattern] = 0

    def save_data(self):
        random = np.random.random()
        np.save("Plot/log{}.npy".format(random), self.data, allow_pickle=True)


