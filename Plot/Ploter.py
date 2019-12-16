import matplotlib.pyplot as plt
import numpy as np
# import Plot.InitParams


def load_data(file_name):
    data = np.load(file_name, allow_pickle=True).item()
    return data


def plot_occurances(data):
    x = np.arange(int(data["n_generations"]))
    for occurances in data["all_attempts"]:
        plt.plot(x, data["all_attempts"][occurances])


def add_legend(data):
    plt.legend([x for x in data["all_attempts"]])


def sign_axis():
    plt.xlabel("Generation num (-)")
    plt.ylabel("Occurrences num (-)")

def add_title(data):
    plt.title("Occurrences of specified patterns in {} generations \n on {} board shape with {} probability".format(
        data["n_generations"],
        data["universe_size"],
        data["probability_of_ones"]
    ))

if __name__ == '__main__':
    data = load_data("log.npy")
    plot_occurances(data)
    add_legend(data)
    sign_axis()
    add_title(data)
    plt.tight_layout()
    plt.show()
