# https://leetcode.com/problems/robot-return-to-origin/
class RobotReturn:
    def judgeCircle(self, moves):
        if moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L"):
            return True
        else:
            return False

    #         temp_map = dict()
    #         for c in moves:
    #             if c not in temp_map.keys():
    #                 temp_map[c] = 1
    #             else:
    #                 temp_map[c] += 1
    #         if "U" not in temp_map.keys():
    #             temp_map["U"] = 0
    #         if "D" not in temp_map.keys():
    #             temp_map["D"] = 0
    #         if "R" not in temp_map.keys():
    #             temp_map["R"] = 0
    #         if "L" not in temp_map.keys():
    #             temp_map["L"] = 0


    #         if temp_map["U"] == temp_map["D"] and temp_map["R"] == temp_map["L"]:
    #             return True
    #         else:
    #             return False

if __name__ == "__main__":
    input = "UD" #ans True
    obj = RobotReturn()
    print(obj.judgeCircle(input))
