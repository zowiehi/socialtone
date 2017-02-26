import React from 'react';
import queryString from 'query-string';
import Chart from 'chart.js';
import fetch from 'isomorphic-fetch';


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
      this.setState({ results: json, loaded: true })
    });
  }

  componentDidUpdate() {
    const avctx = document.getElementById('avChart');
    const pcctx = document.getElementbyId('pcChart');

    if (avctx) {
      const results = this.state.results;
      const avData = {
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

        var avChart = new Chart(avctx, {
          type: 'doughnut',
          data: avData,
          // options: options
        });
    }

    if (pcctx) {
      const results = this.state.results;

      const pcData = {
        labels: [
          "Negative",
          "Positive"
        ],
        datasets: [{
          data: [
            results.percent_negative * 100,
            results.percent_positive * 100
          ]
          backgroundColor: [
            "#a5dff9",
            "#a5dff9"
          ]
        }]
      };

      var pcChart = new Chart(pcctx, {
        type: 'bar',
        data: pcData
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
              <canvas id="pcChart" width="400px" height="400px"></canvas>
              <canvas id="avChart" width="400px" height="400px"></canvas>
            </div>
          </div>);
      }
      return (<div className="loader"></div>);
  }
}

export default App;
