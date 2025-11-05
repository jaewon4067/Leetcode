class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()     # 결과 리스트 시작점
    cur = dummy            # 현재 위치
    carry = 0              # 자리 올림 숫자
    
    while l1 or l2 or carry:
        # 값이 있다면 node 값, 없다면 0 사용
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        total = x + y + carry
        carry = total // 10
        digit = total % 10
        
        cur.next = ListNode(digit)
        cur = cur.next
        
        # 다음 노드로 이동
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next
