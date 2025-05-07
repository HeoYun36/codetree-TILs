class Id:
    def __init__(self, id="", level=0):
        self.id = id
        self.level = level

id1 = Id()
tuple1 = ("codetree", 10)
id1.id, id1.level = tuple1

id2 = Id()
tuple2 = tuple(input().split())
id2.id, id1.level = tuple2

print(f"user {id1.id} lv {id1.level}")
print(f"user {id2.id} lv {id2.level}")
