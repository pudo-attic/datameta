from setuptools import setup, find_packages

setup(
    name='datameta',
    version='0.1.0',
    description="A meta search engine and archival service for open data.",
    long_description="",
    classifiers=[],
    keywords='data opendata repository metadata',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='https://github.com/pudo/datameta',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    zip_safe=False,
    install_requires=[
    ],
    tests_require=[],
    entry_points="""
    """,
)
