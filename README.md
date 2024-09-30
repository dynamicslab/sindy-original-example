# pysindy-example
Template for example notebooks to include in pysindy's docs.  To make a new
example, follow the instructions on pysindy's README.

To add a new set of examples:

1. Clone this repository, changing the project name and description in docs/conf.py
1. Save the notebooks in examples/
1. Add references to the toctree in examples/index.rst
1. Add notebook run dependencies to examples/requirements.txt.
1. Build the documentation and verify it builds without warning or error:
```
pip install -r requirements-docs.txt
sphinx-build -W docs/source docs/build
```
1. Add and commit build result

Other dependency methods, e.g. pyproject.toml, are acceptable.  You will need
to modify the appropriate CI step

There are two CI files: one to build the documentation, one to run the experiments
against new versions of pysindy.  If you do not plan on updating the example code,
its fine to leave the example dependent upon an old version of pysindy: delete the
pysindy.yml CI file, 