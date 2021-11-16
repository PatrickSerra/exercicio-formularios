from django.core.exceptions import ValidationError

def validate_lowercase(value):
    if value.lower() != value:
        raise ValidationError("{} is not lowercase.".format(value))
    
    