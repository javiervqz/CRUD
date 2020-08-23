from setuptools import setup


setup(
    name='pv',
    version='0.1',
    author = 'Javier Vazquez',
    author_email = 'jvrvzqzp@gmail.com',
    description = ('CRUD to practice the best way to deliver software professionally'),
    py_modules=['pv'],
    install_requires=[
                    'Click',
                    ],
    entry_points='''
                   [console_scripts]
                   pv=pv:cli
                ''',
    )
