from django.db import models

import jsonfield

class Grid(models.Model):
    grid_data = jsonfield.JSONField(null = True)

class ShipYard(models.Model):
    ships = jsonfield.JSONField(null = True)