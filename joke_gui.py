"""
A simple Tkinter GUI demonstration that displays programming jokes.

This script provides a minimal desktop interface with a button that retrieves
and displays a programming joke using the pyjokes library. It is intended as a
learning exercise to explore basic Tkinter widgets, event-driven behavior, and
integration with a third-party Python package.

The application is deliberately kept small and focused, prioritizing clarity
and structure over advanced GUI features.
"""

import tkinter
import pyjokes


def get_joke(joke_label):
    """
    Retrieves a programming joke and updates the GUI to display it.

    The function uses the pyjokes library to fetch a single joke and replaces
    the text of the provided Tkinter label with the retrieved content. It is
    designed to be triggered by a user action, such as a button click.

    Args:
        joke_label (tkinter.Label): The label widget used to display the joke.
    """
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)


def main():
    """
    Initializes and runs the Tkinter GUI application.

    The function creates the main application window, configures the interface
    elements, and starts the Tkinter event loop. User interaction is handled
    through a button that triggers joke retrieval and updates the display
    dynamically.
    """
    root = tkinter.Tk()
    root.title("Joke Generator (Tkinter Demo)")
    label = tkinter.Label(
        root, text='Click the button to generate a programming joke.')
    label.pack(pady=10)

    joke_label = tkinter.Label(root, text="Your joke will appear here.")
    joke_label.pack(pady=20)

    # Insert button
    get_joke_button = tkinter.Button(
        root, text='Tell me a joke', command=lambda: get_joke(joke_label))
    get_joke_button.pack(pady=50)
    root.mainloop()


if __name__ == "__main__":
    main()
