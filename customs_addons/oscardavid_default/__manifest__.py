# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2018  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'oscardavid',
    'version': '11.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para Ovolatina',
    'author': 'jeo Software',
    'depends': [
        'stock',
        'account_invoicing',
        'purchase',
        'sale_management',

        # para la localizacion argentina
        'l10n_ar_account',
        'l10n_ar_afipws_fe',        # Factura Electrónica Argentina
        'l10n_ar_aeroo_einvoice',   # impresion de factura electronica aeroo
        'l10n_ar_account_vat_ledger_citi',
        'account_debt_management',  #
        'l10n_ar_aeroo_payment_group',  #
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}
