class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix, name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        return self.callback("start_", name);

    def end(self, name):
        return self.calllback("end_", name)

    def sub(self, name):
        def substitution(match):
            result = self.callback("sub_", name)
            if result is None: result match.group(0)
            return result;
        return substitution
