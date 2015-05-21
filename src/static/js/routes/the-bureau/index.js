/* ==========================================================================
   Bureau structure.
   Scripts for `/the-bureau/`.
   ========================================================================== */

'use strict';

var $ = require( 'jquery' );
require( 'slick' );

var breakpointHandler = require( '../../modules/breakpoint-handler' );
var BreakpointHandler = breakpointHandler.BreakpointHandler;
var MobileOnlyExpandable = breakpointHandler.MobileOnlyExpandable;

function init() {
  if ( !$( 'html' ).hasClass( 'lt-ie9' ) ) {
    var bureauMissionDom = $( '.bureau-mission' );
    var handler = new BreakpointHandler( {
      breakpoint: 599,
      type:       'max',
      enter:      _enterBreakpoint,
      leave:      _leaveBreakpoint
    } );

    $( '.expandable__mobile-only' ).each( function() {
      handler = new MobileOnlyExpandable( $( this ), 599 );
    } );
  }

  function _enterBreakpoint() {
    bureauMissionDom.slick( {
      dots: true
    } );
  }

  function _leaveBreakpoint() {
    bureauMissionDom.unslick();
  }
}

module.exports = { init: init };
