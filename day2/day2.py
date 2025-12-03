def validId1(id):
	length = len(id)

	if (length % 2) == 1:
		return True

	left = 0
	right = length // 2

	while right < length:
		if (id[left] != id[right]):
			return True

		left += 1
		right += 1
	
	return False

def validId2(id):
	length = len(id)

	for i in range(1,(length // 2) + 1):
		if not length % i:
			substring = id[0:i]
			mult = length // i

			if ((substring * mult) == id):
				return False
	return True


def countInvalidIds1(start, end):
	count = 0
	for i in range (start, end + 1):
		if not validId1(str(i)):
			count += i
	return count

def countInvalidIds2(start, end):
	count = 0
	for i in range (start, end + 1):
		if not validId2(str(i)):
			count += i
	return count

def main():
	input_file = "input.txt"
	count1 = 0
	count2 = 0
	with open(input_file, 'r') as file:
		for line in file:
			ranges = line.split(',')
			for range in ranges:
				limits = range.split('-')
				start = int(limits[0])
				end = int(limits[1])
				count1 += countInvalidIds1(start,end)
				count2 += countInvalidIds2(start,end)
	
	print(f"Final count part1: {count1}")
	print(f"Final count part2: {count2}")


if __name__ == '__main__':
	main()