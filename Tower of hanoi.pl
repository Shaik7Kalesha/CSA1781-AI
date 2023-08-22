% Define the predicate for solving Towers of Hanoi
% hanoi(N, A, B, C) - Move N disks from tower A to tower C using tower B as auxiliary.
hanoi(1, A, _, C) :-
    write('Move disk 1 from '), write(A), write(' to '), write(C), nl.
hanoi(N, A, B, C) :-
    N > 1,
    M is N - 1,
    hanoi(M, A, C, B),  % Move top M-1 disks from A to B using C
    write('Move disk '), write(N), write(' from '), write(A), write(' to '), write(C), nl,
    hanoi(M, B, A, C).  % Move the M-1 disks from B to C using A

% Define a predicate to solve Towers of Hanoi for a given number of disks
solve_hanoi(N) :-
    hanoi(N, 'A', 'B', 'C').

% Example usage:
% solve_hanoi(3).
