from odoo import http
from odoo.http import request

class Hotel(http.Controller):
    @http.route(['/hotel'],auth='public', website=True)
    def index(self, **kwargs):
        page = int(kwargs.get('page', 1))   
        rooms = request.env['hotel.room'].search([],)
        total_rooms = len(rooms)
        pager = request.website.pager(
            url='/hotel',total = total_rooms,page=page,step=6
        )
        offset = pager['offset']
        rooms = rooms[offset: offset + 6]

        return http.request.render('hotel.rooms_page_view',{
            'rooms':rooms,
            'pager':pager
        })