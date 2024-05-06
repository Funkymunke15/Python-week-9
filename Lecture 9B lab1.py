# Davis Arita
# 10/26/22
# CS 131 Lecture 9B lab1
# ask the user for a file name and prints the number of characters, words, and lines

def main():
    infile = open(input("Enter file name: "), "r")
    outfile = open("9BLab1_output.txt", "w")

    num_words = 0
    num_lines = 0
    num_char = 0

    char_data = infile.read()
    char_data.rstrip("\n")
    num_char = len(char_data)
    word_data = char_data.splitlines()
    num_lines = len(word_data)

    for line in word_data:
        temp_word = line.split()
        for i in temp_word:
            num_words += 1

    print("The file contains %d characters, %d words, and %d lines" % (num_char, num_words,
                                                                       num_lines))


main()