##All methods are complexity O(n)... I do not think they can me improved because it is neessary to review the whole list before doing any change

class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next

	def __str__(self):
		return str(self.value)

class LinkedList():
	def __init__(self, value):
		self.main_node = Node(_value=value) 
		self.next_node = self.main_node
		self.length = 1	

	def __str__(self):
		node = self.main_node
		finalList = ""
		while node is not None:
			if node.next is not None: 
				finalList += str(node.value) + "->"
			else: 
				finalList += str(node.value)
			node = node.next
		return finalList
		

	def length(self):
		print "The length of your list is %d" % self.length
		return self.length

	def addNode(self, new_value):
		new_node = Node(new_value)
 		new_node.value = new_value
		if self.main_node.value == None:
			self.main_node = new_node
			self.next_node = new_node
		else:
			self.next_node.next = new_node
			self.next_node = new_node
		self.length += 1


	def addNodeAfter(self, new_value, after_node):
		if after_node > self.length:
			print "Node %d does not exist" % after_node
		else:
			temp_node = self.main_node
			pos = 1
			while pos != after_node:
				temp_node = temp_node.next
				pos += 1
			temp_node.next = Node(new_value, temp_node.next)
			self.length += 1

	def addNodeBefore(self, new_value, before_node):
		if before_node == 1:
			print "No nodes before the head"
		else:
			self.addNodeAfter(new_value, before_node-1)

	def removeNode(self, node_to_remove=None):
		if node_to_remove > self.length:
			print "Node %d does not exist" % node_to_remove
		elif node_to_remove == 1:
			self.main_node = None
		else:
			temp_node = self.main_node
			temp_next = temp_node.next
			pos = 0
			while pos != (node_to_remove-2):
				temp_node = temp_node.next
				temp_next = temp_node.next
				pos += 1
			temp_node.next = None
			temp_node.next = temp_next.next
			self.length -= 1

	def removeNodesByValue(self, value):
		if self.main_node.value == value:
			print "Value in head. Head will not be removed"
			pass
		pos = 2
		count = 2
		temp_node = self.main_node.next
		while temp_node.next != None:
			if temp_node.value == value:
				self.removeNode(count)
				temp_init = temp_node.value
				temp_node = temp_node.next
				count -=1
				self.length -= 1
			else:
				temp_init = temp_node.value
				temp_node = temp_node.next
			pos += 1
			count +=1
			if temp_init == value: 
				self.removeNode(count)
		if count == pos:
			print "Value not found"

	def getValue(self, number_node):
		temp_node = self.main_node
		pos = 0
		while pos != number_node:
			temp_value = temp_node.value
			temp_node = temp_node.next
			pos += 1
		return temp_value

	def reverse(self):
		#current_node = self.main_node
		size_orig = self.length
		new_node = LinkedList(self.getValue(self.length))
		for i in range(1, size_orig):
			new_value = self.getValue(size_orig-i)
			new_node.addNode(new_value)
		print new_node




