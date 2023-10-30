import i18n

from dash import html, register_page

register_page(__name__, path='/', 
    name = 'home', 
    title=i18n.t('app.navigation.home'))

layout = html.Div([
])