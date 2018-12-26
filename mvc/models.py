class Users:
    def __init__(self, name, religion):
        self.name = name
        self.religion = religion

    def get_json(self):
        return {"name": self.name,
                "religion": self.religion
        }