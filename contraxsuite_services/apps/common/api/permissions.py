"""
    Copyright (C) 2017, ContraxSuite, LLC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    You can also be released from the requirements of the license by purchasing
    a commercial license from ContraxSuite, LLC. Buying such a license is
    mandatory as soon as you develop commercial activities involving ContraxSuite
    software without disclosing the source code of your own applications.  These
    activities include: offering paid services to customers as an ASP or "cloud"
    provider, processing documents on the fly in a web application,
    or shipping ContraxSuite within a closed source product.
"""
# -*- coding: utf-8 -*-

# Third-party imports
from rest_framework.permissions import BasePermission, IsAuthenticated
from apps.task.utils.task_utils import check_blocks

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.6.0/LICENSE"
__version__ = "1.6.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class SuperuserRequiredPermission(BasePermission):
    """
    Allows access only to superusers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class ReviewerReadOnlyPermission(IsAuthenticated):
    """
    Gives read only access for reviewers - i.e. only GET request methods are allowed
    """
    def has_permission(self, request, view):
        res = super().has_permission(request, view)
        if not res:
            return res
        if request.user.is_reviewer and request.method != 'GET':
            return False
        return True


class ReviewerForbiddenPermission(IsAuthenticated):
    """
    Allows access only to superusers.
    """
    def has_permission(self, request, view):
        res = super().has_permission(request, view)
        if not res:
            return res
        return not request.user.is_reviewer


class AppBlockPermissions(BasePermission):

    def has_permission(self, request, view):
        # check for any app-wide blocks
        if request.method != 'GET':
            block_msg = check_blocks(raise_error=False, error_message='Unable to process request.')
            if block_msg is not False:
                self.message = block_msg
                return False
        return True
