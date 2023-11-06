% Define the possible professions
profession(smith).
profession(baker).
profession(carpenter).
profession(tailor).

% Define the father-son relationships and constraints
father_son_relation(Father, Son) :-
    profession(Father),
    profession(Son),
    Father \= Son.

% Constraint: Baker has the same profession as Carpenter's son
baker_carpenter_relation :-
    father_son_relation(carpenter, Son),
    profession(Son),
    Son = baker.

% Constraint: Smith's son is a baker
smith_son_baker_relation :-
    father_son_relation(smith, Son),
    profession(Son),
    Son = baker.

% Find the solution
find_solution(Father, Son) :-
    father_son_relation(Father, Son),
    baker_carpenter_relation,
    smith_son_baker_relation.