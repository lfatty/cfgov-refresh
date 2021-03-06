from jinja2 import contextfilter
from jinja2.ext import Extension

from core.templatetags.richtext import richtext_isempty
from core.templatetags.svg_icon import svg_icon
from core.utils import signed_redirect, slugify_unique, unsigned_redirect


class CoreExtension(Extension):
    def __init__(self, environment):
        super(CoreExtension, self).__init__(environment)
        self.environment.globals.update({
            'signed_redirect': signed_redirect,
            'svg_icon': svg_icon,
            'unsigned_redirect': unsigned_redirect,
        })

        self.environment.filters.update({
            'richtext_isempty': richtext_isempty,
            'slugify_unique': contextfilter(slugify_unique),
        })


filters = CoreExtension
