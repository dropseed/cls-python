from .settings import settings as _settings
# These are the things we'll export for the client libraries
# (nothing beyond these should be counted on)
from .events import track_event, dispatch_events

set_project_key = _settings.set_project_key
set_project_slug = _settings.set_project_slug
set_request_permission_prompt = _settings.set_request_permission_prompt
set_debug = _settings.set_debug
set_noninteractive_tracking = _settings.set_noninteractive_tracking
set_user_id = _settings.set_user_id
set_invocation_id = _settings.set_invocation_id
