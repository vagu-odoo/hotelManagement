from odoo import models, fields

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
    
    is_booked = fields.Boolean()
    image = fields.Image()
    def action_set_room_book(self):
        for record in self:
           record.status = 'occupied' 
        return True

    def action_set_room_unbook(self):
        for record in self:
           record.status = 'available' 
        return True