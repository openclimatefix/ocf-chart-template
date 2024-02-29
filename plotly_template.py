import plotly.io as pio

colors = ['#7BCDF3', '#63BCAF', '#FF9736', '#FFD053' , '#14120E', '#4C9A8E']  # Define a custom color palette for plots
pio.templates.default = "plotly"  # Set the default plotly template for consistent styling
pio.templates["plotly"]["layout"]["font"] = dict(family="Inter, sans-serif") # Set the default font family to 'Inter'
pio.templates["plotly"]["layout"]["colorway"] = colors  # Apply the custom color palette to the plot colorway
pio.templates["plotly"]["layout"]["title"] = dict(x=0.5)  # Center the plot title horizontally
pio.templates["plotly"]["layout"]["margin"] = dict(t=50)  # Reduces the top margin to bring the title closer to the graphs
pio.templates["plotly"]["layout"]["plot_bgcolor"] = "#FFF"  # Set the background color of the plot to white
pio.templates["plotly"]["layout"]["xaxis"]["gridcolor"] = '#E4E4E4'  # Set the grid color of the x-axis (light grey)
pio.templates["plotly"]["layout"]["yaxis"]["gridcolor"] = '#E4E4E4'  # Set the grid color of the y-axis (light grey)
