import i18n

from dash import html, page_registry
from dash_bootstrap_components import NavLink, Nav, Row, Col


def get_sitebar():
    nav_contents = [
        NavLink(page['title'], href=page["relative_path"], active="exact")
            for page in page_registry.values() 
            if page['name'] not in ('home', 'about')
    ]

    return Row(
        Col([
            html.P(i18n.t('app.sidebar.header'), className="lead"),
            Nav(nav_contents, pills=True, justified=True, vertical=True)
        ])
    )
