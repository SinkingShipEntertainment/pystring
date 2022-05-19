name = "pystring"

version = "1.1.3"

authors = [
    "Sony Picture Imageworks"
]

description = \
    """
    Pystring is a collection of C++ functions which match the interface and behavior
    of python's string class methods using std::string. Implemented in C++, it does
    not require or make use of a python interpreter. It provides convenience and
    familiarity for common string operations not included in the standard C++ library.
    It's also useful in environments where both C++ and python are used.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.pystring"


# To build/release (since there is Makefile and CMakeLists)
# rez-build -i -b cmake
# rez-release -b cmake


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.PYSTRING_ROOT_DIR = "{root}"
    env.LIBRARY_PATH.append("{root}/lib")  # pystring is built as static lib, so LIBRARY_PATH
