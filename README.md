# Final Project - Flocking
By: Jonah Boe, Rhett Redd, Matthew Shaw
For: CS 5110 - Utah State University

## Outline
This project shows how voting mechanisms can be used to assist in the 
re-election of the leading agent in flocking algorithms. It also explores the
effects that the different voting mechanisms effect the resulting leaders
attributes.

## Commands
Run with default settings:
```commandline
python Flocking.py
```
Arguments:
```commandline
-v (b, p, v) # Set voting mechanism 
             # b: Borda (default)
             # p: Plurality with elimination
             # v: Veto with elimination (of most least voted for)
```
