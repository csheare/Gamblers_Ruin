# Gamblers Ruin

## What is a Gambler's Ruin?

Two gamblers that start with i amounts of money and probability p of winning, play rounds of a game against each other. If a player wins the game, their i is incremented by 1, and the other player, therefore has lost - meaning she must lose 1.

If it is a fair game both players have the same amount of initial wealth and the same probability of winning a single game.

If one player has finite wealth and 0 expected value, while the other player has infinite wealth - the first player will eventually go broke. This scenario can be modeled by a simple stochastic process: a random walk.


## What is a Stochastic Process?

A stochastic process is any random occurence represented by a collection of random variables with a known probability distribution. These random variables are Bernoulli variables that take on 1 of 2 values.

### Simple Random Walk Example
Suppose you play a game where you win $1 if a fair coin lands on heads but you have to pay $1 if it lands on tails. It is a fair game if the expected value is $0.


### What the code will do?

Allow you to visualize this random walk behavior through an updating graph after each round. The y-axis will represent wealth, while the x-axis will represent # games played.


Sources:
* https://github.com/Arvind-Arik/Gamblers-Ruin
* https://en.wikipedia.org/wiki/Stochastic_process
* 

Ideas:
-http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.32.1642&rep=rep1&type=pdf
