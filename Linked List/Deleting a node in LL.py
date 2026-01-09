def Node():
    def __init__(self, data, next=None):
        self.data= data
        self.next=next
if __name__=="__main__":
    arr=[1,2,3,4,5]
    head = Node(arr[0])
    current=head
    for i in range(1, len(arr)):
        current.next=Node(arr[i])
        current=current.next
    # Deleting node with value 2
    key=2

    if head is None:
        break
    if head.data==key:
        head=head.next
        break
    temp=head