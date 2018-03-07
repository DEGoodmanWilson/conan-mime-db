#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools

class MimeDbConan(ConanFile):
    name = "mime-db"
    version = "1.33.0"
    url = "https://github.com/bincrafters/conan-mime-db"
    description = "Keep it short"
    license = "https://github.com/jshttp/mime-db/blob/master/LICENSE"
    exports_sources = ["db.json"]
    no_copy_source = True
    build_policy="missing"
        
    def source(self):
        tools.download("https://cdn.rawgit.com/jshttp/mime-db/v{0}/db.json".format(self.version), 'db.json')

    def package(self):
        self.copy(pattern="db.json", dst="res")