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
[Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5) | [Python](python/05.py) | I am sure I will not understand what I wrote when I look at it in a couple of days.. Anyway for pt2 I worked with ranges and their intersections, take into account "holes" in intersections which result in a different resulting range. Anyway, boring and tedious.
[Day 6: Wait For It](https://adventofcode.com/2023/day/6) | [Python](python/06.py) | The solution range is equal to the determinant of the quadratic equation which describes the motion of boats. However we need to pick only integer solutions which satisfy the equation which is why I needed to play around with `ceil`.
[Day 7: Camel Cards](https://adventofcode.com/2023/day/7) | [Python](python/07.py) | This is my favourite puzzle this year! It is interesting how many conditions for Joker cards collapse into cases of how many groups of cards there are. ~~I think my solution would be nicer if there was a way to provide an optional argument to the sorting function!~~ There is a way, so I reduced code duplication!
[Day 8: Haunted Wasteland](https://adventofcode.com/2023/day/8) | [Python](python/08.py) | LCM for part 2. Since the instructions repeat themselves I ~~created a generator function for it~~ imported `itertools.cycle` (in my uncomitted initial solution I kept poping and appending a `deque`).
[Day 9: Mirage Maintenance](https://adventofcode.com/2023/day/9) | [Python](python/09.py) | No comment.
[Day 10: Pipe Maze](https://adventofcode.com/2023/day/10) | [Python](python/10.py) | "BFS" for the first part to find the loop. After that, clean up the "pipe map" from all the pipe parts not belonging to the loop and then use regex to find groups of pipes. Scan each line of the map left to right and change in/out status dependent on the pipe configuration encountered. For example `L--J` is like a U configuration which means that if we started from the outside we will remain on the outside once we pass it. On the other hand `F-J` or `|` configurations change the status from in to out and vice versa. I think that was a neat use of the `xor` operator.
[Day 11: Cosmic Expansion](https://adventofcode.com/2023/day/11) | [Python](python/11.py) | Replace coordinates sequentially by the "expansion factor" if there are "gaps" between coordinates.
[Day 12: Hot Springs](https://adventofcode.com/2023/day/12) | [Python](python/12.py) | Dynamic programming is recursion + memoization, remember this MAJA!! And never stop trusting the Recursion Fairy :sparkles:
[Day 13: Point of Incidence](https://adventofcode.com/2023/day/13) | [Python](python/13.py) | This one was very interesting - we were supposed to find a line which mirrors the image - I used the same function on a normal and on the image rotated by 90 degrees. In second part instead of trying out all combinations with a missing image I just changed the match condition to be that the lengths of original image and mirrored image differ by 1.
[Day 14: Parabolic Reflector Dish](https://adventofcode.com/2023/day/14) | [Python](python/14.py) | This one was fun! In second part it was a bit of a headache to find the cycle but ok.
[Day 15: Lens Library](https://adventofcode.com/2023/day/15) | [Python](python/15.py) | Honestly I don't even remember that I solved this one. The code looks simpler than what I'd expect form reading the puzzle...
[Day 16: The Floor Will Be Lava](https://adventofcode.com/2023/day/16) | [Python](python/16.py) | The kicker for this one was my realization that beams don't end but are in continuous loops.
[Day 17: Lens Library](https://adventofcode.com/2023/day/17) | [Python](python/17.py) | Dijkstra. My main issue was not keeping track of both positions _and_ last directions. I think my logic for calculating heat in next positions is _somewhat_ convoluted...
[Day 18: Lavaduct Lagoon](https://adventofcode.com/2023/day/18) | [Python](python/18.py) | Shoelace formula! Which I successfully avoided in Day 10...
[Day 19: Aplenty](https://adventofcode.com/2023/day/19) | [Python](python/19.py) | Why does my recursion work like this? I literally tried every combination with returning and storing of `result`, and this works?! If someone can explain my code to me I'd be grateful.
[Day 20: Pulse Propagation](https://adventofcode.com/2023/day/20) | [Python](python/20.py) | Followed [this](https://advent-of-code.xavd.id/writeups/2023/day/20/) tutorial almost to a word. Before that I tried an approach without classes at but it became too convoluted (and surprise, surprise, didn't output correct results). Not very happy with this one, might revisit it.
[Day 22: Sand Slabs](https://adventofcode.com/2023/day/22) | [Python](python/22.py) | For pt2 I could not get it to work even though I already had the "supported by" logic. Again, [this](https://advent-of-code.xavd.id/writeups/2023/day/22/) was very helpful. I started the path construction path but it didn't output correct results...
