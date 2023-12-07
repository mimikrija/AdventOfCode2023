# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2023 :sparkles: :snake: :christmas_tree:

Ho, ho, ho, welcome to my 2023 Advent of Code repository!
My goal this year:
- solve the first 10 puzzles within 24h of their release
- learn some Kotlin - [My Kotlin repo](https://github.com/mimikrija/KotlinOfCode2023)

My previous AoC repositories: [2015](https://github.com/mimikrija/AdventOfCode2015), [2016](https://github.com/mimikrija/AdventOfCode2016), [2017](https://github.com/mimikrija/AdventOfCode2017), [2018](https://github.com/mimikrija/AdventOfCode2018), [2019](https://github.com/mimikrija/AdventOfCode2019), [2020](https://github.com/mimikrija/AdventOfCode2020), [2021](https://github.com/mimikrija/AdventOfCode2021)

## Solutions overview


Puzzle | Solution(s) | Remarks |
---    |---    |----
[Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1) | [Python](python/01.py) | Search for the first occurence of a reversed word starting from the end of the line to avoid the overlapping issue in words such as "oneight". |
[Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2) | [Python](python/02.py) | The most difficult part is parsing - I used regex again (some say it is overkill but I kinda like it here). In first part, a game is disqualified if any of the cube quantities (in any of the sets) is greater than a specified value per cube color. In the second part we need to find per color maximums.
[Day 3: Gear Ratios](https://adventofcode.com/2023/day/3) | [Python](python/03.py) | `re.finditer` to simultaneously find positions and numbers and then classic set/neighbor operations to solve both parts of the puzzle. I think pt2 could be nicer but it's ok.
[Day 4: Scratchcards](https://adventofcode.com/2023/day/4) | [Python](python/04.py) | I think this one was the most straightforward puzzle so far. The second part sounds tricky at first, but we actually have to go through the list of cards only once (because the winning cards only affect copying of cards _after_).
[Day 5: If You Give A Seed A Fertilizer] | [Python](python/05.py) | I am sure I will not understand what I wrote when I look at it in a couple of days.. Anyway for pt2 I worked with ranges and their intersections, take into account "holes" in intersections which result in a different resulting range. Anyway, boring and tedious.
[Day 6: Wait For It](https://adventofcode.com/2023/day/6) | [Python](python/06.py) | The solution range is equal to the determinant of the quadratic equation which describes the motion of boats. However we need to pick only integer solutions which satisfy the equation which is why I needed to play around with `ceil`.
[Day 7: Camel Cards](https://adventofcode.com/2023/day/7) | [Python](python/07.py) | This is my favourite puzzle this year! It is interesting how many conditions for Joker cards collapse into cases of how many groups of cards there are. I think my solution would be nicer if there was a way to provide an optional argument to the sorting function!
