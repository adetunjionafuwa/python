#Create Node object for LinkedList
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def __repr__(self):
		return self.data


#Implement LinkedList Object
class LinkedList:
	def __init__(self, nodes = None):
		self.head = None

		if nodes is not None:
			#Pass first element in array into the node
			node = Node(data = nodes.pop(0))
			self.head = node

			#Handle remaining element in nodes
			for elem in nodes:
				node.next = Node(data = elem)
				node = node.next

	def __repr__(self):
		nodes = []
		node  = self.head
		while node is not None:
			nodes.append(str(node.data))
			node = node.next
		nodes.append('None')

		return '->'.join(nodes)

	def len(self):
		counter = 0
		node = self.head
		while node is not None:
			counter += 1
			node = node.next
		return counter

	def get_data_index(self, data):
		node = self.head
		counter = 0
		try:
			while node.data != data:
				counter += 1
				node = node.next
		except:
			raise Exception('Data not found')
		return counter

	def get_position(self, position):
		if position < 0:
			raise Exception('Invalid position found')

		counter  = 0
		node = self.head

		#bound loop in length of position
		while node is not None and counter<= position:
			if position == counter:
				return node.data
			node = node.next
			counter += 1
			
		raise Exception('Invalid position found')