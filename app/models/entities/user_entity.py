class User:
    def __init__(self, name="", score=0, stage=0):
        self.name = name
        self.score = score
        self.stage = stage

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_stage(self):
        return self.stage

    def set_stage(self, stage):
        self.stage = stage
