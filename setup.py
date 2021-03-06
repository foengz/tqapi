#from distutils.core import setup, Extension
from setuptools import setup, Extension
import numpy as np
import os

if hasattr(os, 'uname'):
    OSNAME = os.uname()[0]
else:
    OSNAME = 'Windows'

#if OSNAME == 'Darwin':
#    os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.9'
    
msgpack = ( 'msgpack',
    {
        'sources' : [
            "lib/msgpack/src/vrefbuffer.c",
            "lib/msgpack/src/unpack.c",
            "lib/msgpack/src/objectc.c",
            "lib/msgpack/src/zone.c",
            "lib/msgpack/src/version.c",
        ],

        'include_dirs' : [
            'lib/msgpack/include'
        ]
    })


sources = [
    "lib/snappy/snappy-stubs-internal.cc",
    "lib/snappy/snappy-c.cc",
    "lib/snappy/snappy-sinksource.cc",
    "lib/snappy/snappy.cc",
    "lib/myutils/filemapping.cpp",
    "lib/myutils/ipc_connection.cpp",
    "lib/myutils/ipc_common.cpp",
    "lib/myutils/misc.cpp",
    "lib/myutils/mprpc.cpp",
    "lib/myutils/unicode.cpp",
    "lib/myutils/csvparser.cpp",
    "lib/myutils/socket_connection.cpp",
    "lib/myutils/socketutils.cpp",
    "lib/myutils/loop/MessageLoop.cpp",
    "lib/myutils/loop/RunLoop.cpp",
    "lib/jsoncpp/src/json_reader.cpp",
    "lib/jsoncpp/src/json_value.cpp",
    "lib/jsoncpp/src/json_writer.cpp",

    "pyext/tqapi_tapi.cpp",
    "pyext/tqapi_dapi.cpp",
    "pyext/tqapi_py.cpp",
    "pyext/tqs_stralet.cpp",
    "c/api/impl_tquant_api.cpp",
    "c/tqs/rt/realtime.cpp",
    "c/tqs/bt/backtest.cpp",
    "c/tqs/bt/sim_context.cpp",
    "c/tqs/bt/sim_data.cpp",
    "c/tqs/bt/sim_trade.cpp",
    "c/tqs/stralet.cpp",
    "c/tqs/logger.cpp"
]

define_macros = [
    ('MAJOR_VERSION', '0'),
    ('MINOR_VERSION', '1')
]
    
include_dirs = [
    'lib',
    'lib/msgpack/include',
    'lib/jsoncpp/inc',
    'pyext',
    'c/api',
    'c/tqs',
    np.get_include()
]

if OSNAME=="Windows":
    libraries = ['msgpack', 'ws2_32']

elif OSNAME=="Linux":
    libraries = ['msgpack', 'rt']

else:
    libraries = ['msgpack', 'iconv']

module = Extension('tquant._tqapi',
                   define_macros = define_macros,
                   include_dirs  = include_dirs,
                   libraries     = libraries,
                   library_dirs  =  [],
                   sources       = sources)

if OSNAME == "Windows":
    module.extra_compile_args = ['/MT', '/DNOMINMAX']
    msgpack[1]['cflags'] = ['/MT']
else:
    module.extra_compile_args = ['--std=c++11' ]
    

#export MACOSX_DEPLOYMENT_TARGET=10.10

setup(packages = [ 'tquant' ],
      package_dir = { 'tquant' : 'pyext'},
      libraries = [ msgpack ],
      ext_modules = [module],
      name = 'tquant',
      version = '0.1.15',
      description="Acqusta quantitative trading tools",
      author = "Xu Tiezhu",
      author_email = 'xutiezhu@gmail.com',
      url = 'https://github.com/acqusta/tqapi'
)


