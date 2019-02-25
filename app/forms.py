from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import validators

class UploadForm(FlaskForm):
    file = FileField('Choose a image file',[validators.Required("File needed"),validators.Regexp("\.(jpg|png|jpeg|)",message="Invalid file")])