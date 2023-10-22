class Sql_querry:
    def __init__(self, querry:str, user_id:str, user_password:str):
        self.__querry = querry
        self.__user_id = user_id
        self.user_password = user_password
        self.__host = "localhost"
        self.__database = "vocabulary"