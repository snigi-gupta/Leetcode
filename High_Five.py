# https://leetcode.com/problems/high-five/
class HighFive:
    def highFive(self, items):
        temp_map = dict()
        for student in items:
            if student[0] not in temp_map.keys():
                temp_map[student[0]] = [student[1]]
            else:
                temp_map[student[0]].append(student[1])

        result = []
        for key in temp_map:
            result.append([key, int(sum(sorted(temp_map[key], reverse=True)[:5]) / 5)])
        return result


if __name__ == "__main__":
    input = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]] #ans [[1, 87], [2, 88]]
    obj = HighFive()
    print(obj.highFive(input))


