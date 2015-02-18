# encoding: utf-8
from encolinks import db
from encolinks.models import Link
import re
from flask import (
    Blueprint,
    jsonify,
    request,
    abort
)

rest_api = Blueprint("rest_api", __name__)


def create_link(url):
    link = Link(url)
    db.session.add(link)
    db.session.commit()
    return link.cod


def get_cod_from_url(url):
    result = url
    m = re.match(r'http[s]?://[^/]+/(\w{6})/', url)
    if m:
        result = m.group(1)
    return result


@rest_api.route('/shrink/', methods=['POST'])
def shrink():
    url = request.form.get('url', None)
    if not url:
        abort(400)
    cod = create_link(url)
    return jsonify({'url': '{}{}/'.format(
        request.url_root,
        cod
    )})


@rest_api.route('/info/', methods=['GET'])
def info():
    url = request.args.get('url', None)
    if not url:
        abort(400)
    link = Link.query.get(get_cod_from_url(url))
    if not link:
        abort(404, 'Link not found')
    return jsonify(
        {
            "cod": link.cod,
            "last_access": link.last_access,
            "qtd": link.qtd,
            "url": link.url
        }
    )

