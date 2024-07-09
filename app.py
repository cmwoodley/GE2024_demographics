# app.py
import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table
import plotly.express as px
from scipy.stats import pearsonr, linregress
import numpy as np

# Load data
GE_data = pd.read_csv("./constituency_polling_demographics.csv")
properties_2 = [ 'Prop_Reform UK', 'Prop_Independent', 'Prop_Conservative', 'Prop_Liberal Democrat', 
                 'Prop_Labour', 'Prop_Green', 'Prop_Abolish the Welsh Assembly Party', 'Prop_Alliance for Democracy and Freedom', 
                 'Prop_Alliance for Green Socialism', 'Prop_Animal Welfare Party', 'Prop_Ashfield Independents', 
                 'Prop_Blue Revolution', 'Prop_British Democratic Party', 'Prop_Chesterfield Independents', 'Prop_Christian Peoples Alliance', 
                 'Prop_Climate', 'Prop_Communist Future', 'Prop_Communist League', 'Prop_Communist Party of Britain', 'Prop_Confelicity', 
                 'Prop_Consensus', 'Prop_Count Binface Party', 'Prop_Democracy for Chorley', 'Prop_English Constitution Party', 'Prop_English Democrats', 
                 'Prop_Fairer Voting Party', 'Prop_Freedom Alliance', 'Prop_Hampshire Independents', 'Prop_Heritage Party', 'Prop_Independent Alliance Kent', 
                 'Prop_Independent Network', 'Prop_Independent Oxford Alliance', 'Prop_Independents for Direct Democracy', 
                 'Prop_Kingston Independent Residents Group', 'Prop_Liberal', 'Prop_Libertarian Party', 'Prop_Lincolnshire Independents', 
                 'Prop_Liverpool Community Independents', 'Prop_Monster Raving Loony Party', 'Prop_National Health Action Party', 
                 'Prop_New Open Non-Political Organised Leadership', 'Prop_Newham Independents Party', 'Prop_One Leicester', 'Prop_Party of Women', 
                 'Prop_Plaid Cymru', 'Prop_Portsmouth Independent Party', 'Prop_Propel', 'Prop_Psychedelic Future Party', 'Prop_Putting Crewe First', 
                 'Prop_Rebooting Democracy', 'Prop_Rejoin EU', 'Prop_Save Us Now', 'Prop_Shared Ground', 'Prop_Social Democratic Party', 
                 'Prop_Social Justice Party', 'Prop_Socialist Equality', 'Prop_Socialist Labour Party', 'Prop_Socialist Party of Great Britain', 
                 'Prop_South Devon Alliance', 'Prop_Stockport Fights Austerity No to Cuts', 'Prop_Swale Independents', 'Prop_Taking The Initiative Party', 
                 'Prop_The Common Good', 'Prop_The Common People', 'Prop_The Mitre TW9', 'Prop_The North East Party', 'Prop_The Peace Party', 
                 'Prop_The Speaker', 'Prop_The Yorkshire Party', 'Prop_The Yoruba Party in the UK', 'Prop_Trade Unionist and Socialist Coalition', 
                 'Prop_Transform', 'Prop_True & Fair', 'Prop_UK Independence Party', 'Prop_UK Voice', 'Prop_Volt', "Prop_Women's Equality Party", 
                 'Prop_Workers Party of Britain', "Prop_Workers' Revolutionary Party"]

properties_1 = [ 'Prop_Asian', 'Prop_Black', 'Prop_Mixed', 'Prop_White', 'Prop_Other', 
                 'Prop_Asian, Asian British or Asian Welsh: Bangladeshi', 'Prop_Asian, Asian British or Asian Welsh: Chinese', 
                 'Prop_Asian, Asian British or Asian Welsh: Indian', 'Prop_Asian, Asian British or Asian Welsh: Other Asian', 
                 'Prop_Asian, Asian British or Asian Welsh: Pakistani', 'Prop_Black, Black British, Black Welsh, Caribbean or African: African', 
                 'Prop_Black, Black British, Black Welsh, Caribbean or African: Caribbean', 'Prop_Black, Black British, Black Welsh, Caribbean or African: Other Black', 
                 'Prop_Mixed or Multiple ethnic groups: Other Mixed or Multiple ethnic groups', 'Prop_Mixed or Multiple ethnic groups: White and Asian', 
                 'Prop_Mixed or Multiple ethnic groups: White and Black African', 'Prop_Mixed or Multiple ethnic groups: White and Black Caribbean', 
                 'Prop_Other ethnic group: Any other ethnic group', 'Prop_Other ethnic group: Arab', 'Prop_White: English, Welsh, Scottish, Northern Irish or British', 
                 'Prop_White: Gypsy or Irish Traveller', 'Prop_White: Irish', 'Prop_White: Other White', 'Prop_White: Roma', 
                 'Prop_Economically active (excluding full-time students): In employment', 
                 'Prop_Economically active (excluding full-time students): Unemployed: Seeking work or waiting to start a job already obtained: Available to start working within 2 weeks', 
                 'Prop_Economically active and a full-time student: In employment', 
                 'Prop_Economically active and a full-time student: Unemployed: Seeking work or waiting to start a job already obtained: Available to start working within 2 weeks', 
                 'Prop_Economically inactive (excluding full-time students)', 'Prop_Economically inactive and a full-time student', 'Prop_Aged 15 years and under', 
                 'Prop_Aged 16 to 24 years', 'Prop_Aged 25 to 34 years', 'Prop_Aged 35 to 49 years', 'Prop_Aged 50 to 64 years', 'Prop_Aged 65 years and over']

external_stylesheets = [
    "https://fonts.googleapis.com/css?family=Inconsolata:wght@400;700&display=swap"
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Election Analytics: Demographic and Vote Share Insights"

def update_charts(Property_1, Property_2):
    data_filtered = GE_data.mask(GE_data[Property_2] == 0).dropna()

    # Calculate trendline manually
    x = data_filtered[Property_1]
    y = data_filtered[Property_2]
    
    # Fit a linear trendline
    z = np.polyfit(x, y, 1)
    trendline = np.poly1d(z)

    result = linregress(x,y)

    fig = px.scatter(
        data_filtered, 
        x=Property_1, 
        y=Property_2, 
        color="Winning_party",
        title="Vote Share vs Demographic Information",
        hover_data={
            "Constituency": True,
            "Winning_party": True,
            Property_1: True,
            Property_2: True
        },
    )
    
    # Add trendline to the plot
    fig.add_scatter(
        x=x, 
        y=trendline(x), 
        mode='lines', 
        name='Trendline', 
        line=dict(color="#000000"), 
        hoveron="points",
        hoverinfo='text',  # Specify hoverinfo to enable text hover data
        hovertext=f"R-squared: {result.rvalue**2:.2f}"
    )    
    
    fig.update_layout(
        xaxis={"fixedrange": True},
        yaxis={"fixedrange": True},
        title={
            "text": "Vote Share vs Demographic Information",
            "x": 0.05,
            "xanchor": "left"
        }
    )
    
    return fig

def update_stats(Property_1, Property_2):
    data_filtered = GE_data[[Property_1, Property_2]].dropna()

    # Calculate Pearson correlation coefficient and p-value
    r, p_value = pearsonr(data_filtered[Property_1], data_filtered[Property_2])
    
    # Prepare summary table
    summary = {
        "Variable": [Property_1],
        "Pearson Correlation Coefficient": [r],
        "P-value": [p_value]
    }

    # Convert summary to DataFrame
    summary_df = pd.DataFrame(summary)

    # Prepare columns and data for return
    columns = [{"name": col, "id": col} for col in summary_df.columns]
    data = summary_df.to_dict('records')

    return columns, data

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📊", className="header-emoji"),
                html.H1(
                    children="Election Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Explore the relationship between general election vote shares"
                        " and demographic information across different constituencies."
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Select Demographic Property", className="menu-title"),
                        dcc.Dropdown(
                            id="Property_1",
                            options=[
                                {"label": property, "value": property}
                                for property in properties_1
                            ],
                            value=properties_1[0],
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Select Vote Share Property", className="menu-title"),
                        dcc.Dropdown(
                            id="Property_2",
                            options=[
                                {"label": property, "value": property}
                                for property in properties_2
                            ],
                            value=properties_2[0],
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="Dependence_plot",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.H2(
                    children="Statistical Analysis", className="section-title"
                ),
                html.Div(
                    children=dash_table.DataTable(
                        id="stats_output",
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'left'},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    [Output("Dependence_plot", "figure"),
     Output("stats_output", "columns"),
     Output("stats_output", "data")],
    [Input("Property_1", "value"),
     Input("Property_2", "value")]
)
def update_graph_and_stats(Property_1, Property_2):
    fig = update_charts(Property_1, Property_2)
    columns, data = update_stats(Property_1, Property_2)
    return fig, columns, data

if __name__ == '__main__':
    app.run_server(debug=True)
