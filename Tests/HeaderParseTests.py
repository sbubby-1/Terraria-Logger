import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata

expectedHeaderFieldCount = 153


def initializeHeaderFieldsTests():
    success = True

    Metadata.initializeHeaderFields()

    if expectedHeaderFieldCount != 153:
        success = False

    for key, value in Metadata.headerFields.items():
        if (
            type(key) != str
            or "type" not in value
            or "isRelevant" not in value
            or type(value["type"]) != str
            or type(value["isRelevant"]) != bool
        ):
            success = False
    return success
