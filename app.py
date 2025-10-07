from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def home():
    venv_dir = os.path.join(os.path.dirname(__file__), 'venvs')
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)
    venvs = [d for d in os.listdir(venv_dir) if os.path.isdir(os.path.join(venv_dir, d))]

    if request.method == 'POST':
        venv_name = request.form.get('venv_name', '').strip()
        if not venv_name:
            flash('Environment name cannot be empty.', 'error')
        elif venv_name in venvs:
            flash('Environment already exists.', 'error')
        else:
            venv_path = os.path.join(venv_dir, venv_name)
            try:
                import venv
                venv.create(venv_path, with_pip=True)
                flash(f'Virtual environment "{venv_name}" created!', 'success')
                venvs.append(venv_name)
            except Exception as e:
                flash(f'Error creating environment: {e}', 'error')
        return redirect(url_for('home'))

    return render_template('index.html', venvs=venvs)

if __name__ == '__main__':
    app.run(debug=True)
