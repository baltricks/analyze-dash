import i18n

from dash import html, register_page
from dash_bootstrap_components import Card, CardBody, Tabs, Tab

register_page(__name__, 
    name = 'basic_stats', 
    title=i18n.t('app.sidebar.page.basic_stats'))


tab1_content = Card(
    CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
        ]
    ),
    className="mt-3",
)

tab2_content = Card(
    CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
        ]
    ),
    className="mt-3",
)

layout = Tabs(
    [
        Tab(tab1_content, label=i18n.t('app.basic_stats.metrics.tab')),
        Tab(tab2_content, label="...")
    ]
)