from setup import Setup

def main():
    min = int(input("How many minutes you want to extract information (integer number) :‌ "))
    iter = int(input("How many times do you want to do this :‌ "))
    start = Setup(min, iter)

main()