from flask import(
    Blueprint, render_template, request
)

from app.routes.auth import login_required
from app.db import get_db

bp = Blueprint('resources', __name__)

@bp.route('/help/eresources', methods=('GET', 'POST'))
@login_required
def resource():
    db = get_db()
    addictions = db.execute('SELECT addiction_type FROM addiction').fetchall()
    if request.method == 'GET':
        return render_template('eresource/base.html', labels = addictions)

    label = request.form['label']
    if label == 'none':
        return render_template('eresource/base.html', labels = addictions)
    

    if label == 'All':
        eresources = db.execute("SELECT title, body, article_link, video_name, video_link FROM educational_resources").fetchall()
        return render_template('eresource/content.html', eresources = eresources, labels = addictions, label = label)
    
    eresources = db.execute("SELECT title, body, article_link, video_name, video_link FROM educational_resources WHERE type_id IN (SELECT type_id FROM addiction WHERE addiction_type = ?)", (label,)).fetchall()

    return render_template('eresource/content.html', eresources = eresources, labels = addictions, label = label)


