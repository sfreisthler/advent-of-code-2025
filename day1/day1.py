class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.cur_pos = self.head
	
	def append(self, data):
		new_node = Node(data)
		if not self.head:
			new_node.next = new_node
			new_node.prev = new_node
			self.head = new_node
		else:
			cur = self.head
			while (cur.next != self.head):
				cur = cur.next
			
			cur.next = new_node
			new_node.next = self.head
			new_node.prev = cur
			self.head.prev = new_node
	def find(self, value):
		cur = self.head
		if cur is None:
			return None
		while True:
			if cur.data == value:
				return cur
			cur = cur.next
			if cur == self.head:
				break
		return None
	
	def print(self):
		cur = self.head
		while (cur.next != self.head):
			print(f"Data: {cur.data}, Next: {cur.next.data}, Prev: {cur.prev.data}")
			cur = cur.next
		
		print(cur.data)

class Lock:
	def __init__(self):
		self.lock = CircularLinkedList()
		for i in range(100):
			self.lock.append(i)
		self.cur_pos = self.lock.find(50)
	
	def rotateLeft(self, number):
		if self.cur_pos == None:
			self.cur_pos = self.head
		
		for i in range (number):
			self.cur_pos = self.cur_pos.prev

	def rotateRight(self, number):
		if self.cur_pos == None:
			self.cur_pos = self.head
		
		for i in range (number):
			self.cur_pos = self.cur_pos.next
	
	def checkZero(self):
		return self.cur_pos.data == 0


def main():
	input_file = 'input.txt'
	count = 0
	# create circular linked list with 99 nodes
	lock = Lock()

	# read input line by line
	with open(input_file, 'r') as file:
		for line in file:
			direction = line[0]
			number = int(line[1:])

			if direction == 'L':
				lock.rotateLeft(number)
			else:
				lock.rotateRight(number)

			# if lands on 0, add 1 to counter
			if lock.checkZero():
				count += 1
	
	print(f"Password: {count}")

if __name__ == '__main__':
	main()