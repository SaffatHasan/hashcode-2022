from model import Contributor, Project, RequiredSkill

def parse(path_name):
    with open(path_name) as file:
        nr_contributor, nr_projects = [int(col) for col in file.readline().strip().split(" ")]
        return parse_contributors(file, nr_contributor), parse_projects(file, nr_projects)


def parse_contributors(file, n):
    contributors = []
    for _ in range(n):
        name, num_skills = file.readline().split()
        num_skills = int(num_skills)
        skills = parse_skills()
        contributors.append(Contributor(name, skills))
    return contributors


def parse_skills(file, n):
    return {skill: int(skill_level) for skill, skill_level in file.readline.split() for _ in range(n)}


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
