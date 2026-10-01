
# import argparse

# parser = argparse.ArgumentParser(description="A simple command line utility.")
# parser.add_argument("file.txt", help="the file to process.")
# parser.add_argument("-n", "--number", type=int, default=1, help="number of times to repeat the output.")

# args = parser.parse_args()

# try:
#     with open(args.file.txt, "r", encoding="utf-8") as file:
#         content = file.read()
#         for _ in range(args.number):
#             print(content)
# except FileNotFoundError:
#     print("file not found")

import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add","sub", "div", "mul"], help="Operation to perform")

args = parser.parse_args()

# print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print("Some error occurred")
 