# main.py — this now integrates obscure.py



# import obscure output generator
from obscure import print_obscure

def main():
    print("Running main operation…\n")

    print_obscure()  # <-- here is your foreign output
    print("Main completed.\n")

if __name__ == "__main__":
    main()
