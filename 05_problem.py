words=["ganda","bad","donkey"]

with open("file.txt","r") as f:
    content=f.read()

for w in words:
    content=content.replace(w,"*"*len(w))

with open("file.txt","w") as f:
    f.write(content)


