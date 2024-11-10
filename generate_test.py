import random
import sys
from typing import List


def random_array_int(lower:int, upper:int, lenght: int) -> List[int]:
    return [random.randint(lower, upper) for _ in range(lenght)]

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: What do you want to generate? Be specific.\n")
        exit(1)
    generate_type = args[1]
    match generate_type:
        case "arr" | "a" | "array":
            if len(args) < 5:
                print("Usage: You need 3 parameters in following order lowerbound upperbound length.\n")
                exit(1)
            print(random_array_int(int(args[2]), int(args[3]), int(args[4])))
        case _:
            print("unsupported type")
            exit(1)

if __name__ == "__main__":
    main()