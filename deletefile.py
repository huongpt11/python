import os
if os.path.exists("doc.txt"):
    os.remove("doc.txt")
else:
    print("The file does not exist")