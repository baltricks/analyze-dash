import i18n
import locale

import numpy as np

from dash import register_page, dcc, html
from dash_bootstrap_components import Row, Col, Card, CardBody, Tabs, Tab
from plotly.graph_objs import Box, Figure

from resources.markdown.measures import measures

register_page(__name__, 
    name = 'basic_stats', 
    title=i18n.t('app.sidebar.page.basic_stats'))


class BasicStats():
    def __init__(self):
        self._title = i18n.t('app.basic_stats.measures.graph.title')
        self._names = ['A', 'B']
        self._data = []
        np.random.seed(42)
        self._data.append(np.random.randn(50) - 1)
        np.random.seed(11)
        self._data.append(np.random.randn(50))
        lang = locale.getlocale()[0][:2]

        self._tabs = [
            { 
                'label': i18n.t('app.basic_stats.measures.tab'),
                'content': Row([
                    Col([
                        Card(
                            CardBody([
                                dcc.Graph(id='measures-graph', 
                                    figure=self.get_measures_figure(self._title))
                            ])
                        ),
                        html.P(i18n.t('app.basic_stats.measures.graph.note'), className="mt-2"),
                    ], width=6),
                    Col([
                        measures[lang]
                    ], width=6)
                ], className="mt-3")
            }
        ]

    def get_measures_figure(self, title):
        fig = Figure()
        for name, y in zip(self._names, self._data):        
            fig.add_trace(Box(y=y,
                boxpoints='all', 
                jitter=0.3, 
                whiskerwidth=0.2,
                marker_size=2,
                line_width=1,
                name=name, 
                boxmean='sd'))
        fig.update_layout(
            title=title,
        )
        return fig

    def get_layout(self):
        return Tabs(
            [ Tab(tab['content'], label=tab['label'])
                for tab in self._tabs ]
        )

layout = BasicStats().get_layout()