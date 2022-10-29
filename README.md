# DietProblem
OR-Tool for a personalizable version of the original "Stigler Diet Problem" by adjusting the parameters.

This project is built to be a more practical and personalize version of the original "Stigler Diet Problem".
The main files for this are first the "Nutrients_ID.csv", which is basically the dataset on which the solver operates and the "solver.py", which is the actual solver.

In the solver you can input your desired boundaries for every of the about 290 diff rents micro- and macro-nutrients.
From this point on you can personalize multiple aspects of the solver like:
- weight (sets boundaries of some nutrients dependent on your weight)
- calculation period ⇾ you can set the solver to calculate your specifications for n-days, for example you can make it calculate your needs for 2 days or a week or even a whole month in advance (calculations might not apply if n is to big and the daily needs are not sufficiently covered)
- maximal amount of any single food in 1 day (for example)
- blacklist: blacklist items you dont want to have in your daily foods (e.g. octopus or meats or oysters etc.)
- (extremely-/custom-) reduced lists: reduce some foods that you dont want to eat as much of (e.g. butter, beans, bread, protein powder, etc.)
- sorting function: you can choose if the daily foods are displayed sorted by grams or ID or name and ASC or DESC

If the restrictions are to tight, the solver might not be able to calculate an optimized solution. In this case removing the last changed boundary might help. The arrows under the nutrition output also indicate that this specific nutrient is on the edge and might be sensitive to changes in a particular direction.
