# Dash
import dash  # Main Dash library
from dash import Dash, html, dcc, callback, Output, Input  # Dash components and utilities

# Bootstrap Libraries
import dash_bootstrap_components as dbc  # Bootstrap components for Dash
import dash_mantine_components as dmc  # Mantine components for Dash

# import website content from content.py
from content import *

# Social media icons without text
social_media_icons = html.Div([
    html.A(html.Img(src=github_icon, height="30"), href=github_link, target="_blank", className="icon"),
    html.A(html.Img(src=linkedin_icon, height="30"), href=linkedin_link, target="_blank", className="icon"),
    html.A(html.Img(src=medium_icon, height="30"), href=medium_link, target="_blank", className="icon")
], style={'display': 'flex', 'justify-content': 'space-between', 'width': '125px'})

# Social media icons with text
social_media_icons_with_text = html.Div([
    dbc.NavLink(html.Div([html.Img(src=github_icon, height="100em"), html.Span("GitHub", style={"padding": "1em"})]), href=github_link, style={"margin": "1em"}),
    dbc.NavLink(html.Div([html.Img(src=linkedin_icon, height="100em"), html.Span("LinkedIn", style={"padding": "1em"})]), href=linkedin_link, style={"margin": "1em"}),
    dbc.NavLink(html.Div([html.Img(src=medium_icon, height="100em"), html.Span("Medium", style={"padding": "1em"})]), href=medium_link, style={"margin": "1em"})
])

# My headshot image (for home page)
headshot_img = dmc.Image(
            src=headshot_src,
            alt="Picture of me",
            id="headshot-img"
)

# Image of a laptop (for contact page)
laptop_img = dmc.Image(
            src=laptop_src,
            alt="Picture of laptop",
            id="laptop-img"
)

footer_content = dbc.Row([ 
        html.P("© 2024 Rebekah Fowler. All rights reserved."),
        html.Div(social_media_icons)
    ], id = "footer-content")

# Footer component
footer = dmc.Footer(
    height=40,
    fixed=True,
    children=[footer_content]
)

# Function to create project card
def create_project_card(image_src, title, description, button_text, button_href, technology, button_color="blue"):
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=image_src,
                    height=160,
                )
            ),
            dmc.Group(
                [
                    dbc.Row(
            [
                dbc.Col(dmc.Text(title, weight=500, style={"padding-right": "5px"}), width={"size": 9}),
                dbc.Col(dmc.Badge(technology, color="blue", variant="light"), style={"textAlign": "right", "position": "absolute", "right": "5px"})
            ],
            #className="align-items-center justify-content-end"
        )
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                description,
                size="sm",
                color="dimmed",
                style={
                    "height": "200px", 
                    "overflowY": "auto",
                    "textOverflow": "ellipsis",
                    "WebkitOverflowScrolling": "touch",
                    "scrollbarWidth": "thin",
                    "scrollbarColor": "rgba(0, 0, 0, 0.5) rgba(0, 0, 0, 0.1)"
                }
            ),
            html.A(dmc.Button(
                button_text,
                variant="light",
                color=button_color,
                fullWidth=True,
                mt="md",
                radius="md",
            ), href = button_href, target="_blank", style={"textDecoration": "none"}),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"margin": "1em"},
    )

# Create Portfolio Project cards
project_cards = [
    create_project_card(
        project["image_src"],
        project["title"],
        project["description"],
        project["button_text"],
        project["button_href"],
        project["technology"]
    )
    for project in projects_list
]

# Define a chip group for skills
skills_chip_group = dmc.ChipGroup(
    [dmc.Chip(x, value=x) for x in ["Python", "SQL", "Tableau", "Excel"]],
    value="Python"
)

# Function to create an accordion label with an avatar, skill label, and description
def create_accordion_label(label, image, description):
    return dmc.AccordionControl(
        dmc.Group(
            [
                dmc.Avatar(src=image, size="lg"),
                html.Div(
                    [
                        dmc.Text(label),
                        dmc.Text(description, size="sm", weight=400, color="dimmed")
                    ]
                )
            ]
        )
    )
# Function to create accordion content with skill details
def create_accordion_content(content):
    return dmc.AccordionPanel(dmc.Text(content, size="sm"))
    
# Creating an accordion component to display skills information
skills_accordion = dmc.Accordion(
    chevronPosition="right",
    variant="contained",
    children=[
        dmc.AccordionItem(
            [
                create_accordion_label(
                    skill["label"], skill["image"], skill["description"]
                ),
                create_accordion_content(skill["content"])
            ],
            value=skill["id"]
        )
        for skill in skills_list
    ]
)

# Navigation bar with links and social media icons
nav = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", id="home-link", href="/", className="nav-link")),
        dbc.NavItem(dbc.NavLink("About", id="about-link", href="/about", className="nav-link")),
        dbc.NavItem(dbc.NavLink("Skills", id="skills-link", href="/skills", className="nav-link")),
        dbc.NavItem(dbc.NavLink("Portfolio", id="portfolio-link", href="/portfolio", className="nav-link")),
        dbc.NavItem(dbc.NavLink("Contact", id="contact-link", href="/contact", className="nav-link")),
        social_media_icons
    ],
    brand="Rebekah Fowler",
    brand_href="/",
    color="primary",
    dark=True,
    expand="lg",
    id = "nav-bar"
)
# Function to create education timeline component
def generate_education_timeline(certificates_list):
    # Initialize an empty list to store TimelineItem components
    timeline_items = []

    # Iterate over the certificates_list and create a TimelineItem for each certificate
    for certificate in certificates_list:
        timeline_item = dmc.TimelineItem(
            title=certificate["name"],
            children=[
                dmc.Text(
                    [
                        certificate["description"],
                        html.Br(),
                        dmc.Anchor("Certification Issued {}".format(certificate["date_issued"]), href=certificate["href"], size="sm") if certificate["href"] else None
                    ],
                    color="dimmed",
                    size="sm"
                )
            ]
        )
        timeline_items.append(timeline_item)

    # Create and return the education_timeline component with the generated TimelineItems
    education_timeline = dmc.Timeline(
        active=len(certificates_list) - 1,  # Set active item to the last index
        bulletSize=15,
        lineWidth=2,
        children=timeline_items
    )

    return education_timeline

education_timeline = generate_education_timeline(certificates_list)

# Page Layouts
"""
# Home page layout
home_side_content = [
    html.H2("Hello, I'm Rebekah!", className="home-title", style = {"padding-top":"250px", "padding-bottom":"0px"}),
    html.P("Data Analyst and Data Storyteller", className="home-description", style = {"padding-bottom":"2em"}),
    html.A(dmc.Button("See My Work", variant="light"), href='/portfolio')
]

home_page = html.Div([
    dbc.Row([
        dbc.Col(home_side_content, style={"margin": "1em", "text-align": "center"}, width={"sm": 12, "md": 6}, id="home-side-content"),
        dbc.Col(headshot_img, className="hide-img", width={"sm": 12, "md": 6})
    ])
], id="home", className="col-to-row")
"""
# Home page layout
home_side_content = html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("Hello, I'm Rebekah!", className="home-title"),
                html.P("Data Analyst and Data Storyteller", className="home-description"),
                html.A(dmc.Button("See My Work", variant="light"), href='/portfolio')
            ], md=6, className="order-2 order-md-1"),
            dbc.Col(html.Img(src=headshot_src, className="headshot-image"), md=6, className="order-1 order-md-1")
        ], className="overlay-content")
], style={
    'background-image': 'url("https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")',
    'background-size': 'cover',
    'background-repeat': 'no-repeat',
    'background-position': 'center',
    'height': '100vh'
})

home_page = html.Div([
    home_side_content
], id="home")


# About page layout
about_page = html.Div([
    html.H2("About Me", className="about-title"),
    html.P([about_content], className="about-description"),
    dmc.Divider(size="md"),
    html.H2("Education", className="about-title"),
    education_timeline
], id="about", className="content")

# Skills page layout
skills_page = html.Div([
    html.H2("Skills", className="skills-title"),
    #html.P("This section is about me and my skills.", className="skills-description"),
    skills_accordion
], id="skills", className="content")

# Portfolio page layout
portfolio_page = html.Div([
    dbc.Container([
        html.H2("Featured Projects", className="projects-title"),
        #html.P("Here are some of my projects and works.", className="projects-description"),
        dbc.Row([
            dbc.Col(card, className="portfolio-card", sm = 12, md=6, lg = 4) for card in project_cards
        ], align="center")
    ]),
    # For the ability to filter projects by technologies used (to be implemented)
    #html.H2("Projects", className="projects-title"),
    #skills_chip_group
], id="portfolio", className="content")

# Contact page layout
contact_side_content = [
    html.H2("Where you can reach me", className="contact-title"),
    #html.P("You can reach out to me using the following contact details.", className="contact-description"),
    html.H5("contact@rebekahfowler.com", className="contact-email"),
    social_media_icons_with_text
]

contact_page = html.Div([
    dbc.Row([
        dbc.Col(laptop_img, width={"sm": 12, "md": 6}),
        dbc.Col(contact_side_content, id="contact-side-content", style={"margin": "3em", "text-align": "center"}, width={"sm": 12, "md": 6})
    ])
], id="contact")

# URL to an external CSS file
external_styles = "https://rebekah999.github.io/styles_v2.css"

# Initialize Dash app with external stylesheets
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, external_styles])
#server = app.server

app.title = "Rebekah Fowler"

# Defining app layout
app.layout = html.Div([
    html.Meta(name='viewport', content='width=device-width, initial-scale=1'),
    html.Link(
        rel='shortcut icon',
        href="/Users/rebekahfowler/Downloads/Website Icons/faviconio-logo/logo.png"  # Update file served on GitHub
    ),
    dcc.Location(id='url', refresh=False),
    html.Div([nav, html.Div(id='page-content'), footer], style={"display": "flex", "flexDirection": "column", "overflow-x": "hidden"})
], id="app")

# Callback to update page content based on URL pathname
@app.callback(
    Output('page-content', 'children'), # Output component to display page content
    [Input('url', 'pathname')] # Input component for URL pathname changes
)
def display_page(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/about':
        return about_page
    elif pathname == '/skills':
        return skills_page
    elif pathname == '/portfolio':
        return portfolio_page
    elif pathname == '/contact':
        return contact_page
    else:
        return html.H1("404 - Page not found", style={'textAlign': 'center'})
        
# Run the app
if __name__ == '__main__':
    app.run_server()
    #app.run_server(debug=True) # Run the app in debug mode
