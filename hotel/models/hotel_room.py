from odoo import models, fields
from odoo.exceptions import UserError

class Room(models.Model):
    _name = 'hotel.room'
    _description = 'description for hotel room'
    
    room_number = fields.Integer(required=True)
    price = fields.Integer(required=True)
    max_adult = fields.Integer(default=2)
    max_child = fields.Integer(default=2)

    manager = fields.Many2one('res.users', 'Manager')
    room_type_id = fields.Many2one('hotel.room.type', 'Room Type', required=True)
    status = fields.Selection([('available', 'Available'),
                               ('occupied', 'Occupied')],
                              'Status', default='available')
    
    is_booked = fields.Boolean(string='Booked', compute='_compute_is_booked')
    image = fields.Image()

    def _compute_is_booked(self):
        for room in self:
            bookings = self.env['hotel.booking'].search([
                ('room_id', '=', room.id),
                ('booking_date', '=', fields.Date.today())
            ])
            room.is_booked = bool(bookings)
            
    def action_set_room_book(self):
        for record in self:
            if record.is_booked == False:
                record.status = 'occupied' 
            else:
                raise UserError('Room is not available for this date you can try on some other day or some other room')    
        return True

    def action_set_room_unbook(self):
        for record in self:
           record.status = 'available' 
        return True