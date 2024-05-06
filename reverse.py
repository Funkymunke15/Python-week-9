# Davis Arita
# 11/7/22
# CS 131 Exercise 9 part B
# takes a file and reverses the lines of a text file

def main():
    infile = open("input.txt", "r")
    outfile = open("reverseOutput.txt", "w")
    data = []
    for line in infile:
        line = line.rstrip("\n")
        data.append(line)
    data = data[::-1]
    for i in data:
        print(i)
        print()

    outfile.write("\n".join(data))


main()
