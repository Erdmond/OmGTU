input_file = open('OLYMP\Tau\input_s1_01.txt')
input_string = input_file.readline()
input_file.close()
words = input_string.split(' ')
circular_list = []
if len(words) % 2 == 0:
    middle_index = len(words) // 2
    circular_list.append(words[middle_index])
    for i in range(1, middle_index + 1):
        circular_list.append(words[middle_index - i])
        if i < middle_index:
            circular_list.append(words[middle_index + i])
else:
    middle_index = (len(words) - 1) // 2
    circular_list.append(words[middle_index])
    for i in range(1, middle_index + 1):
        circular_list.append(words[middle_index - i])
        circular_list.append(words[middle_index + i])
palindrome_list = []
for word in circular_list:
    palindrome = ""
    if len(word) % 2 == 0:
        middle_index = len(word) // 2
        palindrome += word[middle_index]
        for i in range(1, middle_index + 1):
            palindrome += word[middle_index - i]
            if i < middle_index:
                palindrome += word[middle_index + i]
    else:
        middle_index = (len(word) - 1) // 2
        palindrome += word[middle_index]
        for i in range(1, middle_index + 1):
            palindrome += word[middle_index - i]
            palindrome += word[middle_index + i]
    palindrome_list.append(palindrome)
output_string = ""
for palindrome in palindrome_list:
    output_string += palindrome + " "

print(output_string[:-1])
