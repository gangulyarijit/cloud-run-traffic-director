# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
import sys
import subprocess
import urllib.request

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():
    request_args = request.get_json()
    print(request_args)
    cmd = "https://google.com"
    if request_args and 'command' in request_args:
        print("reading command", file=sys.stderr)
        cmd = request_args.get('command')
    else:
        print('using default command', file=sys.stderr)
    print("Curling with timeout to:", cmd, file=sys.stderr)
    contents = urllib.request.urlopen(cmd, timeout=5).read()
    return contents


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
