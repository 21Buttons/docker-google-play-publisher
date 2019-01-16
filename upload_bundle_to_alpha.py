#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Uploads an apk to the alpha track."""

import argparse
import sys
from apiclient import sample_tools
from oauth2client import client

TRACK = 'alpha'  # Can be 'alpha', beta', 'production' or 'rollout'

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('package_name',
                       help='The package name. Example: com.android.sample')
argparser.add_argument('bundle_file',
                       help='The path to the Bundle file to upload.')
argparser.add_argument('mapping_file',
                       help='The path to the mapping file to upload.')


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv,
        'androidpublisher',
        'v3',
        __doc__,
        __file__,
        parents=[argparser],
        scope='https://www.googleapis.com/auth/androidpublisher')

    # Process flags and read their values.
    package_name = flags.package_name
    bundle_file = flags.bundle_file
    mapping_file = flags.mapping_file

    try:
        edit_request = service.edits().insert(body={}, packageName=package_name)
        result = edit_request.execute()
        edit_id = result['id']

        bundle_response = service.edits().bundles().upload(
            editId=edit_id,
            packageName=package_name,
            media_body=bundle_file,
            media_mime_type='application/octet-stream').execute()

        version_code = bundle_response['versionCode']

        print('Version code %d has been uploaded' % version_code)

        service.edits().deobfuscationfiles().upload(
            packageName=package_name,
            editId=edit_id,
            apkVersionCode=version_code,
            deobfuscationFileType='proguard',
            media_body=mapping_file,
            media_mime_type='application/octet-stream').execute()

        print('Mapping for version code %d has been uploaded' % version_code)

        track_response = service.edits().tracks().update(
            editId=edit_id,
            track=TRACK,
            packageName=package_name,
            body={'releases': [{
                'versionCodes': [version_code],
                'status': 'completed',
            }]}).execute()

        print('Track %s is set with releases: %s' % (
        track_response['track'], str(track_response['releases'])))

        commit_request = service.edits().commit(editId=edit_id, packageName=package_name).execute()

        print('Edit "%s" has been committed' % (commit_request['id']))

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')


if __name__ == '__main__':
    main(sys.argv)
