import numpy as np
import argparse


def solution(n: int) -> int:
    """Calculate the sum of multiples of 3 or 5 below n"""
    numbers = np.array(range(1,n))
    solution = np.sum(numbers[(numbers%3==0)|(numbers%5==0)])

    return solution


def main():
    """Project Euluer problem 1"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1000, required=False, help='Integer cutoff for problem 1')
    args = parser.parse_args()

    problem_statement = """
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below {}.
    """.format(args.n)
    print(problem_statement)

    answer = solution(n=args.n)

    print("""
        Answer: {}
        """.format(answer)
    )


if __name__ == '__main__':
    main()