import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="napari-minimal-plugin",
    version="0.1.0",
    author="Robert Haase",
    author_email="robert.haase@tu-dresden.de",
    description="A minimal napari plugin for demonstrating the plugin mechanism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haesleinhuepf/napari-minimal-plugin",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["scikit-image", "napari==0.4.3", "napari_plugin_engine", "magicgui==0.2.5", "numpy!=1.19.4"],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: napari",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
    ],
    entry_points={
        'napari.plugin': [
            'my_category = napari_minimal_plugin',
        ],
    },
)
