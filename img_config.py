from os import environ

NAME_USER = environ['USERNAME']
LANG_DEFAULT_USER = environ['LANG']

# Accuracy parameters
COMPARING_ACCURACY = 50
DEBUG = True

SEARCH_DIRECTORY = [
    {
        "dir": environ['HOME'] + '/images',
        "recursive": False
    }
]

DEBUG_DIR = [
    {
        "dir": './images_exit',
        "recursive": False,
    }
]

TYPE_IMAGES_SEARCH = ['.png', '.jpg', '.jpeg']

FORMAT_NAME_COMPRESS = ''