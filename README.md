# Gale-Shapley Matching

This is a simple implementation of the Gale-Shapley Matching Algorithm for one-to-one matching. It takes an input of 2-2D lists of n by n size, `malePreferences` and `femalePreferences`. As in the original Gale-Shapley example (a 1960s marriage-matching algorithm), male preferences represent the proposer preferences and female preferences represent the proposee preferences. 

It will generate a set of stable matches, meaning that no proposer and proposee who are not matched to each other simultaneously prefer each other to their matches.

This algorithm has a male- or proposer-preference in that the proposer will receive the best possible stable match for him/her, while the proposee will receive the worst possible stable match for him/her.

## Preference Structure

`malePreferences` is organized such that `malePreferences[i]` is the ranked order of preferences of proposer `i`. Therefore, `malePreferences[i][0]` represents the first choice of proposer `i`, while `malePreferences[i][n-1]` represents the last choice of proposer `i`. 

The same is true of `femalePreferences`, with `femalePreferences[i]` representing the ranked order preferences of proposee `i`.
