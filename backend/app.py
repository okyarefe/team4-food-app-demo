import importlib
import pkgutil

from flask import Flask

import routes


def create_app() -> Flask:
    app = Flask(__name__)
    for module in pkgutil.iter_modules(routes.__path__):
        blueprint = getattr(importlib.import_module(f"routes.{module.name}"), "bp", None)
        if blueprint is not None:
            app.register_blueprint(blueprint)
    return app


app = create_app()
