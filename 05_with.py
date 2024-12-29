# f=open("file.txt")
# print(f.read())
# f.close()


#if you want to write this statement without being closed explicitly
with open("file.txt") as s:
    text=s.read()
    print(text)