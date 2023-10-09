class _CircularLinkedList:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = next
	def __init__(self):
		self.head = None

	def run(self, player_1, player_2):
		head = self.head

		node = self.Node(player_1)
		head = node

		node_1 = self.Node(player_2)
		node.next = node_1
		node_1.next = head
		return head

circular_list = _CircularLinkedList()
