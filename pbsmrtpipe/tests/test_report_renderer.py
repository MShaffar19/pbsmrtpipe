import os
import tempfile
import logging
import unittest

from base import TestDirBase as _TestBase, TEST_DATA_DIR
from base import _write_temp_file

import pbsmrtpipe.report_renderer as R

try:
    import pbreports.serializers as S
    HAS_PBREPORTS = True
except ImportError:
    HAS_PBREPORTS = False

log = logging.getLogger(__name__)


@unittest.skipIf(not HAS_PBREPORTS, "Pbreports is not installed.")
class TestRenderReportIndex(_TestBase):

    def test_01(self):
        name = "filter_reports_filter_stats.json"
        f = os.path.join(TEST_DATA_DIR, name)
        report = S.json_file_to_report(f)
        s = R.render_report(report)
        log.info(s)
        self.assertIsNotNone(s)
        _write_temp_file(self.temp_dir, s, suffix="index.html")


@unittest.skipIf(not HAS_PBREPORTS, "Pbreports is not installed.")
class TestCliReportRender(_TestBase):

    def test_01(self):
        name = "filter_reports_filter_stats.json"
        f = os.path.join(TEST_DATA_DIR, name)
        report = S.json_file_to_report(f)
        s = R.render_report(report)
        self.assertIsNotNone(s)

        for x in ('css', 'js'):
            p = os.path.join(self.temp_dir, x)
            if not os.path.exists(p):
                os.mkdir(p)
        html_output = os.path.join(self.temp_dir, 'report.html')
        rcode = R.write_report_with_html_extras(report, html_output, self.temp_dir)
        msg = "Failed writing {f}".format(f=html_output)
        self.assertEqual(rcode, 0, msg)
