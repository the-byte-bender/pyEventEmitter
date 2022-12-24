# EventEmitter

A Python implementation of the Node.js EventEmitter class.

## Features

- Register event listeners using the `on` and `once` methods
- Remove event listeners using the `off` method
- Remove all event listeners for a specific event or for all events using the `remove_all_listeners` method
- Get a list of all event listeners for a specific event using the `listeners` method
- Trigger events using the `emit` method

## Installation

To install the `EventEmitter` class:

` pip install git+https://github.com/meatbag93/pyEventEmitter`

## Usage

To use the `EventEmitter` class, create an instance of it and then use the `on`, `once`, and `emit` methods to register event listeners and trigger events:

```python
from event_emitter import EventEmitter

emitter = EventEmitter()

# Register an event listener using the on method
def event_handler(arg1, arg2):
    print(f'event_name triggered with arguments: {arg1}, {arg2}')
emitter.on('event_name', event_handler)

# Register an event listener using the once method
def event_handler_once(arg1, arg2):
    print(f'event_name triggered once with arguments: {arg1}, {arg2}')
emitter.once('event_name', event_handler_once)

# Trigger the event
emitter.emit('event_name', 'arg1 value', 'arg2 value')
emitter.emit('event_name', 'arg1 value', 'arg2 value')
```

More methods are available. They all have proper docstrings.