from distutils.core import setup
import os
from distutils.extension import Extension

'''
import hello
hello.system("ls")
hts_engine_python.system
from hts_engine_python import system
'''

def 讀(檔名):
    return open(os.path.join(os.path.dirname(__file__), 檔名)).read()

module1 = Extension('hello',
                    sources=['hts_engine_python.c', ],
#                     sources = ['bin/hts_engine.c','hts_engine_python/hts_engine.c',],
                    include_dirs=['include',],
                    library_dirs=['lib'],
                    )
setup(
    # 臺灣言語工具 tai5_uan5_gian5_gi2_kang1_ku7
    name='hts_engine_python',
#     packages=['hts_engine_python'],
    version='0.1.0',
    description='臺灣語言資訊系統（Toolkit for Languages in Taiwan）',
    long_description=讀('README'),
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='http://意傳.台灣/',
    download_url='https://github.com/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7',  # I'll explain this in a second
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
	        ext_modules=[module1],
)
