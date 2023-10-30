import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import time
import plotly.io as pio

def collatz(n):
    """Generates the Collatz sequence for the given number n.

    Args:
        n: A positive integer.

    Returns:
        A list of integers, representing the Collatz sequence for n.
    """

    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

def plot_collatz(n):
    """Plots the Collatz sequence for the given number n.

    Args:
        n: A positive integer.
    """

    # Generate the Collatz sequence
    sequence = collatz(n)

    # Create the Plotly figure
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Real-time Collatz Graph', 'Step-by-step Collatz Graph')
    )

    # Add the real-time scatter plot trace
    fig.add_trace(go.Scatter(x=list(range(len(sequence))), y=sequence, mode='lines+markers', name='Collatz Sequence'), row=1, col=1)

    # Add the step-by-step scatter plot trace
    fig.add_trace(go.Scatter(x=list(range(len(sequence))), y=sequence, mode='markers', name='Collatz Sequence'), row=1, col=2)

    # Set the layout
    fig.update_layout(title='Collatz Sequence', xaxis_title='Step', yaxis_title='Value')

    # Plot the figure
    pio.show(fig)

def update_realtime_graph(fig, sequence):
    """Updates the real-time Collatz graph.

    Args:
        fig: The Plotly figure object.
        sequence: The Collatz sequence.
    """

    # Get the real-time scatter plot trace
    trace = fig.data[0]

    # Update the trace data
    trace.x = list(range(len(sequence)))
    trace.y = sequence

    # Redraw the graph
    pio.update(fig)

if __name__ == '__main__':
    # Get the input number from the user
    n = int(input('Enter a positive integer: '))

    # Plot the Collatz sequence
    plot_collatz(n)

    # Start the real-time update loop
    while True:
        # Generate the next value in the Collatz sequence
        n = collatz(n)[-1]

        # Update the real-time graph
        update_realtime_graph(fig, collatz(n))

        # Wait for a short period of time
        time.sleep(0.1)
