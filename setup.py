from distutils.core import setup
import os
from distutils.extension import Extension

current_directory = os.path.dirname(__file__)


def read_file(filename):
    return open(os.path.join(current_directory, filename)).read()

sources = ['hts_engine_python.c']
library_path = os.path.join(current_directory, 'src', 'lib')
for filename in os.listdir(library_path):
    if filename.endswith('.c'):
        sources.append(os.path.join(library_path, filename))

module = Extension(
    'htsengine',
    sources=sources,
    include_dirs=[library_path, os.path.join(
        current_directory, 'src', 'include'), ],
    library_dirs=[library_path],
)

setup(
    name='htsengine',
    version='0.2.4',
    description='An extension for whose want to use hts engine by Python 3',
    long_description=read_file('README.md'),
    url='http://hts-engine.sourceforge.net/',
    download_url='https://github.com/sih4sing5hong5/hts_engine_python',
    keywords=[
        '語言合成',
        'Text to Speech',
        'TTS',
        'HTS',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    ext_modules=[module],
)
