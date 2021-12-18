import plotly.express as px
import plotly.graph_objects as go


with open('file_path', 'r') as file:
    data = file.read()

hourly = data[someindex]
goal = data[someindex]

hourly = list(map(int,hourly.split(",")))


labels = ['To drink','Drank']
#some index is the index position of the result from calculation stored in the string data
values = [goal - sum(hourly),sum(hourly)]
colors = ["royalblue","darkblue"][::-1]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.write_html("remaining.html")
