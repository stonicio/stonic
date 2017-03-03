import yaml

from stonic.syntax.node import HostsNode


class StonicLoaderMeta(type):

    def __new__(cls, name, bases, attrs):
        nodes = attrs.pop('nodes', [])

        klass = super().__new__(cls, name, bases, attrs)

        for node in nodes:
            klass.add_path_resolver(node.tag, node.path, node.kind)
            klass.add_constructor(node.tag, node)

        return klass


class StonicLoader(yaml.Loader, metaclass=StonicLoaderMeta):
    def __init__(self, path):
        super().__init__(open(path))


class PlaybookLoader(StonicLoader):
    nodes = [HostsNode]


def load(path):
    return yaml.load(path, PlaybookLoader)
