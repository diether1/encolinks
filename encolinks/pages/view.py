# encoding: utf-8
from encolinks import db
from encolinks.models import Link
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    redirect
)


pages = Blueprint(
    "pages",
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/pages'
)


def update_link_access(link):
    link.qtd += 1
    link.last_access = datetime.now()
    db.session.add(link)
    db.session.commit()
    return True


@pages.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@pages.route('/<cod>/')
def make_redirect(cod):
    link = Link.query.get(cod)
    update_link_access(link)
    return redirect(link.url, 301)

