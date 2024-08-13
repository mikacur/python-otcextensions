#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
Replace CSS Cluster node
"""

import openstack

openstack.enable_logging(True)
conn = openstack.connect()

cluster_name_or_id = '3b300b4e-2aa9-45c0-b898-a9e6fa319922'
node_id = '3b04c1ab-3887-4cb6-9796-d15619cec0f5'

cluster = conn.css.find_cluster(cluster_name_or_id)

conn.css.replace_cluster_node(cluster, node_id)
