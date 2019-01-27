# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class MEBStockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_confirm_raw_move(self):
        for move in self:
            move.raw_material_production_id.action_assign()
    
class MEBMrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def action_assign(self):
        for production in self:
            dummy_bom_line = self.env.ref('mrp_editable_bom.mrp_bom_line_dummy')
            new_move = production.move_raw_ids.filtered(lambda x: x.state == 'draft')
            qty = production.product_qty - production.qty_produced
            for move in new_move:
                move.write({
                            'location_dest_id': move.product_id.property_stock_production.id,
                            'unit_factor': qty > 0.0 and move.product_uom_qty/qty or 0.0,
                            'procure_method': 'make_to_stock',
                            'name': production.name,
                            'origin': production.name,
                            'group_id': production.procurement_group_id and production.procurement_group_id.id or False,
                            'bom_line_id': dummy_bom_line and dummy_bom_line.id or False})
            new_move.action_confirm()
        return super(MEBMrpProduction, self).action_assign()
