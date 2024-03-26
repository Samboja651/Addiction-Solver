from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from app.routes.auth import login_required
from app.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    db = get_db()
    stories = db.execute(
        'SELECT user_name, story, story_url FROM success_stories'
    ).fetchall()

    addictions = db.execute('SELECT addiction_type FROM addiction').fetchall()

    return render_template('home/index.html', stories = stories, addiction_type = addictions)


@bp.route('/mystory/<id>', methods=('GET', 'POST'))
def full_story(id):
    id = str(id)

    db = get_db()
    owner_story = db.execute(
        'SELECT story_id, user_name FROM success_stories'
    ).fetchall()
    
    for owner in owner_story:
        if str(owner['story_id']) == id:
            return render_template('home/my_story.html', username = owner['user_name'])
        
    return redirect(url_for('home'))



    

