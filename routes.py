from flask import request, redirect, flash, render_template

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register', methods=['POST'])
    def register():
        db = app.config['DB']
        name, email, phone, course = (request.form.get(x) for x in ['name', 'email', 'phone', 'course'])
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)", (name, email, phone, course))
            db.commit()
            flash("Success", "success")
        except Exception as err:
            db.rollback()
            flash(f"Failed {err}", "danger")
        finally:
            return redirect('/')
