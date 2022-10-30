#!/usr/bin/python3
"""Defines the  city."""
from models.base_model import BaseModel

class City(BaseModel):
    """Repreesents a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name =""
