
a = open("Module2.py")
content = a.read()
print(content)
a.close()

# enter file name ,file location
# input lines , input data
# write data , read data
# count lines,words with space and chars and without space and chars

# task

file  = open("run.txt","w+")
def fn():
    n = int(input("entre no of lines "))
    for i in range(n):
        data = input("enter data ")
        file.write(data)
        file.write("\n")

def fn1():
    line = 0
    word = 0
    without_space_chars = 0
    file.seek(0)
    a_data = file.read()
    print(a_data)
    with_space_chars = len(a_data)
    for i in a_data:
        if i == " ":
            word = word+1
        elif i == '\n':
            line = line+1
            word = word+1
        else:
            without_space_chars = without_space_chars+1
            print("L ",line)
            print("W ",word)
            print("S C ",without_space_chars)

fn()
fn1()
file.close()


