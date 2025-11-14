class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        newNote = Node(data) # Node(data) là tạo ra 1 node mới lấy tham số là data vì chúng ta đã tạo ra class Node rồi
        if head is None: # xét TH1: list lúc này k có giá trị gì cả nên lấy giá trị hiện tại làm head
            head = newNote
            return head
        else:
            curr = head # # Bắt đầu một 'con trỏ' ở đầu danh sách
            while curr.next is not None: 
            
            # Di chuyển 'con trỏ' đến node CUỐI CÙNG
            # (Node cuối là node có .next == None)
               curr = curr.next
            
            curr.next = newNote   # Gắn Node mới của chúng ta vào sau node cuối cùng
        
        # Đề bài yêu cầu luôn trả về node ĐẦU (head)
        # Trong trường hợp này, 'head' không bao giờ thay đổi
        return head
    
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  