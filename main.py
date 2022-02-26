from problem_parser import parse
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

    algorithms = {
        "naive": naive_solution, 
        "linear": linear_solution,
    }

    for name, algo in algorithms.items():
        total_score = sum(
            score(*algo.solve(*parse(f))) for f in files
        )
        print(f"{name:10} {total_score:10,}")
