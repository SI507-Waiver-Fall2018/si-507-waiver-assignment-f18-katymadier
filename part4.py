#Katy Madier | kmadier
#SI507 Waiver Part 4

# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

f=open("noun_data.csv","r")
fstr=f.readlines()
f.close()

noun=[]
quantity=[]
for line in fstr[3:]:
    pair=line.strip().split(",")
    noun+=[pair[0]]
    quantity+=[pair[1]]

for line in fstr[:1]:
    wordsSearched=line.strip().split()[0]
    user=line.strip().split()[4].split("'")[0]

trace = go.Bar(
    x=noun,
    y=quantity,
    name='Nouns',
    marker=dict(
        color=['rgba(87,254,226,0.8)','rgba(87,254,226,0.8)','rgba(87,254,226,0.8)','rgba(87,254,226,0.8)','rgba(87,254,226,0.8)']))
data = [trace]
layout = go.Layout(title="Most frequent nouns used by " + user + " out of " + wordsSearched + " tweets analyzed", width=800, height=640)
fig = go.Figure(data=data, layout=layout)

py.plot(data, filename='part4_viz_image')
py.image.save_as(fig, filename='part4_viz_image.png')
