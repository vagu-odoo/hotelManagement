from odoo import http,api
from odoo.http import request

class Hotel(http.Controller):
    @http.route(['/hotel', '/hotel/page/<int:page>'],auth='public', website=True)
    def index(self, **kwargs):
        page = int(kwargs.get('page', 1))   
        rooms = request.env['hotel.room'].search([],)
        total_rooms = len(rooms)
        pager = request.website.pager(
            url='/hotel',total = total_rooms,page=page,step=6
        )
        offset = pager['offset']
        # offset = (page - 1) * 6
        rooms = rooms[offset: offset + 6]
        print(rooms)
        return http.request.render('hotel.rooms_page_view',{
            'rooms':rooms,
            'pager':pager
        })
    
    

    @http.route('/hotel/<model("hotel.room"):room_details>/', auth='public', website=True)
    def room_details(self, room_details):
        return http.request.render('hotel.room_details_page_view', {
        'room': room_details
    })


    @http.route('/hotel/book_room/<model("hotel.room"):room_details>/', auth='public', website=True)
    def book_room(self, room_details):
        return http.request.render('hotel.booking_form', {
        'room': room_details
    })


    # @http.route('/confirm_booking', type='http', auth='public', website=True)
    # def confirm_booking(self, **kwargs):
    #     email = kwargs.get('email')
    #     phone = kwargs.get('phone')
    #     booking_date = kwargs.get('booking_date')
    #     room_id = int(kwargs.get('room_id'))
    #     room_type_id = int(kwargs.get('room_type_id'))

    #     # Create the booking record
    #     booking = request.env['hotel.booking'].create({
    #         'email': email,
    #         'phone': phone,
    #         'booking_date': booking_date,
    #         'room_id': room_id,
    #         'room_type_id': room_type_id,
    #     })

    #     return True

    @http.route('/confirm_booking', type='http', auth='public', website=True)
    def confirm_booking(self, **kwargs):
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        booking_date = kwargs.get('booking_date')
        room_id = int(kwargs.get('room_id'))

        room_type_id = kwargs.get('room_type_id')
        if room_type_id:
            room_type_id = int(room_type_id)
        
        data={
            'email': email,
            'phone': phone,
            'booking_date': booking_date,
            'room_id': room_id,
            'room_type_id': room_type_id,
            'status': 'confirmed'  # Assuming the booking is confirmed upon submission
    
        }

        # Create the booking record
        booking = request.env['hotel.booking'].create(data)

        return "Booking confirmed successfully"
   