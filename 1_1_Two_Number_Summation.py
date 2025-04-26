# Problem: give two numbers and return the a+b


def summationFunction(a,b):
    return a+b

if __name__ == "__main__":
    a,b = input().split()
    print(summationFunction(int(a),int(b)))

