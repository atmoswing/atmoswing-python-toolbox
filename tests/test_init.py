import tempfile

from atmoswing_toolbox.datasets import generic


def test_module_import():
    with tempfile.TemporaryDirectory() as tmp_dir:
        generic.Generic(directory=tmp_dir, var_name=None, ref_data=None)
