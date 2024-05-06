# file reading

def main():
    infile = open("numbers.txt", "r")
    outfile = open("output.txt", "w")
    total = 0
    count = 0
    line = infile.readline()
    while line != "":
        total += float(line)
        print(line, end="")
        outfile.write(line)
        count += 1
        line = infile.readline()
    print()
    print(total)
    avg = total/count
    print(avg)
    outfile.write("\nNumber of entries: %d\nTotal: %8.2f\n" % (count, total))
    outfile.write("Average of elements: %8.2f" % avg)
    infile.close()
    outfile.close()


main()