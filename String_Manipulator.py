# This class contains methods to generate permutations and combinations of strings
class Manipulator(object):

    def __init__(self,info):
        self.visited = []
        self.data = info

    def permute(self):
        if len(self.visited) == len(self.data):
            print("".join(self.visited))
            return
        for ch in self.data:
            if ch in self.visited:
                continue
            else:
                self.visited.append(ch)
                self.permute()
                self.visited.pop()

    def generate_combinations(self):
        data_str = self.data
        self.combine(data_str)

    def combine(self,data_str):
        for index,ch in enumerate(data_str):
            if ch in self.visited:
                continue
            else:
                self.visited.append(ch)
                print("".join(self.visited))
                if index < len(data_str) - 1:
                    self.combine(data_str[index:])
                self.visited.pop()

if __name__ == '__main__':
    str_oj = Manipulator("abc")
    str_oj.permute()
    str_oj.generate_combinations()