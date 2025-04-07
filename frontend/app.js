// Fetch and render top 10 populous countries
fetch('../output/top_10_populous.json')
  .then(res => res.json())
  .then(data => {
    const labels = data.map(item => item["Country/Territory"]);
    const values = data.map(item => item["2022 Population"]);

    new Chart(document.getElementById('populousChart'), {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: '2022 Population',
          data: values,
          backgroundColor: 'rgba(75, 192, 192, 0.6)'
        }]
      },
      options: {
        indexAxis: 'y'
      }
    });
  });

// Fetch and render global population trend
fetch('../output/global_population_trend.json')
  .then(res => res.json())
  .then(data => {
    const labels = Object.keys(data);
    const values = Object.values(data);

    new Chart(document.getElementById('trendChart'), {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Global Population',
          data: values,
          borderColor: 'blue',
          fill: false
        }]
      }
    });
  });

// Pie chart: Population by continent
fetch('../output/population_by_continent.json')
  .then(res => res.json())
  .then(data => {
    const labels = Object.keys(data);
    const values = Object.values(data);

    new Chart(document.getElementById('continentChart'), {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: values,
          backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#32CD32', '#BA55D3', '#FFA07A']
        }]
      }
    });
  });

// Scatter plot: Area vs Population
fetch('../world_population.csv')
  .then(response => response.text())
  .then(csvText => {
    const rows = csvText.split('\n').slice(1);
    const points = rows.map(row => {
      const cols = row.split(',');
      return {
        x: parseFloat(cols[13]), // Area (km²)
        y: parseFloat(cols[5]),  // 2022 Population
        label: cols[2]           // Country/Territory
      };
    }).filter(p => !isNaN(p.x) && !isNaN(p.y));

    new Chart(document.getElementById('scatterChart'), {
      type: 'scatter',
      data: {
        datasets: [{
          label: 'Countries',
          data: points,
          backgroundColor: 'rgba(255, 99, 132, 0.5)'
        }]
      },
      options: {
        parsing: {
          xAxisKey: 'x',
          yAxisKey: 'y'
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: (context) => context.raw.label
            }
          }
        },
        scales: {
          x: { title: { display: true, text: 'Area (km²)' } },
          y: { title: { display: true, text: '2022 Population' } }
        }
      }
    });
  });
