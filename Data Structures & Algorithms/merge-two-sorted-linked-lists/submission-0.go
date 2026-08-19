/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

    // Get current node larger value
    if list2 == nil {
        return list1
    }
    if list1 == nil {
        return list2
    }
    if list1.Val > list2.Val {
        node := list2
        appendage := mergeTwoLists(list1, list2.Next);
        node.Next = appendage;
        return node;
    } else {
        node := list1
        appendage := mergeTwoLists(list1.Next, list2)
        node.Next = appendage;
        return node;
    }
}
