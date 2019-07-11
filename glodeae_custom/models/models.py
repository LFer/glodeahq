# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmation_date = fields.Datetime(string='Confirmation Date',
                                        readonly=False,
                                        index=True,
                                        help="Date on which the sales order is confirmed.",
                                        oldname="date_confirm",
                                        copy=False)


    @api.multi
    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))

        for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        self.write({
            'state': 'sale',
        })
        self._action_confirm()
        if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
            self.action_done()
        return True


# class StockMoveLine(models.Model):
#     _inherit = 'stock.move.line'
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         import ipdb;ipdb.set_trace()
#         pick = False
#         if 'picking_id' in vals_list[0]:
#             pick = self.env['stock.picking'].browse(vals_list[0]['picking_id'])
#         # vals_list['date'] pick.date
#         lines = super(StockMoveLine, self).create(vals_list)
#         if pick:
#             lines.date = pick.date
#
#         return lines

