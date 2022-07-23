import csv
data=[]
with open('merge1.csv','r') as f:
    read=csv.reader(f)
    for i in read:
        data.append(i)

f=f[f['column_name'].notna()]
columns = f.columns

f.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

    
file=f.rename({
    'Star_name':"Star_name",
    'Distance':"Distance",
    'Mass':'Mass',
    'Radius':"Radius",
},
axis='columns')

print(file.shape)
file.to_csv("main.csv"),