from typing import List

class RequiredSkill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Project:
    def __init__(self, name: str, number_days: int, score: int, best_before_date: int, roles: List[RequiredSkill]):
        self.name = name
        self.number_days = number_days
        self.score = score
        self.best_before_date = best_before_date
        self.roles = roles

    def manhours(self):
        return self.score / (self.number_days * len(self.roles))

class Contributor:
    def __init__(self, name: str, skills: dict):
        self.name = name
        self.skills = skills