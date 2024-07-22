class Pokemon:
    def __init__(self, name, type, abilities, height, weight, image, capture_id=None):
        self.name = name
        self.type = type
        self.abilities = abilities
        self.height = height
        self.weight = weight
        self.image = image
        self.capture_id = capture_id

    def __str__(self):
        if self.capture_id:
            return f"{self.capture_id}: {self.name} ({self.type}) [{self.height}km, {self.weight}kg] - {self.abilities} - {self.image}"
        return f"{self.name} ({self.type}) [{self.height}km, {self.weight}kg] - {self.abilities} - {self.image}"
