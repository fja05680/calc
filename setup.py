from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='calc',
    version='0.5.0',
    description='Calculator for evaluating math expressions.',
    author='Farrell Aultman',
    author_email='fja0568@gmail.com',
    url='https://github.com/fja05680/calc',
    packages=['calc'],
    include_package_data=True,
    license='MIT',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
