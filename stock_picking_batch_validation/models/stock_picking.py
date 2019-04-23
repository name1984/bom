# -*- coding: utf-8 -*-
# © 2017 Jérôme Guerriat
# © 2017 Niboo SPRL (https://www.niboo.be/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def do_all(self):
        for picking in self:
            for pack_operation in picking.pack_operation_product_ids:
                pack_operation.qty_done = pack_operation.product_qty
