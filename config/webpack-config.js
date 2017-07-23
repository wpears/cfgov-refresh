/* ==========================================================================
   Settings for webpack JavaScript bundling system.
   ========================================================================== */

'use strict';

const BannerFooterPlugin = require( 'banner-footer-webpack-plugin' );
const path = require( 'path' );
const environment = require( '../config/environment' );
const paths = environment.paths;
const scriptsManifest = require( '../gulp/utils/scripts-manifest' );
const webpack = require( 'webpack' );

// Constants.
const JS_ROUTES_PATH = '/js/routes';
const COMMON_BUNDLE_NAME = 'common.js';
const OAH_COMMON_BUNDLE_ROUTE = '/js/owning-a-home/routes';


const babelConf = {
  test: /\.js$/,
  use: [ {
    loader: 'babel-loader?cacheDirectory=true',
    options: {
      presets: [ [ 'env', {
        targets: {
          browsers: environment.getSupportedBrowserList()
        }
      } ] ]
    }
  } ],
  exclude: /node_modules/
};

const modernConf = {
  cache: true,
  context: path.join( __dirname, '/../', paths.unprocessed, JS_ROUTES_PATH ),
  entry: scriptsManifest.getDirectoryMap( paths.unprocessed + JS_ROUTES_PATH ),
  module: {
    rules: [ babelConf ]
  },
  output: {
    path: path.join( __dirname, 'js' ),
    filename: '[name]'
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin( {
      name: COMMON_BUNDLE_NAME
    } ),
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } ),
    // Wrap JS in raw Jinja tags so included JS won't get parsed by Jinja.
    new BannerFooterPlugin( '{% raw %}', '{% endraw %}', { raw: true } )
  ]
};

const ieConf = {
  entry: paths.unprocessed + '/js/ie/common.ie.js',
  output: {
    filename: 'common.ie.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } )
  ]
};

const externalConf = {
  entry: paths.unprocessed + JS_ROUTES_PATH + '/external-site/index.js',
  output: {
    filename: 'external-site.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } )
  ]
};

const onDemandConf = {
  context: path.join( __dirname, '/../', paths.unprocessed,
                      JS_ROUTES_PATH + '/on-demand' ),
  entry:   scriptsManifest.getDirectoryMap( paths.unprocessed +
                                            JS_ROUTES_PATH + '/on-demand' ),
  output: {
    path:     path.join( __dirname, 'js' ),
    filename: '[name]'
  },
  plugins: [
    // Change warnings flag to true to view linter-style warnings at runtime.
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } )
  ]
};

const onDemandHeaderRawConf = {
  context: path.join( __dirname, '/../', paths.unprocessed,
                      JS_ROUTES_PATH + '/on-demand' ),
  entry:   './header.js',
  output: {
    path:     path.join( __dirname, 'js' ),
    filename: '[name]'
  }
};

const spanishConf = {
  entry: paths.unprocessed + JS_ROUTES_PATH + '/es/obtener-respuestas/single.js',
  output: {
    filename: 'spanish.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } )
  ]
};

var owningAHomeConf = {
  cache: true,
  context: path.join( __dirname, '/../', paths.unprocessed, OAH_COMMON_BUNDLE_ROUTE ),
  entry: scriptsManifest.getDirectoryMap( paths.unprocessed + OAH_COMMON_BUNDLE_ROUTE ),
  module: {
    rules: [ babelConf,
             { test: /\.(hbs|handlebars)$/, loader: 'handlebars-loader' }
    ]
  },
  output: {
    path: path.join( __dirname, 'js' ),
    filename: '[name]',
    jsonpFunction: 'OAH'
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin( {
      name: COMMON_BUNDLE_NAME
    } ),
    new webpack.optimize.UglifyJsPlugin( {
      compress: { warnings: false }
    } )
  ]
};

module.exports = {
  onDemandHeaderRawConf: onDemandHeaderRawConf,
  owningAHomeConf:       owningAHomeConf,
  onDemandConf:          onDemandConf,
  ieConf:                ieConf,
  modernConf:            modernConf,
  externalConf:          externalConf,
  spanishConf:           spanishConf
};
