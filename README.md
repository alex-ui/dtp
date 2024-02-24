# dtp
Dot-Peachy elang.

## Summary
This language is what is known as an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language). One of the unique features it has is that a lot of its keywords mimic the shape of the word whose meaning is exactly the function. Additionally, it's able to call and print variables using their index slot value.

## Syntax
### Basics
- Lines must have the end-of-line character, which is "¤".
- Numerical values are written like numbers (example: 12). Strings are written in-between « and » (example: «hi»).
### Variables
Variables, like in any other programming language, have data types. There's a list of keywords, and each keyword corresponds one of these types. To declare a variable, a dot must be written before the keyword itself. Here's the current list of implemented keywords:
- ``` : ``` -> Integer (example: ``` .: foo 12¤```)
- ``` ∿ ``` -> String (example: ``` ∿: my_string ```)

Multiple variables within the same data type line are separated by commas (example: ``` .: foo 12, bar 24¤```).

Each variable has its own ID, based on the order of declaration. These IDs are stored as index slots, starting at zero.

### Functions
DTP has [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)). There are two types of functions:
#### Standard functions
These functions are included in the DTP standard library. Here's the current list of implemented standard functions:
- ``` :* ``` -> Print (example: ``` :*(«hi»;foo;bar)```)
  * It prints the arguments inside of it.
  * Its syntax is the following:
    * Basic structure -> ``` :*()¤ ```
    * Arguments separated by semicolons (";").
    * Variable names within « and » are taken as string literals to avoid issues.
    * Undeclared variables that have been called by their names in ``` :* ``` are printed as "?".
    * Variable names, values or index slot values can all be printed using various methods. The dot and the underscore serve different purposes: a dot before a variable's name or ID would print the variable's name, while an underscore prints its index slot value if it's before a variable's name (and viceversa). If none are written, a variable's name will print its value, unless it's within « and » (like mentioned before, it'd be treated as a string literal), and an index slot value will just print the number (since it's literally just an integer number, completely unrelated to variable logic). The following arguments are all the possible the cases:
    	 1. ```:*(«foo»)``` -> prints "foo" (not interpreted as a variable name, it's just another word).
      2. ```:*(.foo)``` -> prints "foo" (this is redundant, will print its ID in the future).
      3. ```:*(.0)``` -> prints "foo".
      4. ```:*(foo)``` -> prints "12".
      5. ```:*(_foo)``` -> prints "12".
      6. ```:*(_0)``` -> prints "12".
      7. ```:*(12)``` -> prints "12" (because this is just an integer being printed, not a variable).
      8. ```:*(«12»)``` -> prints "12" (also interpreted as a "word", or, at least, as a string. A one-digit number would be a character if this data type existed).
      9. ```:*(_foo)``` -> prints "0" (the ID where "foo" is, which is the first one in this case, 0. Since just printing the variable name already prints its value, we can use the underscore for this).
      10. ```:*(0)``` -> prints "0" (same case as ```:*(12)```, it's just interpreted as a regular integer number).
      
#### Custom functions
These functions are user-defined. They haven't been implemented yet.
