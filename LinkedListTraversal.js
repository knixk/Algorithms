// A simple recursion based solution.

function printLinkedList(head) {
    
    if (head == null) {
        return;
    }
    
    console.log(head.data);
    printLinkedList(head.next);
}
