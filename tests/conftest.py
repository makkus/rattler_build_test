#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest


import os
import tempfile
import uuid
from pathlib import Path

import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JOBS_FOLDERS = [
    Path(os.path.join(ROOT_DIR, "tests", "resources", "jobs")),
    Path(os.path.join(ROOT_DIR, "examples", "jobs")),
]


def create_temp_dir():
    session_id = str(uuid.uuid4())
    TEMP_DIR = Path(os.path.join(tempfile.gettempdir(), "kiara_tests"))

    instance_path = os.path.join(
        TEMP_DIR.resolve().absolute(), f"instance_{session_id}"
    )
    return instance_path

