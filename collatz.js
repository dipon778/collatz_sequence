function collatz(n) {
    const sequence = [n];
    while (n !== 1) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        sequence.push(n);
    }
    return sequence;
}

document.getElementById("plotButton").addEventListener("click", function () {
    const n = parseInt(document.getElementById("inputNumber").value);
    if (isNaN(n) || n <= 0) {
        alert("Please enter a positive integer.");
        return;
    }

    const sequence = collatz(n);

    const data = [{
        x: Array.from({ length: sequence.length }, (_, i) => i),
        y: sequence,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Collatz Sequence',
    }];

    const layout = {
        title: `Collatz Sequence for ${n}`,
        xaxis: { title: 'Step' },
        yaxis: { title: 'Value' },
    };

    Plotly.newPlot('plot', data, layout);
});
