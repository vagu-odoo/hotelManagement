from odoo import models,fields
from odoo.exceptions import UserError,ValidationError

class Booking(models.Model):
    _name = 'hotel.booking'
    _description = 'description for hotel booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    email = fields.Char(required=True)
    phone = fields.Char(required=True)
    booking_date = fields.Date(required=True)
    room_id = fields.Many2one('hotel.room', 'Room', required=True)
    room_type_id = fields.Many2one('hotel.room.type', 'Room Type', )
    status = fields.Selection([('pending', 'Pending'),
                               ('confirmed', 'Confirmed'),
                               ('cancelled', 'Cancelled')],
                              'Status', default='pending')
    customer = fields.Many2one('res.partner')
    room_number = fields.Integer(related="room_id.room_number")


    def action_confirm_booking(self):
        for record in self:
           record.status = 'confirmed' 
        return True


    def action_cancel_booking(self):
        for record in self:
           record.status = 'cancelled' 
        return True

    def create(self, vals):
        existing_booking = self.env['hotel.booking'].search([
            ('room_id', '=', vals.get('room_id')),
            ('booking_date', '=', vals.get('booking_date'))
        ])
        if existing_booking:
            raise ValidationError('Room is already booked for this date!')
        else:
            return super().create(vals)


