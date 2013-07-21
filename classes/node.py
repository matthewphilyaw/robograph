class Node:
    def __init__(self, data):
        self.incoming_edges = {}
        self.outgoing_edges = {}
        self.data = data

    def add_outgoing_edge(self, node, meta):
        """
            Inserts outgoing edge if doesn't exist with meta data
            else does nothing
        """
        self._update_dict(self.outgoing_edges, node, meta)

    def add_incoming_edge(self, node, meta):
        """
            Inserts outgoing edge if doesn't exist with meta data
            else does nothing
        """
        self._update_dict(self.incoming_edges, node, meta)

    def _update_dict(self, dict, node, meta):
        if node not in dict:
            dict[node] = meta

    def remove_edge(self, node):
        if node == None:
            return

        if node != self:
            node.remove_edge(self)

        if node in self.incoming_edges:
            del self.incoming_edges[node]

        if node in self.outgoing_edges:
            del self.outgoing_edges[node]

    def remove_all_edges(self):
        for k,v in self.outgoing_edges.items():
            k.remove_edge(self)
            del self.outgoing_edges[k]
        for k,v in self.incoming_edges.items():
            k.remove_edge(self)
            del self.outgoing_edges[k]

    def get_incoming_edge_data(self, node):
        if node in self.incoming_edges:
            return self.incoming_edges[node]

    def get_incoming_edges(self):
        return self.incoming_edges.items()

    def get_outgoing_edge_data(self, node):
        if node in self.outgoing_edges:
            return self.outgoing_edges[node]

    def get_outgoing_edges(self):
        return self.outgoing_edges.items()
