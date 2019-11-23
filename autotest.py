import ast
import inspect

#main
program = input("Please enter the program you would like to test: ").strip()
programtxt = open(program, encoding="utf8").read()
exec(programtxt)

testcase = input("Please enter the name of the testcase file: ").strip()
f = open(testcase).read().splitlines()

for i in f:
    if ">>>" not in i:
        f.remove(i)
    elif "= RESTART =" in i:
        f.remove(i)


for i in range(len(f)):
    f[i] = f[i].replace(">>>", "").strip()

for i in f:
    print(">>> " + i)
    try:
        print(eval("repr("+i+")"))
    except:
        exec(i)


#V1
#Do not include input

#V2
#Remove everything that is found in between a print or input statment
#Ignore all the >>> an execute the rest of the line
#remember the line numbers that had the >>> so you know where to add them back when ur executing the code
