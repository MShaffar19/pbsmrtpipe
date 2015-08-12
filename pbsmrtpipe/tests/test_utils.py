import os
import unittest
import logging

from pbsmrtpipe.utils import (which, HTML_TEMPLATE_ENV)
from base import TEST_DATA_DIR, SIV_TEST_DATA_DIR


log = logging.getLogger(__name__)


@unittest.skipIf(not os.path.exists(SIV_TEST_DATA_DIR), "Unable to find test {s}".format(s=SIV_TEST_DATA_DIR))
class TestUtils(unittest.TestCase):

    def test_which(self):
        exe = 'python'
        path = which(exe)
        self.assertIsNotNone(path)

    def test_bad_which(self):
        exe = 'pythonz'
        path = which(exe)
        self.assertIsNone(path)




class TestLoadJinjaTemplate(unittest.TestCase):

    def test_can_find_and_load_template(self):
        template_name = 'index.html'
        t = HTML_TEMPLATE_ENV.get_template(template_name)
        self.assertIsNotNone(t)

    @unittest.skip
    def test_render_index_html(self):
        template_name = 'index.html'
        t = HTML_TEMPLATE_ENV.get_template(template_name)
        self.assertIsNotNone(t)

        d = dict(value=1)
        html = t.render(**d)
        self.assertIsInstance(html, basestring)
