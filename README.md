# GUI Playground

This repository is a learning playground for experimenting with basic graphical user interfaces (GUIs) in Python.

It contains small, focused examples built with **Tkinter**, Python’s built-in GUI library. The goal of this repo is to practice event-driven programming, widget layout, and integrating simple third-party libraries into a desktop interface — not to build full applications.

Some ideas are inspired by optional exercises from the **Zero To Mastery Python course**, but the implementations here reflect my own exploration, research, and assembly based on documentation and experimentation.

---

## Current Demo

### Joke Generator (Tkinter Demo)

A minimal desktop application that displays programming jokes.

**What it does:**

* Creates a simple Tkinter window
* Displays instructional text and a placeholder area
* Uses a button to trigger an action
* Fetches a programming joke using the `pyjokes` library
* Updates the GUI dynamically in response to user interaction

The application is intentionally small and focused to demonstrate:

* Tkinter widget setup
* Event handling with callbacks
* Updating UI state at runtime
* Integrating a third-party Python package into a GUI

---

## Usage

Run the script directly:

```
python joke_gui.py
```

Click the **“Tell me a joke”** button to generate and display a programming joke.

---

## Purpose of This Repository

* Learn the basics of GUI programming with Tkinter
* Practice event-driven application structure
* Integrate external Python libraries into a desktop interface
* Build small, self-contained learning demos
* Experiment without relying on paid APIs or external services

This repository may grow as additional GUI demos are added.

---

## Requirements

* Python 3
* pyjokes

---

## Notes

* This is a learning-focused repository
* The GUI is intentionally minimal and unstyled
* The demo prioritizes clarity and structure over features
* Not intended as a production application
