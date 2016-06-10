from quark_runtime import *

import quark.reflect
import quark_ffi_signatures_md


class Box(object):
    def _init(self):
        self.contents = None

    def __init__(self, contents):
        self._init()

    def get(self):
        return _cast(None, lambda: T)

    def _getClass(self):
        return u"generics.constructors.Box<quark.Object>"

    def _getField(self, name):
        if ((name) == (u"contents")):
            return (self).contents

        return None

    def _setField(self, name, value):
        if ((name) == (u"contents")):
            (self).contents = _cast(value, lambda: T)


Box.generics_constructors_Box_quark_Object__ref = None