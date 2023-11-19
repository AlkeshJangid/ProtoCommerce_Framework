import logging
import inspect

class GenerateLogs:
    @staticmethod
    def LogGen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        File = logging.FileHandler(r"F:\Testing Documents\Pycharm Practice\ParaBankFramework\Logs\LogFile.log")

        Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")

        File.setFormatter(Format)

        logger.addHandler(File)

        logger.setLevel(logging.INFO)

        return logger




