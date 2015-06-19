from setuptools import setup, find_packages

setup(
    name='jsonbfield',
    version='0.1.0',
    description='Django JSONB field',
    long_description='The Postgres 9.4 JSONB field support coming in Django 1.9'
                     ' extracted to a standalone module',
    author='Tome Cvitan',
    author_email='tome@cvitan.com',
    url='https://github.com/HearstCorp/django-jsonbfield',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Librares',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='django postgres jsonb',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'psycopg2>=2.5.4',
        'Django>=1.8'
    ]
)
