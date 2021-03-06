# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import boto3
from botocore.vendored import requests
from botocore.exceptions import ClientError
from LabelBot import LabelBot
import unittest

# some version issue
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestLabelBot(unittest.TestCase):
    """
    Unittest of LabelBot.py
    """
    def setUp(self):
        self.lb = LabelBot(repo="harshp8l/mxnet-infrastructure",  apply_secret=True)

    def test_add_labels(self):
        with patch('LabelBot.requests.post') as mocked_post:
            mocked_post.return_value.status_code = 200
            self.lb.all_labels = ['sample_label', 'another_label', 'all_labels']
            self.assertTrue(self.lb.add_labels(issue_num=0, labels=['sample_label']))

    def test_remove_labels(self):
        with patch('LabelBot.requests.delete') as mocked_delete:
            mocked_delete.return_value.status_code = 200
            self.lb.all_labels = ['sample_label', 'another_label', 'all_labels']
            self.assertTrue(self.lb.remove_labels(issue_num=0, labels=['sample_label']))

    def test_update_labels(self):
        with patch('LabelBot.requests.put') as mocked_put:
            mocked_put.return_value.status_code = 200
            self.lb.all_labels = ['sample_label', 'another_label', 'all_labels']
            self.assertTrue(self.lb.update_labels(issue_num=0, labels=['sample_label']))


if __name__ == "__main__":
    unittest.main()
