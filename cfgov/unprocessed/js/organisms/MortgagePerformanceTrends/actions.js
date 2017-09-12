'use strict';

var utils = require( './utils' );

var actions = {};

actions.setGeo = ( geoId, geoName, geoType ) => ( {
  type: 'SET_GEO',
  geo: {
    type: geoType,
    id: geoId,
    name: geoName
  }
} );

actions.clearGeo = () => ( {
  type: 'CLEAR_GEO'
} );

actions.updateChart = ( geoId, geoName, geoType, includeNational ) => {
  var action = {
    type: 'UPDATE_CHART',
    geo: {
      id: geoId,
      name: geoName
    },
    includeNational
  };
  if ( geoType ) {
    action.geo.type = geoType;
  }
  return action;
};

actions.updateNational = includeNational => {
  var action = {
    type: 'UPDATE_CHART',
    includeNational
  };
  return action;
};

actions.updateDate = date => ( {
  type: 'UPDATE_DATE',
  date: date
} );

actions.requestCounties = () => ( {
  type: 'REQUEST_COUNTIES',
  isLoadingCounties: true
} );

actions.requestMetros = () => ( {
  type: 'REQUEST_METROS',
  isLoadingMetros: true
} );

actions.requestNonMetros = () => ( {
  type: 'REQUEST_NON_METROS',
  isLoadingNonMetros: true
} );

actions.fetchMetros = ( metroState, includeNational ) => dispatch => {
  dispatch( actions.requestMetros( metroState ) );
  return utils.getMetroData( ( err, data ) => {
    if ( err ) {
      return console.error( 'Error getting metro data', err );
    }
    // Alphabetical order
    var newMetros = data[metroState].metros.sort( ( a, b ) => a.name < b.name ? -1 : 1 );
    newMetros = newMetros.filter( metro => metro.valid );
    dispatch( actions.setMetros( newMetros ) );
    dispatch( actions.setGeo( newMetros[0].fips, newMetros[0].name, 'metro' ) );
    dispatch( actions.updateChart( newMetros[0].fips, newMetros[0].name, 'metro', includeNational ) );
    return newMetros;
  } );
};

actions.fetchNonMetros = ( nonMetroState, includeNational ) => dispatch => {
  dispatch( actions.requestNonMetros( nonMetroState ) );
  return utils.getNonMetroData( ( err, data ) => {
    if ( err ) {
      return console.error( 'Error getting non-metro data', err );
    }
    // Alphabetical order
    var newNonMetros = data[nonMetroState].nonmetros.sort( ( a, b ) => a.name < b.name ? -1 : 1 );
    newNonMetros = newNonMetros.filter( nonmetro => metro.valid );
    dispatch( actions.setNonMetros( newNonMetros ) );
    dispatch( actions.setGeo( newNonMetros[0].non_fips, newNonMetros[0].state_name, 'non-metro' ) );
    dispatch( actions.updateChart( newNonMetros[0].non_fips, newNonMetros[0].state_name, 'non-metro', includeNational ) );
    return newNonMetros;
  } );
};

actions.fetchCounties = ( countyState, includeNational ) => dispatch => {
  dispatch( actions.requestCounties( countyState ) );
  return utils.getCountyData( ( err, data ) => {
    if ( err ) {
      return console.error( 'Error getting county data', err );
    }
    // Alphabetical order
    var newCounties = data[countyState].counties.sort( ( a, b ) => a.name < b.name ? -1 : 1 );
    newCounties = newCounties.filter( county => county.valid );
    dispatch( actions.setCounties( newCounties ) );
    dispatch( actions.setGeo( newCounties[0].fips, newCounties[0].name, 'county' ) );
    dispatch( actions.updateChart( newCounties[0].fips, newCounties[0].name, 'county', includeNational ) );
    return newCounties;
  } );
};

actions.setMetros = metros => ( {
  type: 'SET_METROS',
  metros: metros
} );

actions.setNonMetros = nonmetros => ( {
  type: 'SET_NON_METROS',
  nonmetros: nonmetros
} );

actions.setCounties = counties => ( {
  type: 'SET_COUNTIES',
  counties: counties
} );

actions.startLoading = () => ( {
  type: 'START_LOADING',
  isLoading: true
} );

actions.stopLoading = () => ( {
  type: 'STOP_LOADING',
  isLoading: false
} );

module.exports = actions;
