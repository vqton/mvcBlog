# models/__init__.py

import os
import glob
from app import db

# Get a list of all the model files
model_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
model_files.remove(__file__)

# Import all the models
for model_file in model_files:
    model_name = os.path.basename(model_file)[:-3]
    __import__(f"app.models.{model_name}")
