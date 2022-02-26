from parser import parse
import naive_solution
import linear_solution
from output import score


if __name__ == '__main__':
    files = [
        "input/a_an_example.in.txt",
        "input/b_better_start_small.in.txt",
        "input/c_collaboration.in.txt",
        "input/d_dense_schedule.in.txt",
        "input/e_exceptional_skills.in.txt",
        "input/f_find_great_mentors.in.txt"
    ]
    for f in files:
        contributors, projects = parse(f)
        naive = naive_solution.solve(projects, contributors)
        linear = linear_solution.solve(projects, contributors)
        print(f"{f} {score(naive)=} {score(linear)=}")




