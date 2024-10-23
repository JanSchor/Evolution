
# Evolution

Small simulation of evolution based on neural networks. Inspired by [video](https://youtu.be/N3tRFayqVtk?si=YQMtKYalPkSQOpWn) from David Miller.

I decided to go public with this project, but it is discontinued.
The slowness of python is very visible here, since it contains a lot of computation.
I am trying to create similar project in c as can be seen here: [EVO-sim2](https://github.com/Waaatzon/EVO-sim2)

## How does it work?

I will cover the absolute basics of evolution principles here.
More detail is provided in the above mentioned video or in the original [github repository](https://github.com/davidrmiller/biosim4) from David Miller.

### Creatures

Creatures are nothing complex. They are represented as small dots in the field.
All creatures have their own brain. This brain is represented by individual genomes.
Based on the genomes and inputs from sensory neurons, action of the creature is calculated.
This happens every step in generation for every creature.
In the first generation all the brains are random.

### Genomes
Genome is represented as 8-digit hexadecimal number.
Genome represents connection between two neurons.
All needed information is in the binary representation of the hex.
 * Bits 0 - 7 represent source neuron
 * Bits 8 - 15 represent sink neuron
 * Bits 16 - 31 represent weight of the connection (devided by 8000 to get value between -4.0 and 4.0)

In each step all the genomes are evaluated, taking the output value from source, multiplying it by weight and pasing it on the input of sink neuron.

### Neurons
There are three types of neurons
 * Sensory - do not take any input, output specific value between -1.0 and 1.0 based on creatures surroundings.
 * Inner - add all the inputs together (from action or another inner) and runs the hyperbolic tangent function to set the value between -1.0 and 1.0. Then it puts this value on the output.
 * Action - same calculation as inner, but they store the resulting value for comparison.

At the end of each step calculation, the action neuron with highest value fires and the action is done.
At the begining every creature has all the neurons, but if they are not connected via any genome, they are useless and removed.

### Criteria for reproducing

For each simulation criteria is set. This criteria is very simple.
For example creature meets the criteria, if it is near right wall of the map.
All the creatures that meet the criteria at the end of generation, get to reproduce.

### Evolution through generations

As mentioned above, the criteria for simulation is set.
All the creatures that meet the criteria pass their brain to the next generation.
This is done by storing all the brains of successful creatures and copying them for the next generation.
This creates the natural selection.

*Whatever reproduces, reproduces. Whatever doesn't, doesn't.*

### Mutation

Mutation is very useful in evolution.
If it was not implemented, the creatures would not move to any more success.
Their brains would be absolutelly the same and they would not be able to adapt to some changes in criteria.
This is ensured by mutation.

At the beginning the chance of mutation happening is set.
Between each two generations the individial genomes are passed to the new creatures.
If mutation happens, one digit in the hex representation of the genome is switched to some different.
This can result in big change in creatures behavior or not having much impact on it.
This can help creatures to exit the local peak of evolution and get closer to greater success.

### Other mechanics

I was experimenting with some other criteria and mechanics for more interesting results, but I left it open and hope to get to it in the new project.

First mechanic was cold area.
Creature would meet the criteria of reproducing, if it got into this area at the end of generation, but it had a small twist.
Creature had to wear coat to survive there (makeCoat action neuron was needed).
Creatures that wear coat are marked with blue color.

Second mechanic was wall.
The wall worked as barrier and creatures needed to go around it to get to the safe zone.
This mechanic can be interesting, because the importance od mutation is visible here.
After introduction of the wall, it takes a few generations, until creatures figure out, how to get around. Without mutation, it would not be possible.

Third mechanic I tried to implement was kill, but it was never finished.
I hope I will get to it in the new project.

## How to run the simulation?

### Requirements

- [Python 3.11](https://www.python.org/downloads/) (or higher)
- [`dearpygui`](https://github.com/hoffstadt/DearPyGui) library (install via pip)

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Waaatzon/EVO-sim2.git
    ```

2. **Install dependencies**:
    This project uses an external library `DearPyGui` which needs to be installed. You can install it with pip:
    ```bash
    pip install dearpygui
    ```

3. **Run the project**:
    After installing the dependencies, you can run the project with:
    ```bash
    python main.py
    ```

The simulation parameters and conditions can be configured inside main.py.