from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.routes.auth import login_required
from app.db import get_db

bp = Blueprint('resources', __name__)

@bp.route('/eresources', methods=('GET', 'POST'))
def resource():
    db = get_db()
    addictions = db.execute('SELECT addiction_type FROM addiction').fetchall()
    if request.method == 'GET':
        return render_template('eresource/base.html', labels = addictions)

    


