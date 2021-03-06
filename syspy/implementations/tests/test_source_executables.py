import pytest
from mock import patch
from mock.mock import Mock

call = Mock()

from ..source_executables import remove_unwanted

with_unwanted_file = ['file1', '__pycache__', '__init__.py', 'file2', '.pytest_cache']
sources_only = ['file1', 'file2']
ignore_sources = ['__init__.py', '__pycache__', '.pytest_cache']


class TestRemoveUnwantedFiles:
	def test_removes_init_py(self):
		assert sources_only == remove_unwanted(with_unwanted_file, ignore_sources)

	def test_removes_nothing(self):
		assert sources_only == remove_unwanted(sources_only, ignore_sources)
