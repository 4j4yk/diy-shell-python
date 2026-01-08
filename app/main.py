import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: #forever loop
        sys.stdout.write("$ ")
        cmd = input() # take input and return as str
        if cmd != 'exit':
            print(f"{cmd}: command not found")
        if cmd == 'exit':
            return exit
    #pass
    return 1


if __name__ == "__main__":
    main()
