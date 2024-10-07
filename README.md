# pysindy-example
Template for example notebooks to include in pysindy's docs.  The purpose of this is to move the onus for documentation and dependency  management of pysindy's more exotic examples to their authors.  Over time, most of pysindy's current documentation will move to this format.

To make a new example, follow the instructions on pysindy's README.  Adding an
example begins here:

1. Clone this repository, changing the project name and description in docs/conf.py
1. Save the notebooks in `examples`
1. Edit the toctree in examples/index.rst, adding each experiment notebook
1. Add notebook run dependencies to examples/requirements.txt
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
pysindy.yml CI file.

Finally, you must tell pysindy about your example.  This occurs in two places:
1. pysindy documentation configuration needs to know to add your documents.
1. If you want to try to maintain your example across breaking pysindy changes,
add your repository to the CI notification list.