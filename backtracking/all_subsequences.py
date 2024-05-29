"""
In this problem, we want to determine all possible subsequences
of the given sequence. We use backtracking to solve this problem.

Time complexity [Generating all subsequences]: O(2^n),
Time complexity [Generating and printing all subsequences]: O(n*2^n),
where n denotes the length of the given sequence.
"""

from __future__ import annotations

from typing import Any


def generate_all_subsequences(sequence: list[Any]) -> None:
    """
    Parent function to generate the state space tree.
    We take in the sequence as a list, pass it along with dummy current sequence and
    initial index value of 0.
    >>> generate_all_subsequences(None)
    >>> generate_all_subsequences([])
    []
    >>> generate_all_subsequences([None])
    []
    [None]
    >>> generate_all_subsequences([1,2])
    []
    [2]
    [1]
    [1, 2]
    """
    if sequence is not None:
        create_state_space_tree(sequence, [], 0)


def create_state_space_tree(
    sequence: list[Any], current_subsequence: list[Any], index: int
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly two children.
    It terminates when it reaches the end of the given sequence.
    >>> create_state_space_tree([1,2],[], 0)
    []
    [2]
    [1]
    [1, 2]
    >>> create_state_space_tree(["All", "Algorithms"],[], 0)
    []
    ['Algorithms']
    ['All']
    ['All', 'Algorithms']
    >>> create_state_space_tree([1,2],[], 3)
    []
    """

    if index >= len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()


if __name__ == "__main__":
    seq: list[Any] = [3, 1, 2, 4]
    generate_all_subsequences(seq)

    seq.clear()
    seq.extend(["A", "B", "C"])
    generate_all_subsequences(seq)
