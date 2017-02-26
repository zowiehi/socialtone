var toneChart = new Chart(ctx, {
    type: 'doughnut',
    data: chartData,
    options: options
});

chartData = {
  labels: [
    "Positive",
    "Anger",
    "Sadness",
    "Disgust"
  ],
  datasets: [
  {
    data: [results.positive_average,
           results.anger_average,
           results.sadness_average,
           results.disgust_average]
    backgroundColor: ["#0b8a46",
                      "#ce1126",
                      "#003893",
                      "#fcd116"

                      ]
  }]
};
