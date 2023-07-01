class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


user1 = Comment("ktk", "Hello classes", 5)

print(user1.username)
print(user1.content)
print(user1.likes)
