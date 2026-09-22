import configparser
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "Configuration", "config.ini")

config = configparser.RawConfigParser()
config.read(CONFIG_PATH)


class ReadConfig:
    @staticmethod
    def get_application_url():
        # Prefer an environment variable if Jenkins sets one (e.g. per-environment
        # target URL), falling back to the checked-in config.ini for local runs.
        return os.environ.get("AUT_BASE_URL", config.get('commonInfo', 'base_url'))

    @staticmethod
    def get_firstname():
        return config.get('commonInfo', 'user_firstname')

    @staticmethod
    def get_lastname():
        return config.get('commonInfo', 'user_lastname')

    @staticmethod
    def set_password():
        return os.environ.get("AUT_PASSWORD", config.get('commonInfo', 'user_password'))

    @staticmethod
    def set_email():
        return os.environ.get("AUT_EMAIL", config.get("commonInfo", "user_email"))
