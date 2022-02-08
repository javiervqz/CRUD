from setuptools import setup


setup(
    name='pv',
    version='0.1',
    author = 'Javier Vazquez',
    author_email = 'javier@javiervqz.org',
    description = ('CRUD to practice the best way to deliver software professionally'),
    packages = ['clients'],
    package_dir = {'':'src'},
    py_modules=['pv'],
    install_requires=[
                    'Click',
                    ],
    entry_points='''
                   [console_scripts]
                   pv=pv:cli
                ''',
    )
