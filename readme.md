# Introduction
This project is an individual assignment for linear algebra classes at bachelor level. 
The assignment involves utilising transformation matrices to perform transformations on vectors.
In my assignment I utilise transformations in 3-dimensional space and my aim is to give the user possibility of choosing 
transformation origin and transformation axis - transformation axis would be the axis along which the rotation happens.

Matplotlib backends integrate Matplotlib plotting capabilities into different windowing systems.
In this application I use `matplotlib.backends.backend_tkagg` as backend to power plots in Tkinter.

`FigureCanvasTkAgg` is the main class needed to embed Matplotlib figures into a Tkinter GUI. 
Those are interactive, i.e. can be updated and displayed at runtime.

With `matplotlib.backends.backend_tkagg` other extra features can be added, such as interactive toolbars (like `NavigationToolbar2Tk`).


### Project requirements:
- use exclusively matrix multiplication throughout the assignment—no separate operations on individual coordinates allowed. 
- use libraries: math, numpy, numpy.linalg
- recommended UI library for Python: Tkinter

#### Assessment criteria:
- correct implementation of rotation, shearing, mirroring, scaling and translation.
- in code explanation of the matrices, operations and their mathematical/ graphical effects.
- originality and creativity of the end result and/or implementation.
- use of colors.
- industry standard in coding.

### Notes and process:
The notes I used is in another markdown file in the root of this repository, called `notes_transformations.md`. 
Those are linear algebra principles and my writing down of intuitions to help conceptualise the steps in the assignment work.


# Getting started
After cloning this repo:

1. in the project's root directory create a new virtual environment:
```bash
python -m venv .venv
```

2. Activate the new environment:
```bash
# On Windows
.venv\Scripts\activate
```

3. Install the required packages:

```bash
# install packages from requirements file
pip install -r requirements.txt
```

4. Open PyCharm and configure it to use the new virtual environment:
Go to `File > Settings > Project > Python Interpreter`
Add the new interpreter by pointing to `.venv\Scripts\python.exe`.

