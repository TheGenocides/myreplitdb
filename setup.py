from setuptools import setup

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name='MyDB',
    author="kaylebetter",
    url="https://github.com/kaylebetter/myreplitdb",
    version='1.0',
    description='The most simplistic and easiest wrapper to use for replit\'s database system.',
    long_description=readme,
    packages=['myreplitdb'],
    include_package_data=True,
    license="MIT",
    project_urls={
        "Github": "https://github.com/PyTweet/PyTweet/",
        },
    keywords="myreplitdb",
    install_requires=[
        'replit',
        'db',
    ],
)