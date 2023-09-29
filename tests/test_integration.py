import pytest
from lib.secret_diary import SecretDiary
from lib.diary import Diary
from unittest.mock import Mock

# def test_error_when_trying_to_read_diary_locked():
#     diary = Mock("hello")
#     secret_diary = SecretDiary(diary)
#     with pytest.raises(Exception) as e:
#         secret_diary.read()
#     assert str(e.value) == "Go away!"

# def test_read_when_trying_to_read_diary_unlocked():
#     diary = Mock("hello")
#     diary.read.return_value = "hello"
#     secret_diary = SecretDiary(diary)
#     secret_diary.unlock()
#     assert secret_diary.read() == "hello"
#     diary.read.assert_called()

# def test_error_when_trying_to_read_diary_locked():
#     diary = Diary("hello")
#     secret_diary = SecretDiary(diary)
#     with pytest.raises(Exception) as e:
#         secret_diary.read()
#     assert str(e.value) == "Go away!"

# def test_read_when_trying_to_read_diary_unlocked():
#     diary = Diary("hello")
#     secret_diary = SecretDiary(diary)
#     secret_diary.unlock()
#     assert secret_diary.read() == "hello"

def test_error_when_trying_to_read_diary_locked():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

def test_read_when_trying_to_read_diary_unlocked():
    diary = Mock()
    diary.read.return_value = "hello"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "hello"
    diary.read.assert_called()