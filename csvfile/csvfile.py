import csv

with open(file,"r") as file:
    s,p,c=0,0,0
    reader = csv.reader(file)
    for row in reader:
        if row[1] == s:
            s += 1
        elif row[1] == p:
            p += 1
        elif row[1] == c:
            c += 1

print(f"s: {s}")
print(f"p: {p}")
print(f"c: {c}")
            


        
