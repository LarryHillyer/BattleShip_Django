from django.db import models

import jsonfield

class Grid(models.Model):
    grid_data = jsonfield.JSONField(null = True)