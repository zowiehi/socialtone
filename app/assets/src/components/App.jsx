import React from 'react';
import queryString from 'query-string';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {loaded: false, results: null};
  }

  componentDidMount() {
    const query = queryString.parse(location.search);
    fetch(`/api?search=${query.s}`)
    .then(response => response.json())
    .then(json => this.setState({ results: json, loaded: true }));
  }

  render() {
      if (this.state.loaded) {
        return (<h1>{ this.state.results }</h1>);
      }
      return (<div className="loader"></div>);
  }
}

export default App;
