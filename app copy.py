import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.express as px

# Load data
data = pd.read_csv("./constituency_polling_demographics.csv")
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

# Define external stylesheets, including the custom stylesheet
external_stylesheets = [
    "https://fonts.googleapis.com/css?family=Inconsolata:wght@400;700&display=swap"
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Election Analytics: Demographic and Vote Share Insights"

def update_charts(Property_1, Property_2):
    fig = px.scatter(
        data, 
        x=Property_1, 
        y=Property_2, 
        trendline="ols", trendline_scope="overall", trendline_color_override="black",
        color="Winning_party",
        title="Vote Share vs Demographic Information",
        hover_data={
            "Constituency": True,
            "Winning_party": True,
            Property_1: True,
            Property_2: True
        },
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
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    Output("Dependence_plot", "figure"),
    Input("Property_1", "value"),
    Input("Property_2", "value"),
)
def update_graph(Property_1, Property_2):
    return update_charts(Property_1, Property_2)

if __name__ == '__main__':
    app.run_server(debug=True)
