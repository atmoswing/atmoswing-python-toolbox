import tempfile

from atmoswing_toolbox.files.create.predictors import generic


def test_module_import():
    with tempfile.TemporaryDirectory() as tmp_dir:
        generic.Generic(directory=tmp_dir, var_name=None, ref_data=None)
