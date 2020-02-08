def main():
    string = str(input("Write any string: "))
    count = 0
    #x = len(string)
    for letter in range(len(string)):
        count = count + 1
        print(string[count*-1])
        # The end of "for" loop
    str(input("Press enter to exit "))
    exit()
if __name__ == "__main__":
    main()
