from typing import List
import argparse

def singleton(ls: List[int]) -> int:
  length: int = len(ls)
  midpoint: int = (int) (length / 2);
  print(f"list: {ls}")
  print(f"midpoint: {midpoint} -> {ls[midpoint]}")
  
  if (midpoint == 0):
    return ls[midpoint]
  if ((ls[midpoint - 1] != ls[midpoint]) and (ls[midpoint + 1] != ls[midpoint])):
    return ls[midpoint]
  else:
    if (ls[midpoint - 1] == ls[midpoint]):
      if ( midpoint % 2 == 0):
        print("left")
        return singleton(ls[:(midpoint + 1)])
      else:
        print("right")
        return singleton(ls[midpoint + 1:])
    else:
      if(((length - midpoint) % 2) == 0):
        print("left")
        return singleton(ls[:(midpoint)])
      else:
        print("right")
        return singleton(ls[midpoint:])

def main(filename):
  numbers: List[int] = []
  try:
    with open(filename, "r") as file:
       for line in file:
          numbers.append(int(line.strip()))
    print(numbers)
    print(singleton(numbers))
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit(1)
  except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Open a file filled with lists of integers and print the singletons in each list.")
  parser.add_argument("filename", help="The file to be processed")
  args = parser.parse_args()

  # Check if there's only one argument provided
  if len(args.__dict__) != 1:
    parser.print_usage()
    exit(1)

# Call main function with the parsed argument
  main(args.filename)

