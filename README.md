# A-B-testing-for-mobile-game-retention
-------------------------------------------------------
In the mobile game cookie cats the player will eventually reach a timegating mechanic where they cannot continue until the next day. The developers of the game want to test if moving the time-gate from gate 30 to gate 40 will improve player retention.

In this project I perform A/B testing for the player retention in the two groups of players who have been randomly assigned to either be time-gated at gate 30 or gate 40. I do this by first bootstrapping a probability distribution for the player retention at both gates and comparing their means. 

![](Images/Cookie%20Cats%20KDE%20comparison.png)

We can see in our KDE plot that there is a difference in the means of the sampled retention rates for the two groups.

We can further prove this with a Z-test. A Z-test of both the 1-day and 7-day retention rates provides the following.

![](Images/Cookie%20Cats%20Z-test.PNG)
