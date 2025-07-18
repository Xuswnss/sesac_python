# 1. CRM 
````
CRM/
├── app/                            
│   ├── __init__.py                
│   ├── models/
│   │   └── import_csv.py
│   │   └── items.py
│   │   └── orderitems.py
│   │   └── orders.py
│   │   └── stores.py
│   │   └── users.py      
│   ├── services/                  
│   │   └── userService.py
│   │   └── orderitemsService.py
│   │   └── orderService.py
│   │   └── itemService.py
│   │   └── storeService.py
│   ├── routes/                    
│       └── userRoutes.py
│       └── storeRoutes.py
│                    
│                       
│
├── config.py                                                        
├── app.py                        
└── README.md                   

````

--- 

user-detail page
- users page에서 user_id 값 클릭
- http://makemyproject.net/crm/user_detail/0a497257-2b1a-4836-940f-7b95db952e61
- 주소 구성 /user_detail/user_id
- 고객 정보 (id)
- order_id -> orders.id
- purchased_date -> orders.order_at
- purchased location -> orders.store_id