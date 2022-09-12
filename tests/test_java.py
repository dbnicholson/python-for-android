import pytest
import sys
from pythonforandroid.recipe import Recipe
from pythonforandroid.toolchain import ToolchainCL


@pytest.fixture(scope='session')
def storage_dir(tmp_path_factory):
    return tmp_path_factory.mktemp('storage')


@pytest.fixture
def src_dir(tmp_path):
    src_dir = tmp_path / 'src'
    src_dir.mkdir()
    return src_dir


@pytest.fixture
def test_options(storage_dir, src_dir):
    return [
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


@pytest.fixture
def unit_test_argv(test_options, monkeypatch):
    argv = ['toolchain.py', 'test'] + test_options
    monkeypatch.setattr(sys, 'argv', argv)


@pytest.fixture
def connected_test_argv(test_options, monkeypatch):
    argv = ['toolchain.py', 'connectedAndroidTest', '--enable-androidx'] + test_options
    monkeypatch.setattr(sys, 'argv', argv)


@pytest.fixture
def cleanup_recipes():
    yield
    if hasattr(Recipe, 'recipes'):
        del Recipe.recipes


def test_android_unit_tests(src_dir, unit_test_argv, cleanup_recipes):
    """Android unit tests"""
    entrypoint = src_dir / 'main.py'
    entrypoint.touch()
    ToolchainCL()


def test_android_instrumented_tests(src_dir, connected_test_argv, cleanup_recipes):
    """Android instrumented tests"""
    entrypoint = src_dir / 'main.py'
    entrypoint.touch()
    ToolchainCL()
