def for_loop(a):
    for i in range(1,a+1):
        print(i)

def while_loop(a):
    i = 1
    while(i<=a):
        print(i)
        i = i+1
def for_loop_values(values):
    for x in values: #whithout using loop value print
        print(x)

if __name__ == "__main__":
    a = int(input("Enter your age"))
    values = ["Ram","Shyam","Hari"]
    for_loop_values(a)
    #for i in range(1,a):
        #print(i)
    for_loop(a)
    while_loop(a)
