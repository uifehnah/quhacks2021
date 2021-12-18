import sys
import plotly.express as px



goal = int(sys.argv[1])
hourly = sys.argv[2]

hourly = list(map(int,hourly.split(",")))

remaining_to_drink = goal - sum(hourly)


fig =px.line(x=list(range(1,len(hourly)),y=hourly)
fig.show()
