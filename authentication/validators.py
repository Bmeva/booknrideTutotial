from django.core.exceptions import ValidationError
import os

def allow_imageonly_validators(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extension = ['.jpg', '.png', '.jpeg']
    
    if not ext.lower() in valid_extension:
        raise ValidationError('unsurported file format selected. You can only select' + str(valid_extension))

#
mylist = ['banana', 'oranges', 'apples']

#tupple
role = ('Customer', 'Driver', 'User')

#dictionries
empty_dict = {}

age = {'Evans': 25, 'name': 'Alice', 'salary': 5000}

#

