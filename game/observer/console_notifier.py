# Console notifier implementation

from observer.iobserver import IObserver

class ConsoleNotifier(IObserver):
    def update(self, msg):
        print(f"[NOTIFICATION] {msg}")

