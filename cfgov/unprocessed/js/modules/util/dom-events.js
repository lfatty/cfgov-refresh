/**
 * Shortcut for binding event listeners to elements.
 * @param  {HTMLNode} elem   The element to attach the event listener to.
 * @param  {Object}   events The list of events to attach to the element.
 */
function bindEvent( elem, events ) {
  let callback;

  let event;
  for ( event in events ) {
    if ( events.hasOwnProperty( event ) ) {
      callback = events[event];
      elem.addEventListener( event, callback );
    }
  }
}

export {
  bindEvent
};
