from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.routes.auth import login_required
from app.db import get_db

bp = Blueprint('resource', __name__)

@bp.route('/eresource', methods=('GET, POST'))
def resource():
    if request.method == 'GET':
        return render_template('eresource/base.html')



