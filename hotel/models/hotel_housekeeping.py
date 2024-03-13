from odoo import models, fields

class HousekeepingTask(models.Model):
    _name = 'hotel.housekeeping.task'
    _description = 'Housekeeping Task'

    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today())
    task = fields.Selection([('cleaning', 'Cleaning'), ('maintenance', 'Maintenance')], string='Task', required=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('pending', 'Pending')
    ], string='State', default='pending')
    room_number = fields.Integer(related="room_id.room_number", readonly=True)

    def action_start_task(self):
        for task in self:
            task.state = 'in_progress'

    def action_complete_task(self):
        for task in self:
            task.state = 'completed'