from odoo import Command,models

class Booking(models.Model):
    _inherit = "hotel.booking"

    def action_create_invoice(self):
        for room in self:
            # prop.env['account.move'].check_access_rights("create")
            # prop.env['account.move'].check_access_rule("create")
            print(" reached ".center(50, '='))
            self.env['account.move'].sudo().create({
                # 'partner_id':prop.buyer.id,
                'move_type':'out_invoice',
                'invoice_line_ids':[
                    Command.create({
                        'name':'6% of the room price',
                        'quantity':1,
                        'price_unit':0.06 * room.room_id.price,
                    }),
                    Command.create({
                        'name':'Additional Administrative Fees',
                        'quantity':1,
                        'price_unit':100,
                    }),
                    Command.create({
                        'name':'Room Charges',
                        'quantity':1,
                        'price_unit':room.room_id.price,
                    })
                    
                ],
            })
        return True