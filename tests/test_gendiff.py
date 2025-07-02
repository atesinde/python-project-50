from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import file_parser


def test_generate_diff_json():
    data1 = file_parser('tests/test_data/file1.json')
    data2 = file_parser('tests/test_data/file2.json')
    assert generate_diff(data1, data2) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''


def test_generate_diff_yml():
    data1 = file_parser('tests/test_data/file1.yml')
    data2 = file_parser('tests/test_data/file2.yml')
    assert generate_diff(data1, data2) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
    data1 = file_parser('tests/test_data/file1.yaml')
    data2 = file_parser('tests/test_data/file2.yaml')
    assert generate_diff(data1, data2) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''