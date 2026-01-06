class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
    

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    num=0
    head=Node(arr[0])
    current=head
    for i in range(1,len(arr)):
        current.next=Node(arr[i])
        current=current.next
    
    new_node=Node(num)
    new_node.next=head
    head=new_node
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")