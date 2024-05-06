# Davis Arita
# 10/24/ 22
# CS 131 Exercises 9 part A
# takes in a set of floating-point numbers, stops when user inputs not-a-number twice
# prints sum of inputted numbers

def main():
    ans = 0

    flag = 0
    done = True
    while done:
        try:
            x = input("Enter a number, or 2 non-numbers to quit: ")
            y = float(x)
            ans += y
        except ValueError:
            flag = 1
        if flag == 1:
            x = input("Enter a number, or another non-number to quit: ")
            flag = 0
            try:
                y = float(x)
                ans += y
            except ValueError:
                done = False
    print("The total is", ans)


main()
