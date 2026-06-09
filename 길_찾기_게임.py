class Node:
    def __init__(self, nodeinfo):
        self.idx = nodeinfo[0]
        self.x = nodeinfo[1][0]
        self.y = nodeinfo[1][1]
        self.left = None
        self.right = None
        
def preOrder(root):
    ret = []
    stack = [root]
    
    while len(stack) > 0:
        cur = stack.pop()
        ret.append(cur.idx)
        if cur.right != None:
            stack.append(cur.right)
        if cur.left != None:
            stack.append(cur.left)
    
    return ret

def postOrder(root):
    # right -> left -> root로 순회한 뒤, 마지막에 반대로 뒤집기
    ret = []
    stack = [root]
    
    while len(stack) > 0:
        cur = stack.pop()
        ret.append(cur.idx)
        if cur.left != None:
            stack.append(cur.left)
        if cur.right != None:
            stack.append(cur.right)
    
    return ret[::-1]

def solution(nodeinfo):
    answer = []
    
    # 노드에 번호를 붙이고, y가 클수록, 동일하다면 x가 작을수록 앞에 오게 정렬
    nodeinfo_new = [(idx + 1, nodeinfo[idx]) for idx in range(len(nodeinfo))]
    nodeinfo_new.sort(key = lambda x: (-x[1][1], x[1][0]))
    
    # 가장 윗 노드를 root로
    root = Node(nodeinfo_new.pop(0))
    
    # 노드를 하나씩 빼면서 루트를 따라 빈자리를 찾아 연결
    while len(nodeinfo_new) > 0:
        newNode = Node(nodeinfo_new.pop(0))
        cur = root
        while True:
            if newNode.x < cur.x:
                if cur.left == None:
                    cur.left = newNode
                    break
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = newNode
                    break
                cur = cur.right
    
    answer.append(preOrder(root))
    answer.append(postOrder(root))
    
    return answer