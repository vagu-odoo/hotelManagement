{
    'name': 'hotel',
    'depends':[
        'base',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data':[
        'security/ir.model.access.csv',
        'controller/hotel_controller_website_view.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_rooms_views.xml',
        'views/hotel_rooms_type_views.xml',
        'views/hotel_menu.xml',
    ]
}