import pytest
import sys
from pythonforandroid.toolchain import ToolchainCL


@pytest.fixture(scope='session')
def storage_dir(tmp_path_factory):
    return tmp_path_factory.mktemp('storage')


def test_python_util(storage_dir, tmp_path, monkeypatch):
    src_dir = tmp_path / 'src'
    src_dir.mkdir()
    entrypoint = src_dir / 'main.py'
    entrypoint.touch()

    argv = [
        'toolchain.py',
        'test',
        '--package=org.example.Test',
        '--version=0.1',
        '--name=test',
        '--dist-name=test',
        f'--private={src_dir}',
        f'--storage-dir={storage_dir}',
        '--bootstrap=service_only',
        '--arch=x86_64',
        (
            '--blacklist-requirements='
            'libffi,openssl,sqlite3,genericndkbuild,setuptools,six,'
            'pyjnius,android'
        ),
    ]
    monkeypatch.setattr(sys, 'argv', argv)

    ToolchainCL()
