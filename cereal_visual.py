import pandas as pd
import plotly.express as px




df = pd.read_csv('cereal.csv')
df.head()


# #bar chat
# fig = px.bar(df, x='name', y='calories')
# fig.show()
# #Modify Bar Charts
# fig = px.bar(df, x='name', y='calories',color='protein',labels={'calories':'Calories in kCal'})
# fig.show()
#Scatter Plots
# fig = px.scatter(df, x="name", y="rating")
# fig.show()
#Heatmap
# fig = px.imshow([[1, 50, 70, 80],
#                  [20, 1, 60, 40],
#                  [30, 60, 1, 90],
#                  [1, 2, 50, 1]])
# fig.show()
#Carpet Plots
import plotly.graph_objects as go
fig = go.Figure(go.Carpet(
    a = [4, 4, 5, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
))
fig.show(renderer="iframe")
#Scatterplot Matrix
fig = px.scatter_matrix(df,
    dimensions=["protein", "fat", "sodium", "fiber"],
    color="rating")
fig.show()
#3D Axes Plot
fig = go.Figure(data=[go.Mesh3d(x=df['protein'],
                   y=df['fat'],
                   z=df['sugars'])])
fig.show()