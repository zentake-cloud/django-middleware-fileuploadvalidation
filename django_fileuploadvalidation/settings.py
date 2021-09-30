from django_fileuploadvalidation.data import whitelists

from django.conf import settings

CLAMAV_USAGE = getattr(settings, "CLAMAV_USAGE", True)
DETECTOR_SENSITIVITY = getattr(settings, "DETECTOR_SENSITIVITY", 0.99)
FILE_SIZE_LIMIT = getattr(settings, "FILE_SIZE_LIMIT", 5000)
FILENAME_LENGTH_LIMIT = getattr(settings, "FILENAME_LENGTH_LIMIT", 100)
UPLOADLOGS_MODE = getattr(settings, "UPLOADLOGS_MODE", "blocked")
SANITIZATION_ACTIVATED = getattr(settings, "SANITIZATION_ACTIVATED", True)

whitelist_type = getattr(settings, "UPLOAD_MIME_TYPE_WHITELIST", None)
if whitelist_type == "AUDIO_ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__AUDIO_ALL
elif whitelist_type == "APPLICATION_ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__APPLICATION_ALL
elif whitelist_type == "IMAGE_ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__IMAGE_ALL
elif whitelist_type == "TEXT_ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__TEXT_ALL
elif whitelist_type == "VIDEO_ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__VIDEO_ALL
elif whitelist_type == "AUDIO_RESTRICTIVE":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__AUDIO_RESTRICTIVE
elif whitelist_type == "APPLICATION_RESTRICTIVE":
    UPLOAD_MIME_TYPE_WHITELIST = (
        whitelists.WHITELIST_MIME_TYPES__APPLICATION_RESTRICTIVE
    )
elif whitelist_type == "IMAGE_RESTRICTIVE":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__IMAGE_RESTRICTIVE
elif whitelist_type == "TEXT_RESTRICTIVE":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__TEXT_RESTRICTIVE
elif whitelist_type == "VIDEO_RESTRICTIVE":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__VIDEO_RESTRICTIVE
elif whitelist_type == "ALL":
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__ALL
elif whitelist_type == "CUSTOM":
    UPLOAD_MIME_TYPE_WHITELIST = getattr(settings, "CUSTOM_WHITELIST", None)
else:  # RESTRICTIVE or other
    UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__RESTRICTIVE
