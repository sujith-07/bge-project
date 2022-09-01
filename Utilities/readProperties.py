import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/Sujith/OneDrive/Desktop/BGE_Test3/BGE_Project/Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','loginemail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password