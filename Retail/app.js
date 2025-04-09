// Fetch and display EDA results
fetch('eda_results.json')
    .then(response => response.json())
    .then(data => {
        // Display summary data
        const summary = document.getElementById('summary');
        summary.innerHTML = `
            <li>Total Invoices: ${data.total_invoices}</li>
            <li>Canceled Orders: ${data.canceled_orders}</li>
            <li>Unique Products: ${data.unique_products}</li>
            <li>Total Revenue: $${data.total_revenue.toFixed(2)}</li>
            <li>Return Rate: ${(data.return_rate * 100).toFixed(2)}%</li>
        `;

        // Render charts using Chart.js
        renderSalesByCountryChart(data.sales_by_country);
        renderTopProductsChart(data.top_products);
    })
    .catch(error => console.error('Error fetching EDA results:', error));

// Render Sales by Country Chart
function renderSalesByCountryChart(salesByCountry) {
    const ctx = document.getElementById('salesByCountryChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(salesByCountry),
            datasets: [{
                label: 'Sales by Country',
                data: Object.values(salesByCountry),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'Country' } },
                y: { title: { display: true, text: 'Sales' } }
            }
        }
    });
}

// Render Top Products Chart
function renderTopProductsChart(topProducts) {
    const ctx = document.getElementById('topProductsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(topProducts),
            datasets: [{
                label: 'Top Products',
                data: Object.values(topProducts),
                backgroundColor: 'rgba(153, 102, 255, 0.6)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'Product Code' } },
                y: { title: { display: true, text: 'Frequency' } }
            }
        }
    });
}