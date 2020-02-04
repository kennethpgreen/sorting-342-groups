# Sorting alg for aba 3 (CS 342)

## Running Directions

There are 3 files in the repo:
- sorting.py
- class.txt
- nets.txt

To run the program, cd into the repo and run python3 sorting.py
Continue to run the program until a "Done" message is displayed or until there is only one unmatched group. The algorithm will never work if it's not possible to pair all the groups or if it's impossible for a group to get one of their preferences.
The algorithm will use the test data to start. 
Replace the data in class.txt and nets.txt with the desired data to sort.

The algorithm will create a document called output.txt when it is finished. There are still few errors in the code that result in noncomplete pairings. Continue to run the algorithm until the Done message displays. See section labeled Bugs that explain two of the bugs that will result. One thing

## Algorithm Overview

This algorithm works by taking the first group in a list and finding the next group that has the same first ranking. The algorithm will pair the two groups together and remove both of them from the list. If the pair has a size of two (both were individuals), the pair will be added back into the groups list. Pairings will either be size 3 or 4. 

Before the algorithm starts, a max amount of groups per topic is determined. The current max size is set at (# of groups / # of topics) X 2. This max size can be changed by adjusting the code on line 72.

If a topic is full (the topic reaches capacity), the topic is removed from the preferences of each group and no additional groups can be placed in this topic. Preferences are then adjusted. For example, if Group 1 prefs 1, 2, 3 and topic 1 is no longer available. Group 1's prefrences will be adjusted to 2, 3.

If there is no other group that has the same first preference, the algorithm will switch the current group's first and second preference.

## Bugs

Note: because we're only looking for this to sort the names once, the code is not completely robust. In certain instances, the algorithm will not complelety finish. As noted previously, continue to run the algorithm until a solution that sorts completely is reached. Here are some of the cases that aren't handled.

1. Sorting ends with 1 extra pair. If there are 11 groups of 2 , it's inevitable that there will be one extra at the end no matter how you sort. The algorithm will display the remaining group for the user to add by hand if they choose to do so.
2. Runtime error. This happens when a group can't be placed in one of their preferences (they're all full). This can be fixed by making the group max capacity larger.


## Algorithm Features
The algorithm is random and does not give some students over others.
It will only result in groups of 3 or 4. 
It guarantees that people will be in 1 of their three preferences or the algorithm will result in a runtime error.

