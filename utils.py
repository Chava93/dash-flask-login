import dash_core_components as dcc
import dash_html_components as html
colors = ["#8c2e2d", "#56565a"]

nav_class = "navbar-item is-tab is-hidden-mobile"

def add_header_element(name, href, active=False):
    className = f"navbar-item is-tab is-active" if active else "navbar-item is-tab"
    return html.A(dcc.Link(name, href=href, className=className,
                  style={"color":"black"}))


def make_header(active_page, pages):
    """
    Obtain an html component for the page header with
    the 'active_page' active

    Parameters
    ----------
    pages: dictionary with link: label
        of thhe headers
    """
    logo_url= "https://static.wixstatic.com/media/8376cb_beb3404abdbc436eada7fc49d1da57f5~mv2.png/v1/fill/w_364,h_112,al_c,lg_1,q_80/letras_analysic_nabla.webp"

    header_tabs = [add_header_element(name, f"/apps/{page}",
                                      active=True if page == active_page else False)
                   for page, name in pages.items()]

    header_logo = [
            html.A(html.Img(src=logo_url),
                   className="navbar-item",
                   href="https://nabla.mx",
                   target="_blank")]

    header = html.Nav([
        html.Div([
            *header_logo,
        ], className="navbar-brand"),
        html.Div([
            html.Div(header_tabs, className="navbar-start", id="id_header_elements")
        ], className="navbar-menu")
    ], className="navbar is-light", role="navigation")
    return header


def make_left_panel(elements, style=None):
    """
    Place empty left panel

    Parameters
    ----------
    elements: list
        collection of dash_core_components
        or dash_html_elements
    """
    panel = html.Aside([
        html.Nav(elements, className="menu",
                 style=style)
    ], className="column is-2")

    return panel


def make_footer():
    footer = html.Footer([
        html.Div([
            html.P("Powered by"),
            html.Strong(html.A("Analysic Nabla", href="https://nabla.mx", target="_blank"))
        ], className="content has-text-centered")
    ], className="footer")

    return footer

def hero_pages(items,active_page):
    tabs = []
    for item in items:
        if item == active_page:
            curr = html.Li(html.A(item), className = 'is-active')
        else:
            curr = html.Li(html.A(item))
        tabs.append(curr)
    if len(tabs) < 2:
        return []
    return tabs

def HeroHeader(title, active_page, pages):
    logo_url= "https://static.wixstatic.com/media/8376cb_beb3404abdbc436eada7fc49d1da57f5~mv2.png/v1/fill/w_364,h_112,al_c,lg_1,q_80/letras_analysic_nabla.webp"
    tabs = hero_pages(list(pages.values()), active_page)
    top_hero = html.Div([
        html.Nav([
            html.Div([
                html.Div([
                    html.A([
                        html.Img(
                            src = logo_url)
                    ], href="https://nabla.mx", target="_blank", className = 'navbar-item')
                ], className = 'navbar-brand')
            ], className = 'container')
        ], className="navbar")
    ], className = 'hero-head')
    hero = html.Section([
        top_hero,
        html.Div([
            html.Div([
                html.H1('Analysic Nabla', className = 'title', style = {'color':colors[0]}),
                html.H2(title, className = 'subtitle'),
            ], className = 'container has-text-centered')
        ], className = 'hero-body'),
        html.Div([
            html.Nav([
                html.Div([
                    html.Ul(tabs)
                ], className = 'container')
            ], className = 'tabs is-boxed is-fullwidth')
        ], className = 'hero-foot')
    ], className = 'hero is-light')
    return hero
