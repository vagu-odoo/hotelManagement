from odoo import models, fields

class RoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'description for hotel room type'

    name = fields.Char(required=True)
    capacity = fields.Integer('Capacity', required=True)
  
    # rooms = fields.One2many('hotel.room', 'room_type_id', 'Rooms')
