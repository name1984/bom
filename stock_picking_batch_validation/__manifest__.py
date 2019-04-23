# -*- coding: utf-8 -*-
# © 2017 Jérôme Guerriat
# © 2017 Niboo SPRL (https://www.niboo.be/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Picking - Batch Validation',
    'version': '10.0.1.0.0',
    'author': 'Niboo',
    'category': 'Warehouse',
    'summary': 'Allow batch validation on delivery orders ',
    'description': """
This module allows the user to do all the moves of a stock picking in one click
 """,
    'website': 'www.niboo.be',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
