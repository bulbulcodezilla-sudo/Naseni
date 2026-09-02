# =========================================================
#  utils/test_data.py
#  Small helpers to generate random test values, so every test
#  run uses unique titles/file numbers instead of colliding
#  with data from previous runs.
# =========================================================

import random
import string


def _random_suffix(length=6):
    """e.g. 'K3F9QZ' - random uppercase letters + digits"""
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def random_title():
    return f"AutoTest Title {_random_suffix()}"


def random_file_number():
    return f"FN-{_random_suffix(8)}"


def random_keyword():
    return f"keyword-{_random_suffix(4).lower()}"


def random_directorate_name():
    return f"AutoTest Directorate {_random_suffix()}"
