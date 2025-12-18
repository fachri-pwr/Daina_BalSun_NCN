# renderers.py

from rest_framework.renderers import JSONRenderer


class NDJSONRenderer(JSONRenderer):
    """
    Renderer that outputs Newline-Delimited JSON (NDJSON).
    Content-Type: application/x-ndjson
    """
    media_type = 'application/x-ndjson'
    format = 'ndjson'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b''

        # We assume data is a list (from a queryset)
        if isinstance(data, list):
            output = []
            for item in data:
                # Serialize each item individually
                json_line = super().render(
                    item,
                    accepted_media_type=accepted_media_type,
                    renderer_context=renderer_context
                )
                # Append the JSON line followed by the newline character (\n)
                output.append(json_line.decode('utf-8') + '\n')

            return ''.join(output).encode('utf-8')

        # Fallback for single objects or errors
        return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)