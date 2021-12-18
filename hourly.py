import plotly.express as px

# with open('file_path', 'r') as file:
#     data = file.read()

# goal = data[some_range]
# hourly = data[some_range]

goal = 3.5
hourly = '0.3,0.25,0.6,0.1,0.4'

hourly = list(map(float,hourly.split(",")))


fig = px.line(x=list(range(1,len(hourly)+1)),y=hourly,title="Hourly Water Intake (Liters/Hour)",labels = {'x': 'Hour','y': 'Liters'})
fig.write_html("hourly.html")