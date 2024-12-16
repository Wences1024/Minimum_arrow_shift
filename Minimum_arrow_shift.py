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
    "<<^>>", #expected 5
    "<", #Expected 0
    "^^<<>>^^", #Expected 8
    "vvvv", #Expected 0
    "^<^v<<^>", #Expected 8 
    "^^^>>>>>vvv<<<<" #Expected 20
    ]

    for i in test_cases:
        print(f"The minimum arrow to shift in the arrow string {i} is: {Test.solution(i)}")