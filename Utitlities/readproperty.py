import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('commonInfo','base_url')
    @staticmethod
    def get_firstname():
        return config.get('commonInfo','user_firstname')
    @staticmethod
    def get_lastname():
        return config.get('commonInfo','user_lastname')
    @staticmethod
    def set_password():
        return config.get('commonInfo','user_password')
    @staticmethod
    def set_email():
        return config.get("commonInfo","user_email")