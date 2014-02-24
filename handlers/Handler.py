class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix, name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        return self.callback("start_", name);

    def end(self, name):
        return self.calllback("end_", name)

	# 为什么回调函数看起来这么费劲呢
    def sub(self, name):
        def substitution(match):
            result = self.callback("sub_", name, match)
            if result is None: result match.group(0)
            return result;
        return substitution
