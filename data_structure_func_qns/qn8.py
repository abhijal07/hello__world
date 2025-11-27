def group_by_extension(files):
    D={}
    for i in files:
        D=i.split('.')
    return D
files = ["script.py","notes.txt","data.csv","main.py","image.png","list.txt"]
print(group_by_extension(files))