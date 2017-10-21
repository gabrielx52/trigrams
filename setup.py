"""Setup file for trigrams package."""
from setuptools import setup


setup(
    name="trigrams",
    description="Python based story writer using trigrams.",
    author=["Cody Dibble", "Gabriel Meringolo"],
    author_email=["hcodydibble@gmail.com", "gabriel.meringolo@gmail.com"],
    license="MIT",
    py_modules=["trigrams"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
    }
)
