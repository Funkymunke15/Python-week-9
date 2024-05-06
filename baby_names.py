# Davis Arita
# 11/7/22
# Cs 131 Exercise 9 part C
# separates boy and girl names and prints the 10 most popular of each

def readData():
    infile = open("babynames.txt", "r")
    boyOut = open("boynames.txt", "w")
    girlOut = open("girlnames.txt", "w")

    for name in infile:
        data = name.split()
        boyOut.write("\n" + data[0] + "\t" + data[1] +
                     "\t" + data[2])
        girlOut.write("\n" + data[0] + "\t" + data[3] +
                      "\t" + data[4])
    infile.close()
    boyOut.close()
    girlOut.close()


def main():
    readData()
    with open("babynames.txt") as myfile:
        head = [next(myfile) for x in range(10)]
    boys = []
    girls = []
    for name in head:
        data = name.split()
        boys.append(data[1])
        girls.append(data[3])

    print("Top 10 most popular baby boy names for 2011: ")
    for i in boys:
        print(i)

    print("\nTop 10 most popular baby girl names for 2011: ")
    for i in girls:
        print(i)


main()



