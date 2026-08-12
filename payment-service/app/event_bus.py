# event_bus.py
import threading
from typing import Callable, Dict, List

class EventBus:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.subscribers = []
                    cls._instance.events = []
        return cls._instance

    def subscribe(self, callback: Callable):
        self.subscribers.append(callback)

    def publish(self, event: Dict):
        self.events.append(event)
        for callback in self.subscribers:
            callback(event)

    def get_events(self):
        return self.events

# Instância global (singleton)
event_bus = EventBus()