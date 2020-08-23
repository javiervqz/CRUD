import uuid

class Client:
    def __init__(self,name,company,position,id=None):
        self.name = name
        self.company = company
        self.position = position
        self.id = id or uuid.uuid4()
    
    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['name','company','position','id']