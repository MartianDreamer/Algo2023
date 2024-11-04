import random
import sys
from typing import List


def random_array_int(lower:int, upper:int, lenght: int) -> List[int]:
    return [random.randint(lower, upper) for _ in range(lenght)]

def main():
    args = sys.argv
    if len(args) < 2:
        print("what do you want to generate? Be specific.\n")
        exit(1)
    generate_type = args[1]
    match generate_type:
        case "arr" | "a" | "array": 
            print(random_array_int(int(args[2]), int(args[3]), int(args[4])))
        case _:
            print("unsupported type")
            exit(1)

if __name__ == "__main__":
    main()