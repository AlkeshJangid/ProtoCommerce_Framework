import configparser

config = configparser.RawConfigParser()
config.read(r"F:\Testing Documents\Pycharm Practice\ParaBankFramework\Configuration\config.ini")

class ReadValue:

    @staticmethod
    def getName():
        Name = config.get('Data info', 'Name')
        return Name

    @staticmethod
    def getEmail():
        Email = config.get('Data info', 'Email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('Data info', 'Password')
        return Password

    @staticmethod
    def getDateOfBirth():
        DateOfBirth = config.get('Data info', 'DateOfBirth')
        return DateOfBirth

    @staticmethod
    def getURL():
        URL = config.get('Data info', 'URL')
        return URL

    @staticmethod
    def getLocation():
        Location = config.get('Data info', 'Location')
        return Location


