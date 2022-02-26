from model import Contributor, Project
from typing import List


def linear_scheduling(projects: List[Project], contributors: List[Contributor]):
    planned_projects: List[Project] = []
    planned_contributors: List[List[Contributor]] = []

    # Who can satisfy a role
    role_availability = {}

    # When is someone earliest available
    contributor_availability = {}

    for contributor in contributors:
        contributor_availability[contributor] = 0
        for skill in contributor.skills:
            if skill not in role_availability:
                role_availability[skill] = [contributor]
            else:
                role_availability[skill].append(contributor)

    for project in projects:
        current_contributors: List[Contributor] = []
        for required_skill in project.roles:
            skill, minimum_level = required_skill.name, required_skill.level
            # TODO we just need min not sort whole thing
            role_availability[skill].sort(key = lambda c: contributor_availability[c])
            for c in role_availability[skill]:
                if c.skills[skill] < minimum_level:
                    continue
                if c in current_contributors:
                    continue
                current_contributors.append(c)
                break
        
        can_finish = True
        if len(current_contributors) != len(project.roles):
            can_finish = False

        if not can_finish:
            # skip current project
            continue
        
        earliest_start = min(contributor_availability[c] for c in current_contributors)
        finish_time = earliest_start + project.number_days
        for c in current_contributors:
            contributor_availability[c] = finish_time

        planned_projects.append(project)
        planned_contributors.append(current_contributors)
    return planned_projects, planned_contributors