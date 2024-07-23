from setuptools import setup, find_packages

setup(
    name='text_evaluator',
    version='0.5',
    packages=find_packages(),
    package_data={'text_evaluator': ['data/my_model.h5', 'data/data.json']},
    install_requires=[
        'tensorflow',
        'nltk'
    ],
    entry_points={
        'console_scripts': [
            'text_evaluator=text_evaluator:main',
        ],
    },
    author='_KroZen_',
    author_email='your.email@example.com',
    description='A text evaluation module using AI-TQA Basic',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/krozen-dev/AI_TextScan',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)