% State representation: state(MLeft, CLeft, BoatPosition, MRight, CRight)

initial(state(3, 3, left, 0, 0)).
goal(state(0, 0, right, 3, 3)).

% Valid state: Ensures that missionaries are not outnumbered by cannibals on either bank.
valid(state(ML, CL, _, MR, CR)) :-
    (ML >= CL ; ML = 0),
    (MR >= CR ; MR = 0).

% Move: Defines the possible moves.
% Move one missionary from left to right.
move(state(ML, CL, left, MR, CR), state(ML1, CL, right, MR1, CR)) :-
    ML1 is ML - 1, MR1 is MR + 1,
    valid(state(ML1, CL, right, MR1, CR)).

% Move two missionaries from left to right.
move(state(ML, CL, left, MR, CR), state(ML1, CL, right, MR1, CR)) :-
    ML1 is ML - 2, MR1 is MR + 2,
    valid(state(ML1, CL, right, MR1, CR)).

% Move one cannibal from left to right.
move(state(ML, CL, left, MR, CR), state(ML, CL1, right, MR, CR1)) :-
    CL1 is CL - 1, CR1 is CR + 1,
    valid(state(ML, CL1, right, MR, CR1)).

% Move two cannibals from left to right.
move(state(ML, CL, left, MR, CR), state(ML, CL1, right, MR, CR1)) :-
    CL1 is CL - 2, CR1 is CR + 2,
    valid(state(ML, CL1, right, MR, CR1)).

% Move one missionary and one cannibal from left to right.
move(state(ML, CL, left, MR, CR), state(ML1, CL1, right, MR1, CR1)) :-
    ML1 is ML - 1, MR1 is MR + 1,
    CL1 is CL - 1, CR1 is CR + 1,
    valid(state(ML1, CL1, right, MR1, CR1)).

% Similar moves for right to left.
move(state(ML, CL, right, MR, CR), state(ML1, CL, left, MR1, CR)) :-
    ML1 is ML + 1, MR1 is MR - 1,
    valid(state(ML1, CL, left, MR1, CR)).

move(state(ML, CL, right, MR, CR), state(ML, CL1, left, MR, CR1)) :-
    CL1 is CL + 1, CR1 is CR - 1,
    valid(state(ML, CL1, left, MR, CR1)).

move(state(ML, CL, right, MR, CR), state(ML1, CL1, left, MR1, CR1)) :-
    ML1 is ML + 1, MR1 is MR - 1,
    CL1 is CL + 1, CR1 is CR - 1,
    valid(state(ML1, CL1, left, MR1, CR1)).

% Depth-first search algorithm to find the solution.
dfs(Path, Node, [Node|Path]) :-
    goal(Node).
dfs(Path, Node, FullPath) :-
    move(Node, NextNode),
    not(member(NextNode, Path)),
    dfs([Node|Path], NextNode, FullPath).

% Query to find the solution.
solve(Solution) :-
    initial(InitialState),
    dfs([], InitialState, Solution).
