import importlib

from django.conf import settings
from django.contrib import admin
from django.db import models

from . import models as core_models

# https://stackoverflow.com/questions/63172053/list-classes-in-python-file
def get_models(module):
    my_models = []
    for item in module.__dict__.values():
        if type(item) == models.base.ModelBase:
            my_models.append(item)
    return my_models


try:
    models_to_register = getattr(settings, "TELEGRAM_MODELS_IN_ADMIN_SITE")
    register_all_models = False
except AttributeError:
    register_all_models = True

if register_all_models:
    my_models = get_models(core_models)
    for model in my_models:
        admin.site.register(model)
else:
    models_module = importlib.import_module("core.models")
    for model_str in models_to_register:
        try:
            model = getattr(models_module, model_str)
            admin.site.register(model)
        except AttributeError:
            raise AttributeError(f"The model {model_str} cannot be registered")
