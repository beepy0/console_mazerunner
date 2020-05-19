# Console Mazerunner
### Solve the maze of the gray blade-runner-esque landscape. 
### Run around abandoned buildings, towers and tunnels and bring the music home.

- Runs entirely in the command line (terminal)
- Easy setup (run `pip3 install -r` for the requirements.txt, see instructions below)
- Potential for new features and open-sourced for everybody



# Setup

## Base requirements
- Python 3.6+
- pip3
- Under Linux/OS X, you need to be root in order to use the required keyboard library

## Without an IDE
- Open a terminal, navigate to the project folder
- **if using Linux/OS X**: enter root mode `sudo su`
- Install the library dependencies via pip:
  `pip3 install -r requirements.txt` . More info [here](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- run `python3 main.py`

## Using PyCharm
- Create a new Python project
- Automatically install packages via the requirements.txt file and [the official instructions](https://www.jetbrains.com/help/pycharm/managing-dependencies.html#) (Best use a [virtualenvironment to separate library dependencies between projects](https://www.jetbrains.com/help/idea/creating-virtual-environment.html#))
- Start in a terminal window **outside** the IDE, Navigate to the project folder and run `python3 main.py`
