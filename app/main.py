import sys


def main():
    # nothing to see here, just making some Long Island iced tea 
    while True: #forever loop
        validCmds = ['', 'exit','echo']
        sys.stdout.write("$ ")
        cmd = input() # take input and return as str
        if False == cmd.startswith(('exit','echo')):
            print(f"{cmd}: command not found")
        elif cmd == 'exit':
            return exit # exit shell
        elif cmd.startswith(('echo')):
            print(f"{cmd[5:]}") # simple hardcoded skip

    #pass
    return 1


if __name__ == "__main__":
    main()
