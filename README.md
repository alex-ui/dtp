# dtp
Dot-Peachy elang.

## Summary
This language is what is known as an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language). One of the unique features it has is that a lot of its keywords mimic the shape of the word whose meaning is exactly the function.

## Syntax
### Basics
- Lines must have the end-of-line character, which is "¤".
- Numerical values are written like numbers (example: 12). Strings are written in-between « and » (example: «hi»).
### Variables
Variables, like in any other programming language, have data types. There's a list of keywords, and each keyword corresponds one of these types. To declare a variable, a dot must be written before the keyword itself. Here's the current list of implemented keywords:
- ```dtp : ``` -> Integer (example: ```dtp .: foo 12¤```)
- ```dtp ∿ ``` -> String (example: ```dtp ∿: my_string ```)

Multiple variables within the same data type line are separated by commas (example: ```dtp .: foo 12, bar 24¤```).

### Functions
DTP has [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)). There are two types of functions:
#### Standard functions
These functions are included in the DTP standard library. Here's the current list of implemented standard functions:
- ```dtp :* ``` -> Print (example: ```dtp :*(«hi»;foo;bar)```)
  * It prints the arguments inside of it.
  * Its syntax is the following:
    * Basic structure -> ```dtp :*()¤ ```
    * Arguments separated by semicolons (";").
    * Variable names within « and » are taken as string literals to avoid issues.
    * Undeclared variables that have been called by their names in ``` dtp:* ``` are printed as "?".
#### Custom functions
These functions are user-defined. They haven't been implemented yet.
