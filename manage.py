from flask_script import Manager, Server

from mongo_alchemy_sample.app import create_app

manager = Manager(create_app)

manager.add_option('-c', '--config', default='Development', choices=('Production', 'Development', 'Testing'),
                   required=False, dest='config')
manager.add_command('runserver', Server(host='0.0.0.0', use_debugger=True, use_reloader=True, threaded=True))

if __name__ == '__main__':
    manager.run()
