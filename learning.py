from resources.user import User

a = []
for i in range(1, 10):
    a.append(i)
b = (1, 5, 3)
new = [x**2 for x in a]
new_x = map(lambda x: x**2, a)
result = filter(lambda x: x % 2, b)
result_new = next(filter(lambda x: x % 2 == 0, b), None)
# print(list(new_x))


users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
c = 1


def check(b):
    return b+c


print(check(2))
