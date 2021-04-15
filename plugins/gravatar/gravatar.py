# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

"""
Gravatar plugin for Pelican
===========================

This plugin assigns the ``author_gravatar`` variable to the Gravatar URL and
makes the variable available within the article's context.
"""

import hashlib
import six

from pelican import signals


def add_gravatar(generator, metadata):
    #import pdb; pdb.set_trace()

    #first check email
    if 'email' not in metadata.keys()\
        and 'AUTHOR_EMAIL' in generator.settings.keys():
            metadata['email'] = generator.settings['AUTHOR_EMAIL']

    #then add gravatar url
    if 'email' in metadata.keys():
        email_bytes = six.b(metadata['email']).lower()
        gravatar_url = "https://www.gravatar.com/avatar/" + \
                        hashlib.md5(email_bytes).hexdigest()
        metadata["author_gravatar"] = gravatar_url


def register():
    signals.article_generator_context.connect(add_gravatar)
