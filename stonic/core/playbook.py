from stonic.syntax import load


class Playbook:

    def __init__(self, path=None):
        if path:
            self.load(path)

    def load(self, path):
        self._data = load(path)

    def run(self):
        print(self._data)
