function insertNodeAtHead(head, data) {
    if (head == null) {
        return new SinglyLinkedListNode(data);
    }
    
    var node = new SinglyLinkedListNode(data);
    
    node.next = head;
    return node;    
        
}
