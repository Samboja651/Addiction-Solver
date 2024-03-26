from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.routes.auth import login_required
from app.db import get_db

bp = Blueprint('help', __name__)

@bp.route('/help', methods=('GET', 'POST'))
@login_required
def platform():
    db = get_db()
    error = None
    try:
        if request.method == 'POST':
            required_fields = ['addiction-type', 'duration', 'cause', 'severity', 'age', 'gender']
            form_data = {field: request.form.get(field) for field in required_fields}
            data = list(form_data.values())

            if not all(form_data.values()):
                return "Please fill in all fields." 

            # get the logged in user's id
            username = g.user['username']
            logged_in_userid = db.execute("SELECT user_id FROM user WHERE username = ?", (username,)).fetchone()['user_id']
            
            # # now add the user_id to the list of data to be inserted into db
            data.append(logged_in_userid)

            # SAVE FORM DATA INTO DB
            stm = 'INSERT INTO addiction_data (addiction_type, duration, cause, severity, age, gender, user_id) VALUES(?, ?, ?, ?, ?, ?, ?)'
            db.execute(stm, data)
            db.commit()
        return render_template('help/platform.html')
    
    except db.IntegrityError:
        error = 'error!, cannot submit form twice.'
        flash(error)
        return redirect(url_for('home'))



@bp.route('/help/chat-doctor')
@login_required
def chat_doctor():
    return render_template('help/chat-doctor.html')


@bp.route('/help/peer-forum')
@login_required
def peer_forum():
    return render_template('help/peer-forum.html')


# # educational_resources
# @bp.route('/test/eresources')
# @login_required
# def e_resources():
#     return render_template('help/educational_resources.html')