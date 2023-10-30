import plotly.graph_objects as go
import plotly.io as pio
import requests

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
    fig = go.Figure()

    # Add the scatter plot trace
    fig.add_trace(go.Scatter(x=list(range(len(sequence))), y=sequence, mode='lines+markers', name='Collatz Sequence'))

    # Set the layout title
    fig.update_layout(title=f'Collatz Sequence for {n}')

    # Plot the figure
    pio.show(fig)

if __name__ == '__main__':
    # Get the input number from the user
    n = int(input('Enter a positive integer: '))

    # Plot the Collatz sequence for the given number
    plot_collatz(n)
