from cls_client import track_command, set_debug, set_is_noninteractive


def test_track_command():
    set_debug(True)

    @track_command(dispatch=False)
    def test_function():
        pass

    test_function()
