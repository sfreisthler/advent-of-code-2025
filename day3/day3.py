NUM_DIGITS = 12

def findLargestJoltageNaive(input):
    length = len(input)
    maximum = 0
    for i in range(length-1):
        for j in range(i+1, length):
                cur = int(input[i] + input[j])
                maximum = max(maximum, cur)

    return maximum

def findLargestJoltage(input):
    length = len(input)
    selected_digits = 0
    digits_left = 12

    
    max_digit_pos = -1
    while(digits_left):
        max_digit = 0
        for i in range(max_digit_pos+1, length - digits_left + 1):
            if int(input[i]) > max_digit:
                max_digit = int(input[i])
                max_digit_pos = i
                
        digits_left -= 1
        selected_digits += (10 ** digits_left * max_digit)

    return selected_digits
            
      

def main():
    input_file="input.txt"
    sum = 0
    with open(input_file, 'r') as file:
          for line in file:
                sum += findLargestJoltage(line.rstrip())
    
    print(f"Sum: {sum}")


if __name__ == '__main__':
	main()