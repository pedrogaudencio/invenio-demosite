# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from invenio.base.i18n import _
from invenio.modules.deposit.types import EditableRecordDeposition
from .article import ArticleForm


class ArticleEditForm(ArticleForm):

    """."""

    #
    # Form configuration
    #
    _title = _('Edit article')
    _subtitle = _('Instructions: (i) Press "Save" to save your upload for '
                  'editing later, as many times you like. (ii) Upload or '
                  'remove  extra files in the bottom of the form. (iii) When '
                  'ready, press "Submit" to finalize your upload.')


class article_edit(EditableRecordDeposition):

    """."""

    name = _("Editable Article")
    name_plural = _("Editable Articles")
    group = _("Articles & Preprints")
    enabled = True
    editable = True
    draft_definitions = {
        '_default': ArticleForm,
        '_edit': ArticleEditForm,
    }

__all__ = ["article_edit"]
