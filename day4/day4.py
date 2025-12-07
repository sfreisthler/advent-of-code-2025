def main():
    input_file="test.txt"

    with open(input_file, 'r') as file:
        line_count = sum(1 for line in file)
        line_length = len(file.readline().rstrip())
        arr = [[0] * line_length] * line_count
        i = 0
        for line in file:
             j = 0
             for char in line:
                  arr[i][j] = char

        print(arr)
                  
             



if __name__ == '__main__':
	main()