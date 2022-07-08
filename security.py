from models.user import UserModel
from hmac import compare_digest
# users = [
#UserModel(1, 'bob', 'abcxyz'),
#UserModel(2, 'user2', 'abcxyz'),
# ]

#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user

# identity is predefined method of Flask jwt
# safe_str_cmp compares two strings


def identity(payload):
    user_id = payload['identity']
   # return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)
