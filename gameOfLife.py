import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Logger import Logger
from Patterns import Patterns
from match import match2
from tqdm import tqdm


def survival(x, y, universe):
    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    # The rules of Life
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    return universe[x, y]


def generation(universe):
    new_universe = np.copy(universe)
    # Apply the survival function to every cell in the universe
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            new_universe[i, j] = survival(i, j, universe)
    return new_universe


def animate_life(universe_size=(100,100), probability_of_ones=0.5, quality=100, cmap='Greys',
                 n_generations=50, interval=100, animation_save=True, log_save=True):
    # Initialise the universe
    universe = np.random.choice([0, 1], size=universe_size[0]*universe_size[1],
                                p=[1-probability_of_ones, probability_of_ones]).reshape(universe_size)
    # Initialise logger
    logger = Logger(Patterns.patterns, universe_size, probability_of_ones, n_generations)

    # Animate
    fig = plt.figure(dpi=quality)
    ims = []
    for i in tqdm(range(n_generations), "Generation Progress: "):
        match2(universe.copy(), universe.shape[0], universe.shape[1], Patterns.patterns, logger)
        logger.add_occurrences_from_generation()
        ims.append((plt.imshow(universe, cmap=cmap),))
        universe = generation(universe)
    print(logger.data["all_attempts"])

    # Make animation
    im_ani = animation.ArtistAnimation(
        fig, ims, interval=interval, repeat_delay=3000, blit=True
    )
    # Save the animation and logger

    if animation_save:
        im_ani.save("GameOfLife.gif", writer="imagemagick")
    if log_save:
        logger.save_data()


if __name__ == "__main__":
    animate_life(
        universe_size=(200, 200),
        probability_of_ones=0.4,
        quality=100,    # image quality in DPI
        cmap='Greys',
        n_generations=1000,
        interval=150,    # interval (in milliseconds) between iterations
        animation_save=True,
        log_save=True
    )
