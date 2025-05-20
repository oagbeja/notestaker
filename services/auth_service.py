from models import auth_model

users = [{"username":'ade',"password":'123456'},{"username":'ade2',"password":'123456'}]


def login(user_item:auth_model.UserBody):
    result = next((user for user in users if user["username"] == user_item.name and  user["password"] == user_item.password), None)
    return {"result":result}