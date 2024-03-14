name = "pystring"

version = "1.1.4"

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
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

uuid = "repository.pystring"

build_system = "cmake"


def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.PYSTRING_ROOT_DIR = "{root}"
    env.LIBRARY_PATH.append("{root}/lib")  # pystring is built as static lib, so LIBRARY_PATH
