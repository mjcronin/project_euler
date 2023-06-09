import numpy as np
import argparse


def solution(n: int) -> None:
    """Calculate the sum of even valued terms of the Fibonacci sequence below n."""
    fibmat = np.array([[1,1],[1,0]])
    fibnums = np.array([1])
    newnums = np.array([[2],[1]])

    while newnums[0] < n:
        fibnums = np.append(fibnums, newnums[0])
        newnums = fibmat@newnums

    fibnums = fibnums.flatten()

    answer = fibnums[(fibnums%2==0)].sum()

    return answer


def main():
    """Project Euluer problem """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        default='4000000',
        type=int,
        required=False,
        help='Integer cutoff for problem 2'
    )
    args = parser.parse_args()

    problem_statement = """
        Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

            1, 2 ,3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values do not exceed {}, find the sum of the even-valued terms.
    """.format(args.n)
    print(problem_statement)

    answer = solution(args.n)

    print("""
        Answer: {}
        """.format(answer)
    )


if __name__ == '__main__':
    main()