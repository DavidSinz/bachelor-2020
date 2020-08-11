from flask import Flask


def create_app():
    app = Flask(__name__)

    from logicfunction.routes import app as func
    from presentation.routes import app as pres
    from datamanager.routes import app as dmgr

    app.register_blueprint(func)
    app.register_blueprint(pres)
    app.register_blueprint(dmgr)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
