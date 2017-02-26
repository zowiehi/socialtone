var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: {
    app: './src/init.js',
    vendor: ['react', 'react-dom', 'chart.js', 'query-string']
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendor', '../static/js/vendor.bundle.js'),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: { warnings: false }
    }),
    new webpack.NoErrorsPlugin(),
  ],
  output: {
    path: __dirname,
    filename: '../static/js/bundle.js'
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  module: {
    loaders: [
      {
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  },
};
