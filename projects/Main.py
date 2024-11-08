import sys


print("Wrong run config!\n")
print()


def menu():
    print("1. To do list")
    print("2. Sentencebot")
    print("3. Contact manager")
    print("4. Personal diary")
    print("5. Online boardgame store")


def main():
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted\n")
        sys.exit(130)
