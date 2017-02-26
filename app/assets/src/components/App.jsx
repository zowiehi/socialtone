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
    this.setState({ query: query.s });
    fetch(`/api?search=${query.s}`)
    .then(response => response.json())
    .then(json => {
      this.setState({ results: json, loaded: true })
    });
  }

  componentDidUpdate() {
    const avctx = document.getElementById('avChart');
    const pcctx = document.getElementById('pcChart');

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
          label: 'Percent Sentiment',
          data: [
            results.percent_negative * 100,
            results.percent_positive * 100
          ],
          backgroundColor: [
            "#ef5285",
            "#60c5ba"
          ]
        }]
      };

      var pcChart = new Chart(pcctx, {
        type: 'horizontalBar',
        data: pcData,
        options: {
        scales: {
            xAxes: [{
              stacked: true
            }],
            yAxes: [{
              stacked: true
            }]
          }
        }
      });
    }


  }

  render() {
      if (this.state.loaded) {
        const top_tweets = this.state.results.top_tweets;
        return (
          <div>
            <div id="top-tweets" class='col-md-6 col-xs-12'>
              <h1>Top Tweets for {`${this.state.query}`}</h1>
              {top_tweets.map(tweet => (<div dangerouslySetInnerHTML={{__html: tweet}}></div>))}
            </div>
            <div id="chart-box" class="row">
              <h1>Social Sentiment</h1>
              <div id="average-box" className="col-md-6 col-xs-12">
                <canvas id="avChart" width="400px" height="400px"></canvas>
              </div>
              <div id="percent-box" className="col-md-6 col-xs-12">
                <canvas id="pcChart" width="400px" height="400px"></canvas>
              </div>
            </div>
          </div>
        );
      }
      return (<div className="loader"></div>);
  }
}

export default App;
