def greetings(name):
    if name:
        print(f"Hello {name}!!")
    else:
        print("Hello, World!!!")
        
name = input("Enter your name and or click enter: ")

greetings(name)
