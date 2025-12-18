# data/utils.py
import math
import numbers

def _is_nan(x):
    try:
        return isinstance(x, float) and math.isnan(x)
    except Exception:
        return False

def sanitize_for_json(obj):
    """Recursively replace NaN/inf with None so JSON renderer won't crash."""
    if obj is None:
        return None
    # primitives
    if _is_nan(obj):
        return None
    if isinstance(obj, numbers.Number):
        # protect for +/-inf too
        try:
            if obj == float("inf") or obj == float("-inf"):
                return None
        except Exception:
            pass
        return obj
    if isinstance(obj, str) or isinstance(obj, bool):
        return obj
    # list/tuple
    if isinstance(obj, (list, tuple)):
        return [sanitize_for_json(x) for x in obj]
    # dict
    if isinstance(obj, dict):
        return {k: sanitize_for_json(v) for k, v in obj.items()}
    # fallback: return as-is
    return obj
