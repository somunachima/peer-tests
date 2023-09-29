# import pytest
from lib.secret_diary import SecretDiary
from unittest.mock import Mock

# def test_lock_diary_not_share_contents():
#     diary = Diary("hello")
#     secret_diary = SecretDiary(diary)
#     assert secret_diary.locked == True

def test_lock_diary_not_share_contents():
    fake_diary = Mock()

    fake_diary.lock.return_value = True

    reading = SecretDiary(fake_diary)
    assert reading.locked == True


# def test_unlocked_diary_share_contents():
#     diary = Diary("hello")
#     secret_diary = SecretDiary(diary)
#     secret_diary.unlock()
#     assert secret_diary.locked == False

def test_unlocked_diary_share_contents():
    fake_diary = Mock()

    fake_diary.unlock.return_value = False
    
    reading = SecretDiary(fake_diary)
    reading.unlock()
    assert reading.locked == False

def test_relock_diary_not_share_contents():
    fake_diary = Mock()

    fake_diary.unlock.return_value = False

    reading = SecretDiary(fake_diary)
    reading.lock()
    assert reading.locked == True

