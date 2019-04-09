# Atypical Riddle

Batman is an ​ **atypical** "superhero". Unlike ​Spider-man​, ​Batman has no special powers (unless you count
being ​ _filthy_ ​ _rich_ a superpower). That said, he is, for better or worse, greatly respected for being a
crime-fighter by his many fans. Despite his dour demeanor, ​Batman at times displays moments of humor
and periodically manifests his modest intellect.

Find all the pairs of ​ 5 ​-digit numbers that use the digits ​ 0 through ​ 9 once each, such that the first
number divided by the second is equal to some integer ​N​, where ​N is between ​ 2 and ​ 100 (inclusive).

That is, given the digits ​0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and a number ​N​, find all permutations of these
digits such that:

##### abcde / fghij = N

where each letter represents a different digit. The first digit of one of the numerals is allowed to be 0.
Because ​Batman lacks any significant superpower (besides money), he begs that you help him defeat the
Riddler​ by using your ​programming superpowers​.

## Input

Each line of input consists of a valid integer ​N​. An input of ​ 0 terminates the program (no output should be
displayed for it).
61
62
0

## Output

The program should display ​ **ALL** pairs of numerals that match the description above. The numerators
should be sorted by increasing numerator and denominator and displayed in the following format:

XXXXX / XXXXX = N

XXXXX / XXXXX = N

...

If there are no pairs of numerals satisfying the atypical division condition, then the program should
display: "There are no solutions for N".
Separate the output for two different values of ​N​ by a blank line.

There are no solutions for 61.

79546 / 01283 = 62

94736 / 01528 = 62
