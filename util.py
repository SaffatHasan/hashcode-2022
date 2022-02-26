from collections import defaultdict

def sort_projects_by_manhours(projects):
    projects.sort(key= lambda x: x.manhours(), reverse=True)
    return projects

def get_role_availability(contributors):
    """ Create a map between a particular skill and the contributors who satify it"""
    role_availability = defaultdict(list)
    for contributor in contributors:
        for skill in contributor.skills:
                role_availability[skill].append(contributor)
    return role_availability