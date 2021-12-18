import sys
import plotly.express as px

with open('file_path', 'r') as file:
    data = file.read()

goal = data[some_range]
hourly = data[some_range]


hourly = list(map(int,hourly.split(",")))

remaining_to_drink = goal - sum(hourly)


fig = px.line(x=list(range(1,len(hourly)+1)),y=hourly,title="Hourly Water Intake (Liters/Hour)")
fig.write_html("test.html")