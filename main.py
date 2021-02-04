from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


def convert_age_to_str(age):
    if age % 10 == 1 and age != 11:
        return f'{age} год'
    if age % 10 in range(2, 5) and age not in range(12, 15):
        return f'{age} года'
    return f'{age} лет'


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    winery_age = datetime.now() - datetime(year=1920, month=1, day=1)

    rendered_page = template.render(
        winery_age=convert_age_to_str(
            int(winery_age.days/365.25)  # 365.25 is leap years hack 
        ),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
