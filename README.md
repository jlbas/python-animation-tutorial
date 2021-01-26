# Python Animation Tutorial

Some basic shape manipulations in Python.

## Table of Contents

[[_TOC_]]

## Overview
This repo contains basic Python animations. Although Python is mostly considered to be a high level scripting language, it can be useful for quickly visualizing and building intuition on new ideas. For more advanced simulations, the reader might consider a domain specific framework, such as [ROS](https://www.ros.org/), providing a feature-full robotics suite. However, these platforms often come with significant overhead, and can be time consuming to get up and running. The following scripts will demonstrate how easy it is to get started, which is what makes Python animations so awesome.

## Installation

You will need a basic installation of [Python3](https://www.python.org/downloads/) on your computer. Most of the scripts in this repo will require `matplotlib` and `numpy`. The easiest way to install these packages is using [pip](https://pip.pypa.io/en/stable/installing/):

```
pip install matplotlib numpy
```

If you prefer to use Python in an isolated workspace, checkout [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/). For a complete overview of the official best practices for package management, see the [Python Packaging User Guide](https://packaging.python.org/).

## Usage

Clone this repo somewhere onto your machine:

```
git clone https://git.uwaterloo.ca/autonomous-systems-lab/python-animation-tutorial.git
```

Execute the Python script of your choice from the `src` directory.

## Code Description

It could be helpful to read this description alongside the [animation_template.py](src/animation_template.py) script.

### Structure

There are many approaches we could take to generate an animation. For simplicity, we will separate the simulation from the animation. The scripts follow this general structure:

1. Run the simulation:
	1. Initialize the parameters
	2. Simulate some dynamics, logging values at each timestep
2. Run the animation:
	1. Initialize the plot
	2. Add patches to the plot
	3. Update the patches at each timestep using the logged values
3. Play and optionally save the animation to a local file

### Implementation Approach

To make an animation, we will first create a shape and then perform transformations on that shape at fixed timesteps. In Python, this can be accomplished by manipulating [patches](https://matplotlib.org/3.3.3/api/patches_api.html) from the `matplotlib` package. This module provides many useful subclasses, which will help us create and manipulate various shapes.

More specifically, we will make use of the [FuncAnimation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.animation.FuncAnimation.html) class from the `matplotlib.animation` module. This class creates an animation by repeatedly calling the `animation` function, where we perform the desired transformations on the patches. When instantiating the `FuncAnimation` class, we will set the optional parameter `blit=True`. This helps with performance since only patches that have been changed will be updated in the figure. By specifying this parameter to `True`, `FuncAnimation` expects an iterable list of artists to be returned by `animation`.

## Scripts

### Circle Scaling

![Scaling a circle](media/circle_scaling.gif)

This [script](src/circle_scaling.py) creates an animation for a circle being scaled up and down, fixed at the origin.

### Circle Translation

![Translating a circle](media/circle_translation.gif)

This [script](src/circle_translation.py) creates an animation for a circle being translated along the x axis.

## Contributing

If you feel the need to demonstrate additional animation functionalities, make a merge request and add a short description and video to the [README](README.md). Here is an example showing how to save a gif of your animation from the Python script:

```python
from matplotlib.animation import FFMpegWriter
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(...)
ani.save('path/to/save/animation.gif', writer=FFMpegWriter(fps=50))
```

Please open an issue for installation difficulties, bugs found in the animation scripts or suggested improvements.
