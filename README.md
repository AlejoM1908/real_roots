# Real Roots Monte Carlo Simulation
## Testing the generated mathematical model

The following repository is created to generate a quick simulation using the monte carlo method to test the mathematical model of the workshop to find the probability of obtaining a real root of the quadratic function x²+2bx+c=0, having b and c uniformly distributed over an interval (-beta, beta) with beta in the Real Numbers

## Getting the code of the workshop

The whole project code is public and open source in the Github.com platform, to easily get access to it install the Version Control System GIT and then excecute:

```sh
git clone https://github.com/AlejoM1908/real_roots.git
cd real_roots
```

## Usage

The project is created using python with MatPlotLib as an extra package for the visualization of the simulation results; To run the project we recommend using a python virtual environment as a good practice. Whichever you choose, run the following python commands to obtain the necessary packages (Remember to activate the virtual environment before running it):

```sh
pip install matplotlib
```

Once you have the required packages, run the project using the following command:
```sh
py main.py
```

## Development

If you want to adjust the number of simulations of the code (10.000 by default) get into main function definition and change the integer value inside plot_simulation function
