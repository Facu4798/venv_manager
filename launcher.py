import subprocess
import webbrowser
import threading
import time



def run_flask_app():
    subprocess.Popen(['python', 'app.py'])
    # Wait for the server to start
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:5000')

def start_webpage():
    thread = threading.Thread(target=run_flask_app)
    thread.start()

start_webpage()