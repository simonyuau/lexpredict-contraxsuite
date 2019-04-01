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

# Project imports
from apps.common.models import AppVar

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2018, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.2.0/LICENSE"
__version__ = "1.2.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"

DEPLOYMENT_TERMS_INITIALIZED = AppVar.set(
    'deployment_terms_initialized', False,
    'True if terms was loaded during first application startup')

DEPLOYMENT_COURTS_INITIALIZED = AppVar.set(
    'deployment_courts_initialized', False,
    'True if courts was loaded during first application startup')

DEPLOYMENT_GEOENTITIES_INITIALIZED = AppVar.set(
    'deployment_geoentities_initialized', False,
    'True if geo entities was loaded during first application startup')

DEPLOYMENT_DOCUMENT_DATA_INITIALIZED = AppVar.set(
    'deployment_document_data_initialized', False,
    'True if document data was loaded during first application startup')