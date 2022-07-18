import csv
data=[]
with open('merged1.csv','r') as f:
    read=csv.reader(f)
    for i in read:
        data.append(i)



del f["Luminiosity"]

file=f.rename({
    'Star_name':"Star_name",
    'Distance':"Distance",
    'Mass':'Mass',
    'Radius':"Radius",
   
}
axis='columns')

print(file.shape)
file.to_csv("main.csv"),