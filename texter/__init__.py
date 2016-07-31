import os
from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "texter.config.DevelopmentConfig")
app.config.from_object(config_path)


from . import views
from . import filters
from . import login