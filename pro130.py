import csv
data=[]
with open('merge1.csv','r') as f:
    read=csv.reader(f)
    for i in read:
        data.append(i)

f=f[f['column_name'].notna()]

del f["Luminiosity"]

    
file=f.rename({
    'Star_name':"Star_name",
    'Distance':"Distance",
    'Mass':'Mass',
    'Radius':"Radius",
},
axis='columns')

print(file.shape)
file.to_csv("main.csv"),