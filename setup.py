import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("entry_points.ini", "r") as fh:
    entry_points = fh.read()

with open("requirements.txt", "r") as fh:
    entry_points = fh.read()

# list of (destination, source_file) tuples
DATA_FILES = [
    # ('~/', ['scripts/.xsessionrc',]),
]

# list of (destination, source_dir) tuples
DATA_DIRS = [
    # ('share/monokrom/linuxcnc', 'linuxcnc/'),
]


def data_files_from_dirs(data_dirs):
    data_files = []
    for dest_dir, source_dir in data_dirs:
        dest_dir = os.path.expandvars(dest_dir)
        for root, dirs, files in os.walk(source_dir):
            root_files = [os.path.join(root, i) for i in files]
            dest = os.path.join(dest_dir, os.path.relpath(root, source_dir))
            data_files.append((dest, root_files))

    return data_files


data_files = [(os.path.expanduser(dest), src_list) for dest, src_list in DATA_FILES]
data_files.extend(data_files_from_dirs(DATA_DIRS))


setup(
    name="semiauto_sg",
    version="0.0.1",
    author="Chris Chatelain",
    author_email="chris.chatelain@digiex.ca",
    description="Surface grinder linuxcnc interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digiexchris/SurfaceGrinder-linuxcnc-ui",
    download_url="",
    packages=find_packages(),
    include_package_data=True,
    data_files=data_files,
    entry_points=entry_points,
    install_requires=[
        'numpy>=1.19.0',
        'qtsass',
        'qtpyvcp>=4.1.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
