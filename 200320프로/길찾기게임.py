# import sys
# sys.setrecursionlimit(10**6)
# class Tree:
#     def __init__(self,dataList):
#         self.data=max(dataList,key=lambda x :x[1])
#         leftList =list(filter(lambda x :x[0] < self.data[0] , dataList))
#         rightList = list(filter(lambda x :x[0] > self.data[0] , dataList))
#         if leftList != []:
#             self.left=Tree(leftList)
#         else :
#             self.left=None
#         if rightList != []:
#             self.right=Tree(rightList)
#         else :
#             self.right=None
# def fix(node,postList,preList):
#     postList.append(node.data)
#     if node.left is not None:
#         fix(node.left,postList,preList)
#     if node.right is not None:
#         fix(node.right,postList,preList)
#     preList.append(node.data)
# def solution(nodeinfo):
#     answer = []
#     root = Tree(nodeinfo)
#     postList = []
#     preList = []
#     fix(root,postList,preList)
#     answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,postList)))
#     answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,preList)))
#     return answer

preorder = list() # 귀찮아서 전역으로
postorder = list()
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    order(nodes,levels,0)
    return [preorder,postorder]

def order(n,levels,curlevel):
    cur = n.pop(0) # VISIT
    preorder.append(cur[0]) # PRE-ORDER
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor
            if n[i][1][1] != levels[curlevel+1]: break
            # next floor
            if n[i][1][0] < cur[1][0]: # LEFT CHILD
                order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
            else: # RIGHT CHILD
                order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                break
    postorder.append(cur[0]) # POST-ORDER
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))