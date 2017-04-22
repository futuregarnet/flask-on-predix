import os
from app import create_app
from flask_script import Manager, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command('runserver', Server(host='127.0.0.1', port=4999))


@manager.command
def start_on_predix():
    # called to get the app running
    # do database migrations here
    port = os.getenv('PORT')
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    manager.run()