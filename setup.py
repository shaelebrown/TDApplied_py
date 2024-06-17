
from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Machine Learning and Inference for Topological Data Analysis'
LONG_DESCRIPTION = 'Topological data analysis is a powerful tool for finding non-linear global structure in whole datasets. The main tool of topological data analysis is persistent homology, which computes a topological shape descriptor of a dataset called a persistence diagram. \'TDApplied\' provides  useful and efficient methods for analyzing groups of persistence diagrams with machine learning and statistical inference, and these functions can also interface with other data science packages to form flexible and integrated topological data analysis pipelines.'

# Setting up
setup(
        name="TDApplied", 
        version=VERSION,
        author="Shael Brown",
        author_email="<shaelebrown@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        MAINTAINER = "Shael Brown",
        MAINTAINER_EMAIL = "shaelebrown@gmail.com",
        URL = "https://github.com/shaelebrown/TDApplied_py",
        LICENSE = "GNU AGPLv3",
        KEYWORDS = ["machine learning", "topological data analysis", "persistent homology", "persistence diagrams", "inference"],
        CLASSIFIERS = ["Intended Audience :: Science/Research",
               "Intended Audience :: Developers",
               "License :: OSI Approved",
               "Programming Language :: C++",
               "Programming Language :: Python",
               "Topic :: Software Development",
               "Topic :: Scientific/Engineering",
               "Operating System :: Microsoft :: Windows",
               "Operating System :: POSIX",
               "Operating System :: Unix",
               "Operating System :: MacOS",
               "Programming Language :: Python :: 3.7",
               "Programming Language :: Python :: 3.8",
               "Programming Language :: Python :: 3.9",
               "Programming Language :: Python :: 3.10",
               "Programming Language :: Python :: 3.11",
               "Programming Language :: Python :: 3.12"],
        INSTALL_REQUIRES = [],
        EXTRAS_REQUIRE = {"tests": ["pandas",
                                    "pytest",
                                    "pytest-cov",
                                    "pytest-azurepipelines",
                                    "pytest-benchmark",
                                    "jupyter_contrib_nbextensions",
                                    "flake8",
                                    "hypothesis"],
                          "doc": ["openml",
                                  "sphinx",
                                  "nbconvert",
                                  "sphinx-issues",
                                  "sphinx_rtd_theme",
                                  "numpydoc"],
                          "examples": ["jupyter",
                                       "pandas",
                                       "openml",
                                       "matplotlib",
                                       "gensim",
                                       "umap-learn"]}
)