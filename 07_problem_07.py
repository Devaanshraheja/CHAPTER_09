with open("log.txt","r") as f:
    line=f.readlines()
lineno=1
for l in line:
    if("python" in l):
        print(f"line number is:{lineno}")
    break    
    lineno+=1
    
else:
    print("PYTHON IS NOT FOUND")
    
