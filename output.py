from typing import List
from model import Contributor, Project

def write(output_path: str, planned_projects: List[Project], planned_assignments: List[List[Contributor]]):
    with open(output_path, "w") as f:
        f.write(f"{len(planned_projects)}\n")
        for project, contributors in zip(planned_projects, planned_assignments):
            f.write(f"{project.name}\n")
            f.write(" ".join(c.name for c in contributors))
            f.write("\n")

def score(planned_projects: List[Project], planned_assignments: List[List[Contributor]]) -> int:
    """ Can know start time based on contributor availability based on assignment to projects"""
    contributor_availability = {}
    result = 0
    for project, assignment in zip(planned_projects, planned_assignments):
        if not verify(assignment):
            return -1
        start_time = 0
        for c in assignment:
            if c not in contributor_availability:
                continue
            start_time = max(start_time, contributor_availability[c])

        project_complete_time = start_time + project.number_days

        # if equal to 0, on time
        # if positive, number of days late
        # if negative, completed early
        penalty = project_complete_time - project.best_before_date 
        if penalty > project.score:
            # no points awarded for current project
            continue

        result += project.score
        if penalty > 0:
            result -= penalty

        for c in assignment:
            contributor_availability[c] = project_complete_time

    return result

def verify(assignment: List[Contributor]):
    # cannot assign one person to two roles for a given project
    if len(assignment) != len(set(assignment)):
        return False
    return True
