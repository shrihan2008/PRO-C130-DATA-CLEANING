import csv,pandas as pd
from turtle import distance
data=[]
f=pd.read_csv("total_stars.csv")

star_data=data[1:]
star_data.sort(key=lambda star_data:star_data[2])

mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
d =f['Distance'].to_list()

f.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

final_data = f.dropna()
final_data.reset_index(drop=True,inplace = True)


    
file=f.rename({
    'Star_name':"Star_name",
    'Distance':"Distance",
    'Mass':'Mass',
    'Radius':"Radius",
},
axis='columns')

print(file.shape)
file.to_csv("e.csv"),