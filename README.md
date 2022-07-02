# Python Tutorial and Project

*August, 2021*

## Introduction

This repository contains 2 components. One component is a programming project that will have a student implement a two player battleships game. The second component is a Python tutorial that will prepare someone who is new to programming with the necessary Python to complete the project. 

## Python Battleships Tutorial 

Below is an outline of the topics in the tutorial. 

* Variables and Primitive Data Types
    * Declaring Variables
    * Viewing Data Types
    * Casting
    * Constants
* Integer and String Operations
    * Integer Addition and Subtraction
    * Updating Shortcut
    * String Concatenation
* Control Flow I: Conditional Statements
    * Comparison Operators
    * Primitive Boolean Conditions
    * Building Compound Boolean Conditions
    * Negating Boolean Conditions
    * if-elif-else Statements
    * Ternary Operator (if-else shortcut)
* Control Flow II: Loops
    * While Loops
    * For Loops
    * Nested Loops
* Printing
    * Printing Multiple Data Types
    * The Newline Character (\n)
    * Printing on the Same Line
* Lists
    * Creating Lists
    * Indexing a List
    * Adding to a List
    * Two-dimensional Lists
    * The range() Function (What does for in really mean?)
* Mutability
    * Idea of a Pointer
    * Tuple, the Immutable List
    * Copying Lists and the Shallow Copy
    * What about Primitives? Are they Mutable? 
* Functions
    * Why do we need functions? (Introduction to Modularity)
    * Parameters v. Arguments
    * Variables inside a Funcion (and Scope)
    * The Return Statement (How many do we need?)
    * Functions that Edit Input
    * Invoking a Function
    * Returning Multiple Items
* Reading User Input
    * The input() Function
    * String to List (split)
* Organizing Code
    * Modularity II (Libraries)
    * Importing Files
    * Constants II (in Libraries)

The tutorial materials are included `battleships_tutorial/`. 

* `battleships_tutorial.py` contains Python code for the examples in `battleships_tutorial.pdf`. 
* `battleships_tutorial.pdf` contains the Python tutorial for the battleships project.
* `overleaf_project/` contains materials for the [Overleaf](https://www.overleaf.com) project used to build `battleships_tutorial.pdf`. 

## Python Battleships Project

Below is an outline of the topics in the battleships project instructions. 

* Introduction
    * Game Overview
* Provided Files
    * battleships_constants.py
    * battleships.py
    * two_player_battleships.py
* Imports in battleships.py
* Set-up Functions
    * copy_list()
    * create_board()
* Displaying a Board
    * get_display_symbol()
    * display_board()
* Arranging Ships
    * ship_at_pos()
    * place_ship()
    * filtered_print()
    * place_ships()
* Player Turns
    * next_player()
    * player_turn()
    * process_turn()
* Imports in two_player_battleships.py
* Preparing a 2 Player Game
    * init_boards_and_ships()
    * prepare_boards()
* Playing 2 Player Game
    * game_over()
    * play_game()

The project materials are included in `battleships_project/`.

* `battleships_project.pdf` contains the instructions for completing the battleships project. This frequently references `battleships_tutorial/battleships_tutorial.pdf`.
* `overleaf_project/` contains materials for the [Overleaf](https://www.overleaf.com) project used to build `battleships_project.pdf`. 
* `solution/` contains a solution to the battleships project.
* `starter_kit/` contains the starter code for completing the assignment.
* `tests/` contains unit tests for testing the functionality of a battleships project implementation.
    
