import sys

if __name__ == "__main__":
    def command_quest():
        """This function recive n input parameters, """
        """display them, and how many they are"""

        print("=== Command Quest ===")
        args = sys.argv
        total = len(args)
        i = 1
        if total == 1:
            print("No arguments provided!")
        print(f"Program name: {args[0]}")
        if total > 1:
            print(f"Arguments received: {total -1}")
            for arg in args:
                print(f"Argument {i}: {args[i]}")
        print(f"Total arguments: {total}")
