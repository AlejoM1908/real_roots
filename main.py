import random
import matplotlib.pyplot as plt
"""
This program is used to generate a monte carlo simulation of the probability of
real roots in the cuadratic equation x^2 + 2bx + c = 0

Author: Daniel Alejandro Melo (dmelo@unal.edu.co)
Last modified: 2022-08-06
"""

def real_roots() -> bool:
    """
    Used to generate a random cuadratic equation and check if it has real roots or not

    Returns:
        bool: True if the equation has real roots, False otherwise
    """
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)

    # Determining if the roots are real
    if b**2 - c >= 0:
        return True
    else:
        return False

def montecarlo_simulation(n: int) -> float:
    """"
    Used to generate a monte carlo simulation of the probability of real roots in the cuadratic equation x^2 + 2bx + c = 0

    Args:
        n (int): Number of simulations

    Returns:
        float: Probability of real roots in n simulations
    """
    real_number = 0

    for i in range(n):
        if real_roots():
            real_number += 1

    return real_number / n

def plot_simulation(n: int) -> None:
    """
    Used to plot the monte carlo simulation of the probability of real roots in the cuadratic equation x^2 + 2bx + c = 0

    Args:
        n (int): Number of simulations
    """
    plt.figure()
    plt.title('Probability of real roots in the cuadratic equation for {} simulations'.format(n))
    plt.xlabel('Number of simulations')
    plt.ylabel('Probability of real roots')
    plt.xlim(0, n)

    plt.plot(range(1, n), [montecarlo_simulation(i) for i in range(1, n)])
    plt.show()


def main() -> None:
    plot_simulation(10000)

if __name__ == '__main__':
    main()
