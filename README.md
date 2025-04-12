# Overview
These are our programs from the 2024/25 FLL season "Submerged".


## Pybricks Setup

First, install the pybricks firmware on your brick using the official [Web-Editor](https://code.pybricks.com/). 

To ensure all dependencies are installed correctly, it's recommended to use a virtual environment. Follow the prompts in your IDE on initial opening or the terminal instructions below for your operating system.

### macOS

    # macOS/Linux
    py -3 -m venv .venv
    .venv/scripts/activate

### Windows

    # Windows PowerShell
    py -3 -m venv .venv
    .venv/scripts/activate

Then install the dependencies in the *requirements.txt* file:
 
    pip install -r requirements.txt file

## How to run 

### VS Code

In VS Code, simply use *F5* or *CRTL* + *F5* to upload your program.

### Manual approach
Use this command to upload and execute your wanted program on the brick:

    pybricksdev run ble my_program.py

    # OR:
    pybricksdev run ble --name "name_of_your_spike" main.py
