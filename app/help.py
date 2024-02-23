from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

bp = Blueprint('help', __name__)

@bp.route('/help')
@login_required
def platform():
    # db = get_db()
    # db.execute()
    return render_template('help/platform.html')


@bp.route('/help/chat-doctor')
@login_required
def chat_doctor():
    return render_template('help/chat-doctor.html')


@bp.route('/help/peer-forum')
@login_required
def peer_forum():
    return render_template('help/peer-forum.html')


# educational_resources
@bp.route('/help/eresources')
@login_required
def e_resources():
    return render_template('help/educational_resources.html')