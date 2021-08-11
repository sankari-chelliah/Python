try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
'description': 'My Project',
'author': 'Sankari',
'url': 'URL to do it at.',
'download_url': 'Where to download it',
'author_email': 'ssssss.aaaaaa@gmail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['NAME'],
'scripts': [],
'name': 'projectname'
}

setup(**config)
