class user:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user1 = user("codetree", 10)

user2_id, user2_levle = input().split()

user2 = user(user2_id, user2_levle)

print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")