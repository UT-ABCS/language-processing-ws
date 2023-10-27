# language-processing-ws
Using Cohere to analyze feedback from responses to a Google Form


# For this error:
<!-- kdunc@Kylans-MacBook-Pro language-processing-ws % python3.10 -m pip install fastavro
Collecting fastavro
  Downloading fastavro-1.8.4.tar.gz (971 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 971.4/971.4 kB 6.8 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: fastavro
  Building wheel for fastavro (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for fastavro (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [51 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.macosx-12-arm64-cpython-310
      creating build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_schema_common.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_schema_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_logical_writers_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/json_read.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/write.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_write_common.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_write_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/__init__.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_read_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/types.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/json_write.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_read_common.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_validate_common.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_logical_readers_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/utils.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/logical_writers.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/_validation_py.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/__main__.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/logical_readers.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/const.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/schema.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/read.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      copying fastavro/validation.py -> build/lib.macosx-12-arm64-cpython-310/fastavro
      creating build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/binary_decoder.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/__init__.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/binary_encoder.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/parser.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/symbols.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/json_encoder.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      copying fastavro/io/json_decoder.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/io
      creating build/lib.macosx-12-arm64-cpython-310/fastavro/repository
      copying fastavro/repository/__init__.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/repository
      copying fastavro/repository/flat_dict.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/repository
      copying fastavro/repository/base.py -> build/lib.macosx-12-arm64-cpython-310/fastavro/repository
      copying fastavro/py.typed -> build/lib.macosx-12-arm64-cpython-310/fastavro
      running build_ext
      Compiling fastavro/_read.pyx because it changed.
      [1/1] Cythonizing fastavro/_read.pyx
      building 'fastavro._read' extension
      creating build/temp.macosx-12-arm64-cpython-310
      creating build/temp.macosx-12-arm64-cpython-310/fastavro
      clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -I/opt/homebrew/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/include/python3.10 -c fastavro/_read.c -o build/temp.macosx-12-arm64-cpython-310/fastavro/_read.o
      xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
      error: command '/usr/bin/clang' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for fastavro
Failed to build fastavro
ERROR: Could not build wheels for fastavro, which is required to install pyproject.toml-based projects -->
# Run xcode-select --install
# https://developer.apple.com/forums/thread/673827