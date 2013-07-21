class Graph:
	def __init__(self):
		self.nodes = {}

	def find_node(self, heading):
		if heading in self.nodes:
			return self.nodes[heading]

		return None

	def add_node(self, node):
		if node.data.heading in self.nodes:
			raise Exception("node already exists")

		self.nodes[node.data.heading] = node

	def remove_node(self, node):
		node.remove_all_edges()	
		del self.nodes[node]
