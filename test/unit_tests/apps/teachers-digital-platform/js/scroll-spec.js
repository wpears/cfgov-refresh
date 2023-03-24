import { jest } from '@jest/globals';
import scroll from '../../../../../cfgov/unprocessed/apps/teachers-digital-platform/js/scroll.js';

const HTML_SNIPPET = `
  <a class="one" href="#one" data-scroll>one</a>
  <a class="two" href="#two" data-scroll>two</a>
  <a class="three" href="#three" data-scroll>three</a>
  <div id="one"></div>
  <div id="two"></div>
  <div id="three"></div>
`;

/**
 * Helper function to simulate events
 *
 * @param eventType - {string} - The type of event to dispatch.
 * @param target - {HTMLElement} - The element to dispatch from.
 */
function simulateEvent(eventType, target) {
  const event = new MouseEvent(eventType, {
    bubbles: true,
    cancelable: true,
    view: window,
  });
  return target.dispatchEvent(event);
}

describe('Scroll', () => {
  beforeEach(() => {
    // Load HTML fixture
    document.body.innerHTML = HTML_SNIPPET;
    global.scroll = jest.fn();
    scroll.init();
  });

  afterEach(() => {
    document.body.innerHTML = '';
  });

  it('should update the URL when clicked', () => {
    const spy = jest.spyOn(global.history, 'pushState');

    scroll.init();
    const jumplink = document.querySelector('.one');

    simulateEvent('click', jumplink);

    expect(spy).toHaveBeenCalledWith(null, null, '#one');
  });
});
