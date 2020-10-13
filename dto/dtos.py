import json


class BioData:

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"BioData name= {self.name} age={self.age}"

    def to_json(self):
        return json.dumps({'name': self.name, 'age': self.age}, indent=2)

    @classmethod
    def from_json(cls, json_data):
        return BioData(name=json_data['name'], age=json_data['age'])

