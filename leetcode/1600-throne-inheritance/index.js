/*
    1st: DFS + hashtable
    - the preorder traversal = the logic of inheritance
    - use a boolean flag to indicate whether a person is alive
    - use a hashtable to store the { name: node } to save time on finding a node for birth() and death()

    Time of birth()                 O(1)
    Time of death()                 O(1)
    Time of getInheritanceOrder()   O(N) N: total number of all nodes
    Space                           O(N)
    680 ms, faster than 53.57%
*/

class Node {
    constructor(name = '#') {
        this.name = name
        this.children = []
        this.isAlive = true
    }
}

/**
 * @param {string} kingName
 */
var ThroneInheritance = function(kingName) {
    this.root = new Node()
    this.root.children.push(new Node(kingName))
    this.ht = {}
    this.ht[kingName] = this.root
};


/** 
 * @param {string} parentName 
 * @param {string} childName
 * @return {void}
 */
ThroneInheritance.prototype.birth = function(parentName, childName) {
    const parent = this.ht[parentName]
    const newNode = new Node(childName)
    parent.children.push(newNode)
    this.ht[childName] = newNode
};

/** 
 * @param {string} name
 * @return {void}
 */
ThroneInheritance.prototype.death = function(name) {
    const target = this.ht[name]
    target.isAlive = false
};

/**
 * @return {string[]}
 */
ThroneInheritance.prototype.getInheritanceOrder = function() {
    const arr = []
    const preOrder = (node) => {
        if (node == null) {
            return
        }
        if (node.isAlive) {
            arr.push(node.name)
        }
        for (let child of node.children) {
            preOrder(child)
        }
    }
    preOrder(this.root)
    return arr.slice(1, arr.length)
};

/** 
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */