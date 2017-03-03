class StonicNode:
    pass


class HostsNode(StonicNode):
    tag = 'stonic:hosts'
    path = [(list, False)]
    kind = dict

    def __init__(self, loader, node):
        self._data = loader.construct_mapping(node)

    def __repr__(self):
        return 'hosts' + str(self._data)
