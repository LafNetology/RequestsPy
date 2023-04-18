from pprint import pprint

import requests

from ya_disk import YandexDisk

class YandexDisk():

    def __init__(self, token):
        self.token = token


    if __name__ == '__main__':

        ya = YandexDisk(token="")
        ya.upload_file_to_disk("Test/test.txt", "test.txt")

