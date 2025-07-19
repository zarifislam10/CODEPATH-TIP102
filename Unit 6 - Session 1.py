# Set: 1
# Problem 1
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    # T is together F is just n_pointer
    state = True

    head = dna_strand
    n_pointer = head
    m_pointer = head

    while n_pointer or m_pointer:
        if state:
            count = 1
            while count < m:
                m_pointer = m_pointer.next
                n_pointer = n_pointer.next
                count += 1
            state = False
        else:
            count = 0
            while n_pointer.next and count < n:
                n_pointer = n_pointer.next
                count += 1
            state = True
            
            m_pointer.next = n_pointer.next
            m_pointer = m_pointer.next
            n_pointer = n_pointer.next
        
    return head

    
        

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11)))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))


# Problem 2

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    head = protein
    slow = fast = head
    res = []
    is_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            is_cycle = True
            break

    if not is_cycle:
        return res
    else:
        marker = slow
        res.append(slow.value)
        slow = slow.next

        while slow != marker:
            res.append(slow.value)
            slow = slow.next

    return res





protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))