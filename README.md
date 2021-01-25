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

## Code Structure

There are many approaches we could take to generate an animation. For simplicity, we will separate the simulation from the animation. These scripts all have the following general structure:

1. Run the simulation:
	1. Initialize the parameters
	2. Simulate some dynamics, logging values at each timestep
2. Run the animation:
	1. Initialize the plot
	2. Add patches to the plot
	3. Update the patches at each timestep using the logged values
3. Play and optionally save the animation to a local file

## Scripts

Click to expand any of the following items to view a description and video of the corresponding script:

<p>
<details>
<summary>Circle Scaling</summary>

![Scaling a circle](media/circle_scaling.gif)

This [script](src/circle_scaling.py) creates an animation for a circle fixed at the origin, being scaled up and down.
</details>
</p>
