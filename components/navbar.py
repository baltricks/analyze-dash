import dash
import i18n

from dash import Input, Output, State, html
from dash_bootstrap_components import Navbar, NavbarBrand, Nav, NavLink, NavbarToggler
from dash_bootstrap_components import Row, Col, Button, Input as Input_comp, Collapse
    

def get_navbar(app):
    nav_contents = [
        NavLink(page['title'], href=page["relative_path"], active="exact")
            for page in dash.page_registry.values() 
            if page['name'] in ('home', 'about')
    ]

    menu_bar = Row(
        [
            Col(Nav(nav_contents, pills=True, justified=True)),
            Col(Input_comp(type="search", 
                placeholder=i18n.t('app.search.placeholder'))),
            Col(
                Button(
                    i18n.t('app.search.label'), 
                    color="primary", className="ms-2", n_clicks=0
                )
            )
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0"
    )

    navbar = Navbar(
        [
            html.A(
                Row(
                    [
                        # Col(html.Img(src=LOGO, height="30px")),
                        Col(NavbarBrand(i18n.t('app.app.title'), 
                            className="ms-2")),
                    ],
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            NavbarToggler(id="navbar-toggler", n_clicks=0),
            Collapse(
                menu_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            )
        ]
    )

    # add callback for toggling the collapse on small screens
    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    return navbar