def test_imports():
    # Don't want these to change on accident
    from cls_client import (
        track_command,
        set_debug,
        set_project_key,
        set_project_slug,
        set_noninteractive_tracking_enabled,
        track_event,
        dispatch_events,
        set_request_permission_prompt,
        set_user_id,
        set_invocation_id,
        set_is_noninteractive,
    )
