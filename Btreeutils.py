import pprint
class Btreeutils(object):
    #Binary tree node
    class Treenode(object):
        def __init__(self, info):
            self.data = info
            self.left = self.right = None

    def create_binary_tree(self,input_array):
        node_dict = {}
        if len(input_array) == 0:
            return None
        root = Btreeutils.Treenode(input_array[0])
        node_dict[0] = root
        for index,ele in enumerate(input_array[1:]):
            if (index + 1) % 2 == 0:
                parent_index = int(((index + 1) - 2) / 2)
            else:
                parent_index = int(((index + 1) - 1) / 2)
            temp = node_dict.get(parent_index)
            if not temp.left:
                temp.left = Btreeutils.Treenode(input_array[2 * parent_index + 1])
                node_dict[index + 1] = temp.left
            else:
                temp.right = Btreeutils.Treenode(input_array[2 * parent_index + 2])
                node_dict[index + 1] = temp.right

        return root

    def create_binary_tree_recursively(self, input_array, pos ,n,root = None,):
        if pos < n:
            root = Btreeutils.Treenode(input_array[pos])
            root.left = self.create_binary_tree_recursively(input_array, 2 * pos + 1,n,root.left)
            root.right = self.create_binary_tree_recursively(input_array, 2 * pos + 2,n,root.right)
        return root


    def is_tree_balanced(self,treeroot):
        if treeroot is None:
            return True
        nodes = []
        depths = []
        nodes.append((treeroot,0))
        #depths.append(0)
        while len(nodes) > 0:
            temp , depth = nodes.pop()
            #you are at a leaf node
            if temp.left is None and temp.right is None:
                if depth not in depths:
                    depths.append(depth)
                #short circuit operation to check if we have already seen leaves with more than 2 depth values
                #if not then check if the diff between the last two depths seen is > 1
                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
            else:
                if temp.left:
                    nodes.append((temp.left , depth + 1))
                if temp.right:
                    nodes.append((temp.right , depth + 1))
        return True


if __name__ == '__main__':
    input_array = [13,12,7,9,21,25]
    result = Btreeutils().create_binary_tree(input_array)
    print(Btreeutils().is_tree_balanced(result))
    #create binary tree recursively
    result = Btreeutils().create_binary_tree_recursively(input_array,0,len(input_array))







