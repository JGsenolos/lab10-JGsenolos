# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    """
    Restate:
    Create a code such that it takes a list, when it sees a number, add it to a stack,
    when it sees an operator (/, *, +, -), pop the last two numbers and the do the operation.
    Push the result back into the stack and return the final number.

    Example:
    ["6", "3", "/", "2", "+"] --> Returns 4
    Add 6 and 3 to the stack.
    Pop the two out since the next one is "/"
    6/3 --> 2
    Return 2 to the stack
    ["2", "2", "+"]
    2 + 2 --> 4

    Sketch:

    """
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9

    stack = []

    for token in tokens:
        # Check if token is a number or not
        if token not in ["/", "*", "+", "-"]:
            # The int(converts the string into a number)
            stack.append(int(token))

        else:
            # Pop the two most recent numbers, LIFO so the first one out is the second number (When order matters)
            b = stack.pop()
            a = stack.pop()

            # Do the calculation
            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "/":
                result = a / b

            elif token == "*":
                result = a * b

            # Add back the result into the stack
            stack.append(int(result))

    return stack.pop()


def decode_string(s):
    # Outline:
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    num_stack = []
    str_stack = []
    
    current_num = 0
    current_str = ""    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
    
        elif char == "[":
            num_stack.append(current_num)
            str_stack.append(current_str)

            current_num = 0
            current_str = ""
    
        elif char == "]":
            repeat = num_stack.pop()
            previous = str_stack.pop()

            current_str = previous + current_str * repeat
    
        else:
            current_str += char
    
    return current_str
    


def daily_temperatures(temps):
    # Outline:
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result
    


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Convert strings into mutable lists
    grid = [list(row) for row in grid]

    def dfs(r, c):
        # Check boundaries and whether this is water
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if grid[r][c] == "0":
            return

        # Mark land as visited
        grid[r][c] = "0"

        # Explore all four directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands

    


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
