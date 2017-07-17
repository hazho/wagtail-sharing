from setuptools import find_packages, setup


install_requires = [
    'Django>=1.8,<1.11',
    'wagtail>=1.8,<1.11',
]


testing_extras = [
    'coverage>=3.7.0',
    'flake8>=2.2.0',
    'mock>=1.0.0',
]


short_description = 'Easier sharing of Wagtail drafts'


setup(
    name='wagtail-sharing',
    url='https://github.com/cfpb/wagtail-sharing',
    author='CFPB',
    author_email='tech@cfpb.gov',
    license='CCO',
    version='0.5',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    description=short_description,
    long_description=open('README.rst').read(),
)
