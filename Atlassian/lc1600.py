class ThroneInheritance:
    def __init__(self, kingName: str):
        self.lineage = {}
        self.dead = set()
        self.kingName = kingName
        self.lineage[kingName] = []

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.lineage:
            self.lineage[parentName].append(childName)
        else:
            self.lineage[parentName] = [childName]
        self.lineage[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> list:
        order = []

        def traversal(name):
            if name not in self.dead:
                order.append(name)
            for child in self.lineage.get(name, []):
                traversal(child)

        traversal(self.kingName)
        return order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()