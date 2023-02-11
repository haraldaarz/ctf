from pwn import *
import math

conn = remote("motherload.td.org.uit.no", 8010)
conn.recvuntil(b"Ready?")
conn.sendline(b"Yup")
conn.recvline()


# Implement your solution here
i = 0

while i < 300:

    mathProblem = conn.recvline()
    print("problem:", str(mathProblem))

    mathProblem = str(mathProblem)[2:-3]  # Remove the b' and n from the string



    # Remove "What is:" from the string
    mathProblem = mathProblem[9:]


    print("problem:", str(mathProblem))

    num1 = int(mathProblem.split(" ")[0])
    num2 = int(mathProblem.split(" ")[2])
    operator = mathProblem.split(" ")[1]


    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2
        answer = math.floor(answer)
    else:
        print("Unknown operator")

    print("answer:", answer)

    conn.sendline(str(answer).encode())
    print("Solved problem", i)

    i += 1

conn.interactive()
