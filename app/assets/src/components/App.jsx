import React from 'react';
import queryString from 'query-string';
import Chart from 'chart.js';



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {loaded: false, results: null};
  }

  componentDidMount() {
    const query = queryString.parse(location.search);
    fetch(`/api?search=${query.s}`)
    .then(response => response.json())
    .then(json => {
      console.log(json);
      this.setState({ results: json, loaded: true })
    });
  }

  componentDidUpdate() {
    const ctx = document.getElementById('myChart');
    if (ctx) {
      const results = this.state.results;
      const chartData = {
        labels: [
          "Positive",
          "Anger",
          "Sadness",
          "Disgust"
        ],
        datasets: [{
          data: [
            results.positive * 100,
            results.anger * 100,
            results.sadness * 100,
            results.disgust * 100
          ],
          backgroundColor: [
            "#60c5ba",
            "#ef5285",
            "#a5dff9",
            "#feee7d"
          ]}]
        };

        var toneChart = new Chart(ctx, {
          type: 'doughnut',
          data: chartData,
          // options: options
        });
    }
  }

  render() {
      if (this.state.loaded) {
        const top_tweets = this.state.results.top_tweets;
        return (
          <div>
            {top_tweets.map(tweet => (<div dangerouslySetInnerHTML={{__html: tweet}}></div>))}
            <div id="chart-box">
              <canvas id="myChart" width="400px" height="400px"></canvas>
            </div>
          </div>);
      }
      return (<div className="loader"></div>);
  }
}

export default App;
