import json

class MyBaseException(Exception):
    pass


class LevelException(MyBaseException):
    def __init__(self, actualLevel, limitLevel):
        self.actualLevel = actualLevel
        self.limitLevel = limitLevel
    def __str__(self) -> str:
        return f'Неправильный уровень доступа, уровень {self.actualLevel} должен быть больше {self.limitLevel}'


class AccessException(MyBaseException):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __str__(self) -> str:
        return f'Не надейден пользователь с именем {self.name} и id {self.id}'


class User:
    def __init__(self, name, id, levelAccess) -> None:
        self.name = name
        self.id = id
        self.levelAccess = levelAccess
    
    def __str__(self) -> str:
        return f'Имя:{self.name}, ID:{self.id}, уровень доступа:{self.levelAccess}'
    
    def __repr__(self) -> str:
        return f'User("{self.name}","{self.id}",{self.levelAccess})'
    
    def __eq__(self, __o: object) -> bool:
        return True if self.name == __o.name and self.id == __o.id else False


class Project:
    user: User = None
    levelAccess: int
    users: list
    def __init__(self, fileName) -> None:
        self.fileName = fileName
        self.users = self.loadUsers(self.fileName)

    def loadUsers(self, fileName):
        data = []
        res = []
        with open(fileName, "r") as f:
            data = json.load(f)
        for i in data:
            res.append(User(i["name"], i["id"], i["levelAccess"]))
        return res

    def login(self, name, id):
        uTmp = User(name, id, 0)
        user = None
        try:
            index = self.users.index(uTmp)
        except ValueError as e:
            raise AccessException(name, id)
        user = self.users[index]
        self.levelAccess = user.levelAccess

    def addUser(self, name, id, levelAccess):
        if self.levelAccess == None or self.levelAccess > levelAccess:
            raise LevelException(levelAccess, self.levelAccess)
        newUser = User(name, id, levelAccess)
        self.users.append(newUser)


if __name__=="__main__":
    p = Project("TesT_14/users.json")
    p.login("Petr","id003")
    print(f'Уровень доступа : {p.levelAccess}')
    p.addUser("P","id005", 7)
    print(p.users)
    p.addUser("V","id006",2)

