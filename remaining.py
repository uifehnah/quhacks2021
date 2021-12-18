import plotly.express as px
import plotly.graph_objects as go


with open('file_path', 'r') as file:
    data = file.read()


labels = ['To drink','Drank']
#some index is the index position of the result from calculation stored in the string data
values = [data[someindex],data[someindex]]
colors = ["royalblue","darkblue"][::-1]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))

