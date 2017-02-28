from setuptools import setup


setup(
    name='stonic',
    version='0.1.dev0',
    description='Stonic Deployment & Configuration Management Tool',
    url='http://stonic.io/',
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='devops configuration automation stonic ansible',
    packages=['stonic'],
    install_requires=['click'],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'stonic=stonic.bin.stonic:main',
        ],
    },
)
