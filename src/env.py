from os import path

BASE_PATH = path.dirname(__file__)
IMG_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'img'))
PDF_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'pdf'))
VIDEO_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'videos'))
SAMPLE_IMG_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'public', 'img'))
SAMPLE_PDF_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'public', 'pdf'))
SAMPLE_JSON_ROOT_PATH = path.abspath(path.join(BASE_PATH, '..', 'public', 'json'))
LOG_ROOT_PATH = path.abspath(path.join(BASE_PATH, 'log'))
DATABASE_ROOT_PATH = path.abspath(path.join(BASE_PATH, 'db'))
