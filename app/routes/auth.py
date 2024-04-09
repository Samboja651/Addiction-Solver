import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
)

from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix = '/auth')
# auth is the name of the blueprint
# __name__ is the location of the bp 


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        # below part is confusing
        if error is None:
            try:
                if len(password) < 8:
                    flash('Password must be at least 8 characters long.', 'danger')
                    return redirect(url_for('auth.register'))  
                
                elif not any(char.isupper() for char in password):
                    flash('Password must contain at least one uppercase letter.', 'danger')
                    return redirect(url_for('auth.register'))
                
                elif not any(char.islower() for char in password):
                    flash('Password must contain at least one lowercase letter.', 'danger')
                    return redirect(url_for('auth.register'))
                
                elif not any(char.isdigit() for char in password):
                    flash('Password must contain at least one numeric digit.', 'danger')
                    return redirect(url_for('auth.register'))
                
                elif not any(char.isalnum() or char in '!@#$%^&*()-_=+[]{}|;:\'",.<>?/`~' for char in password):
                    flash('Password must contain at least one special character.', 'danger')
                    return redirect(url_for('auth.register'))


                db.execute("INSERT INTO user (username, password) VALUES(?, ?)",
                (username, generate_password_hash(password)),)
                db.commit()
            
                return redirect(url_for("auth.login"))   
             
            except db.IntegrityError:
                error = f"User {username} is already registered"
            
            
         # this part has a problem
        else:
            return redirect(url_for("auth.login"))
        
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
        
        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()         # clear any current session and assign a new one
            session['user_id'] = user['user_id']    # in the user table we have column user_id, that's what we are using
            return redirect(url_for('home'))
        
        flash(error)
    # below line is tricky to understand how it connects to the above code
    return render_template('auth/login.html')




@bp.route('/logout')
def logout():
    session.clear()
  
    return redirect(url_for('home'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE user_id = ?', (user_id,)
        ).fetchone()


# ensure users are logged in for some resources
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view  # recursive function here base case is a negation of the if stm


            
