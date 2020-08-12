#!/usr/bin/python3
from models.base_model import BaseModel

#kwargs={ 'name': "California" }
my_model = BaseModel()
my_model.my_number = 89
print(str(my_model))
print(my_model.to_dict())