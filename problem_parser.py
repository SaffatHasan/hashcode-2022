from model import Contributor, Project, RequiredSkill

def parse(path_name):
    with open(path_name) as file:
        nr_contributor, nr_projects = [int(col) for col in file.readline().strip().split(" ")]
        contributors = parse_contributors(file, nr_contributor)
        projects = parse_projects(file, nr_projects)
        return projects, contributors


def parse_contributors(file, n):
    contributors = []
    for _ in range(n):
        name, num_skills = file.readline().split()
        skills = parse_skills(file, int(num_skills))
        contributors.append(Contributor(name, skills))
    return contributors


def parse_skills(file, n):
    skills = {}
    for _ in range(n):
        skill, level = file.readline().split()
        skills[skill] = int(level)
    return skills

def parse_projects(file, n):
    projects = []
    for _ in range(n):
        name, number_days, score, best_before_date, nr_roles = file.readline().strip().split()
        roles = []
        for _ in range(int(nr_roles)):
            skill_name, skill_min_level = file.readline().split()
            roles.append(RequiredSkill(skill_name, int(skill_min_level)))
        projects.append(Project(name, int(number_days), int(score), int(best_before_date), roles))

    return projects
