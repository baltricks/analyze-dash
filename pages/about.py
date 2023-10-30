import i18n

from dash import html, register_page

register_page(__name__, 
    name = 'about', 
    title=i18n.t('app.navigation.about'))

layout = html.Div([
])