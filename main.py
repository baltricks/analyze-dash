import i18n
import locale
# must be set before any components using translations are loaded
locale.setlocale(locale.LC_ALL, 'en')
i18n.load_path.append('resources')

from dash import html, Dash, page_container
from dash_bootstrap_components import Container, Row, Col, themes

from components.sidebar import get_sitebar
from components.navbar import get_navbar

app = Dash(external_stylesheets=[themes.CERULEAN], use_pages=True)


app.layout = Container([
    Row([get_navbar(app)], className="mb-3"),
    Row([
            Col(get_sitebar(), width=2),
            Col(html.Div([
                page_container
            ])),
        ])])


if __name__ == "__main__":
    app.run_server(port=8888)