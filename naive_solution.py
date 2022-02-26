from typing import List
from model import Project, Contributor
from util import get_role_availability, sort_projects_by_manhours

def solve(projects, contributors):
    """ Try to fill each project with the first available contributor.

    Only assign 1 project per contributor (to avoid running overtime / penalty).
    """
    planned_projects: List[Project] = []
    planned_contributors: List[List[Contributor]] = []

    projects = sort_projects_by_manhours(projects)
    role_availability = get_role_availability(contributors)
    visited = set()

    for project in projects:
        current_contributors: List[Contributor] = []
        for required_skill in project.roles:
            skill, minimum_level = required_skill.name, required_skill.level
            for contributor in role_availability[skill]:
                if contributor.name in visited: # already assigned to another
                    continue
                if contributor.skills[skill] < minimum_level:
                    continue
                current_contributors.append(contributor)
                visited.add(contributor.name)
                break
        
        can_finish = True
        if len(current_contributors) != len(project.roles):
            can_finish = False
        # TODO: unvisit engineers
        if not can_finish:
            # skip current project
            continue
        planned_projects.append(project)
        planned_contributors.append(current_contributors)
    return planned_projects, planned_contributors
