let plotData = {
    x: [],
    y: [],
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Collatz Sequence',
};

let layout = {
    title: 'Collatz Sequence',
    xaxis: { title: 'Step' },
    yaxis: { title: 'Value' },
};

let config = {
    responsive: true,
};

const plot = Plotly.newPlot('plot', [plotData], layout, config);

function collatz(n) {
    let sequence = [n];

    function updatePlot(step, value) {
        Plotly.extendTraces('plot', { x: [[step]], y: [[value]] }, [0]);
    }

    function generateNext() {
        if (n !== 1) {
            if (n % 2 === 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            sequence.push(n);
            const step = sequence.length - 1;
            updatePlot(step, n);
            requestAnimationFrame(generateNext);
        }
    }

    generateNext();
}

document.getElementById('plotButton').addEventListener('click', () => {
    const n = parseInt(document.getElementById('inputNumber').value);
    if (isNaN(n) || n <= 0) {
        alert('Please enter a positive integer.');
        return;
    }

    plotData = {
        x: [0],
        y: [n],
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Collatz Sequence',
    };

    layout.title = `Collatz Sequence for ${n}`;

    Plotly.react('plot', [plotData], layout, config);

    collatz(n);
});
