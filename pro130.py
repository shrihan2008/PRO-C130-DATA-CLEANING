import csv,pandas as pd
data=[]
f=pd.read_csv("total_stars.csv")

star_data=data[1:]
star_data.sort(key=lambda star_data:star_data[2])
f=f[f['Radius']]
f=f[f['Mass']]
f=f[f['Distance']]


#f.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

#final_data = f.dropna()

#f#inal_data.reset_index(drop=True,inplace = True)

#final_data.to_csv('final_data.csv')
    
file=f.rename({
    'Star_name':"Star_name",
    'Distance':"Distance",
    'Mass':'Mass',
    'Radius':"Radius",
},
axis='columns')

print(file.shape)
file.to_csv("main.csv"),