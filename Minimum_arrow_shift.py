"""
You are given a string S representing a sequence of N arrows. Each arrow in the sequence points in one of the four directions: up("^"), down("v"), lef("<") or right(">"). In one move, you can rotate an arrow as shown in the image below:

^ ----- <
> ----- ^
v ------ >
< ------ v


Write a function:
def solution(S)

that, given a string S of length N denoting the directions of the arrows, returns the minimum number of moves required to make all of the arrows point in the same direction.

Example: For S ="vv>>vv" the function should return 4. It is optimal to rotate arrows so that all of the point right


Asume that:

- N is an integer within the range [1..100]
string S is made only the following characters: '<','^','>' and/or 'v'

In your solution, focus on correctness. The performance of your solution will not be the focus on the assessment

"""
import os

class Arrow:
    def solution(self, A : list) -> int:
        up = A.count('^')
        down = A.count('v')
        left = A.count('<')
        right = A.count('>')

        total_up = right + 2*down + 3*left
        total_down = left  + 2*up + 3*right
        total_left = up + 2*right + 3*down
        total_right = down + 2*left + 3*up

        return min(total_up,total_down,total_left,total_right)


if __name__ == "__main__":
    os.system('cls||clear')
    Test = Arrow()
    test_cases = [
    "vv>>vv", #Expected 4
    "<<<<<", #expected 0
    "<<^>>", #expected 5........v -> 10, ^ -> 8 , < -> 5, > -> 7
    "<", #Expected 0
    "^^<<>>^^", #Expected 8 ........ v -> 16, ^ ->8, > -> 16, < -> 8
    "vvvv", #Expected 0
    "^<^v<<^>", #Expected 8 ......... v -> 12, ^ -> 12, < -> 8,  > -> 16
    "^^^>>>>>vvv<<<<" #Expected 20
    ]

    for i in test_cases:
        print(f"The minimum arrow to shift in the arrow string {i} is: {Test.solution(i)}")