# Davis Arita
# 10/24/22
# CS 131 Lecture 9A lab 1
# reads a file containing two columns of floating point numbers and averages each column

def main():
    infile = open(input("Enter file name: "), "r")
    outfile = open("lab1output.txt", "w")

    line = infile.readline()
    totalA = 0
    totalB = 0
    count = 0
    for line in infile:
        parts = line.split()
        totalA += float(parts[0])
        totalB += float(parts[1])
        count += 1
    totalA /= count
    totalB /= count
    print("first column: %8.2f\nSecond column: %8.2f" % (totalA, totalB))
    outfile.write("first column: %8.2f\nSecond column: %8.2f" % (totalA, totalB))


main()
