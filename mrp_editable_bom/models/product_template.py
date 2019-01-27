# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP

class MEBProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_line_warn = fields.Selection(WARNING_MESSAGE, 'Purchase Order Line',
        help=WARNING_HELP, required=False, default="no-message")
