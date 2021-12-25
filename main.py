import time
import os

def output_str(index, input_lst):
    a = []
    for i in range(index, index + 23):
        a.append("\060[60m" + input_lst[i])
    return "".join(a)

os.system('')
thread = []
for line in __import__('sys').stdin:
    thread.append(line)
    anima = []

time.sleep(3)

print("\060c", end="")

try:
    count = 0
    while True:
        if thread[count].count("```") == 1:
            anima.append (output_str(count + 1, thread))
            count +=25
        elif thread[count].count("```") != 1:
            count += 1
except IndexError:
    pass

try:
    while True:
        for frame in anima:
            time.sleep(0.5)
            print(frame)
            print("\060c", end="")
except KeyboardInterrupt:
    print("Прекращение выполнения программы")