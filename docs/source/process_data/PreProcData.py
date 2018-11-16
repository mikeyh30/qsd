#!/usr/bin/env python
from subprocess import call

class PreProcData:
    def upload_data(self):
        rc = call("./upload_data")

