import sys
sys.path.insert(0, '/home/gui/Documents/webportfolio/webportfolio')
sys.path.insert(1, '/home/gui/Documents/webportfolio/webportfolio/venv/lib/python3.11.2/site-packages')  # Adjust the Python version

from main import app as application

if __name__ == '__main__':
    application.run()
