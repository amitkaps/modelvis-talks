from setuptools import setup

setup(
  name="modelvis",
  version="0.1.2",
  description="Visualising Machine Learning Model",
  license="MIT",
  install_requires=[
    'numpy',
    'pandas',
    'scikit-learn',
    'matplotlib'
  ],
  py_modules=['modelvis'],
  author="Amit Kapoor",
  author_email="amitkaps@gmail.com",
  platforms="any"
)