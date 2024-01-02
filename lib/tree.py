class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      
      nodes_to_visit = nodes_to_visit + node['children']
    return None

  def bread_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      result.append(node['value'])
      nodes_to_visit = nodes_to_visit + node['children']
    
    return result 
'''
Method: takes a node as input and return a list containing the values of the root and all its child nodes
Initialize an empty output list
Initialize a list of nodes to visit and add the root node to it
While are nodes in the nodes to visit list:
  Remove the first node from the nodes to visit list
  Add its value to the output list
  Add its children (if any) to the end of the nodes to visit list
Return the output list
'''