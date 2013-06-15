from blog.config.prod import *

try:
    from blog.config.mongo import *
except ImportError:
    pass

