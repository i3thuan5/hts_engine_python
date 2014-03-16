from distutils.core import setup
import os
from distutils.extension import Extension

'''
import hts_engine_python
hts_engine_python.system("ls")
or
from hts_engine_python import system
'''

# read a file by filename
def 讀(檔名):
	return open(os.path.join(os.path.dirname(__file__), 檔名)).read()

# files
檔案 = ['hts_engine_python.c', 'src/bin/hts_engine.c', ]
library_path = 'src/lib'
for 檔名 in os.listdir(library_path):
	if 檔名.endswith('.c'):
		檔案.append(library_path + '/' + 檔名)

module = Extension('hts_engine_python',
	sources=檔案,
	include_dirs=['src/include', ],
	library_dirs=[library_path, ],
	)

setup(
	name='hts_engine_python',
	version='0.1.0',
	description='an extension for whose want to use hts engine by python 3',
	long_description=讀('README'),
	author='薛丞宏',
	author_email='ihcaoe@gmail.com',
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
		'Operating System :: POSIX :: Other',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Natural Language :: Chinese (Traditional)',
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Text Processing',
		'Topic :: Text Processing :: Linguistic',
		],
	ext_modules=[module],
)
