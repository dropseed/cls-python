import os
from cls_client import track_command, set_debug, set_is_noninteractive
from cls_client.ffi import _cls_client_dir


def test_track_command():
    set_debug(True)

    @track_command(dispatch=False)
    def test_function():
        pass

    test_function()


def test_default_instance_path():
    tail = os.path.join("cls-python", "cls_client")  # should always point to the root package dir
    assert _cls_client_dir.endswith(tail)
