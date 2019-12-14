import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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


def animate_life(universe_size=(100,100), probability_of_ones=0.5, quality=100, cmap='Greys', n_generations=50, interval=100, save=True):
    # Initialise the universe
    universe = np.random.choice([0, 1], size=universe_size[0]*universe_size[1], p=[1-probability_of_ones, probability_of_ones]).reshape(universe_size)
    # Animate
    fig = plt.figure(dpi=quality)
    ims = []
    for i in range(n_generations):
        ims.append((plt.imshow(universe, cmap=cmap),))
        universe = generation(universe)
    # Make animation
    im_ani = animation.ArtistAnimation(
        fig, ims, interval=interval, repeat_delay=3000, blit=True
    )
    # Save the animation
    if save:
        im_ani.save("GameOfLife.gif", writer="imagemagick")


if __name__ == "__main__":
    animate_life(
        universe_size=(200, 200),
        probability_of_ones=0.5,
        quality=100,    # image quality in DPI
        cmap='Greys',
        n_generations=100,
        interval=100,    # interval (in milliseconds) between iterations
        save=True,
    )