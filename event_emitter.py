class EventEmitter:
    def __init__(self):
        self.events = {}

    def add_listener(self, event_name, callback):
        """
        Add a callback for the given event.

        :param event_name: The name of the event to listen for
        :param callback: The function to be called when the event is emitted
        """
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(callback)

    def on(self, event_name, callback):
        """
        Add a callback for the given event.

        :param event_name: The name of the event to listen for
        :param callback: The function to be called when the event is emitted
        """
        self.add_listener(event_name, callback)

    def once(self, event_name, callback):
        """
        adds a listener to an event which will be removed  after it's been called once

        :param event_name: The name of the event to listen for
        :param callback: The function to be called when the event is emitted
        """

        def wrapper(*args, **kwargs):
            self.remove_listener(event_name, wrapper)
            callback(*args, **kwargs)

        self.add_listener(event_name, wrapper)

    def remove_listener(self, event_name, callback):
        """
        Remove a given callback from the  given event.

        :param event_name: The name of the event
        :param callback: The function that is listening to this event
        """
        if event_name in self.events:
            self.events[event_name] = [
                cb for cb in self.events[event_name] if cb != callback
            ]

    def off(self, event_name, callback):
        """
        Remove a given callback from the  given event.

        :param event_name: The name of the event
        :param callback: The function that is listening to this event
        """
        self.remove_listener(event_name, callback)

    def remove_all_listeners(self, event_name=None):
        """
        Removes all listeners for a given event, or all listeners for all events.

        :param event_name: The name of the event to listen for. Default None. If None, removes all event listeners for all events
        """
        if event_name is not None:
            self.events[event_name] = []
        else:
            self.events = {}

    def listeners(self, event_name):
        """
        It returns a list of functions that are registered to be called when the event named `event_name` is
        emitted

        :param event_name: The name of the event
        :return: A list of listeners for the event_name.
        """
        return self.events.get(event_name, [])

    def emit(self, event_name, *args, **kwargs):
        """Triggers the specified event, calling all registered event listeners."""
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)
