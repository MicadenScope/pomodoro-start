# 🍅 Pomodoro Timer

A desktop Pomodoro timer built with Python and Tkinter.

The application helps users structure focused work sessions and regular breaks using the Pomodoro technique. It automatically switches between work sessions, short breaks and long breaks.

## Features

- 25-minute work sessions
- 5-minute short breaks
- 20-minute long breaks
- Automatic switching between work and break sessions
- Visual countdown timer
- Completed work-session indicators
- Start and reset buttons
- Graphical user interface built with Tkinter

## Technologies

- Python 3
- Tkinter
- Python `math` module

The project only uses modules from the Python standard library. No external packages are required.

## Project Structure

```text
pomodoro-timer/
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── tomato.png
```

## File Overview

- `main.py` – contains the timer logic and graphical user interface
- `tomato.png` – image displayed in the center of the timer

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

No additional Python packages need to be installed.

## Run the Application

Start the application with:

```bash
python main.py
```

A desktop window will open with the Pomodoro timer.

## How It Works

The application follows this cycle:

1. Work for 25 minutes
2. Take a short 5-minute break
3. Repeat the work and short-break cycle
4. After four completed work sessions, take a 20-minute long break

The timer automatically continues to the next session when the countdown reaches zero.

## Session Logic

The session type is determined by the current repetition number:

```python
if reps % 8 == 0:
    # Long break
elif reps % 2 == 0:
    # Short break
else:
    # Work session
```

Every completed work session adds a check mark to the interface.

## Controls

| Button | Action |
|---|---|
| Start | Starts the timer |
| Reset | Stops the current timer and resets the application |

## Configuration

The timer durations are defined as constants:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

You can change these values to customize the timer.

For testing, you can temporarily use shorter values:

```python
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
```

## Concepts Demonstrated

This project demonstrates:

- Graphical user interfaces with Tkinter
- Event-driven programming
- Functions
- Global variables
- Countdown timers
- Tkinter `after()` scheduling
- Conditional logic
- String formatting
- Working with images
- Grid-based layouts

## Dependencies

This project does not require a `requirements.txt` file because it only uses Python standard-library modules:

```python
tkinter
math
```

## Possible Improvements

- Add pause and resume functionality
- Add sound notifications
- Add desktop notifications
- Allow custom work and break durations
- Save completed Pomodoro sessions
- Add daily productivity statistics
- Add a dark mode
- Prevent multiple timers from starting at the same time
- Add keyboard shortcuts
- Package the application as a desktop executable

## Author

**Mick Kuyenda Misamu**  
MicadenScope

## License

This project is licensed under the MIT License.
