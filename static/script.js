// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to create a Chart.js chart and a description text
    function createChart(data) {
        const description = data[2]['description']
        const para = document.createElement("p");
        const node = document.createTextNode(description);
        para.appendChild(node);

        const element = document.getElementById('description');
        element.appendChild(para);

        const labels = [data[0]].map(point => point.y)[0];
        const values = [data[0]].map(point => point.x)[0];

        const ctx = document.getElementById('myChart2').getContext('2d');
        const netincome = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Net Income',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    x: { type: 'linear', position: 'bottom' },
                    y: { beginAtZero: true }
                }
            }
        });
        const labels1 = [data[1]].map(point => point.y)[0];
        const values1 = [data[1]].map(point => point.x)[0];

        const ctx1 = document.getElementById('myChart1').getContext('2d');
        const revenue = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: labels1,
                datasets: [{
                    label: 'Revenue',
                    data: values1,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    x: { type: 'linear', position: 'bottom' },
                    y: { beginAtZero: true }
                }
            }
        });
    }

    // Show Chart button functionality
    const showData = document.getElementById('showData');
    showData.addEventListener('click', function() {
        // Hide section that asks for symbol
        document.getElementById('getinput').style.display = 'none'

        // Get input from the user
        quote = document.querySelector("#symbol")
        
        // Fetch data from the server when the page loads
        fetch('/get_data', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(quote.value.toUpperCase())
          })

          // Display chart on the page
            .then(response => response.json())
            .then(data => createChart(data))
            .catch(error => console.error('Error fetching data:', error));
    });
});
