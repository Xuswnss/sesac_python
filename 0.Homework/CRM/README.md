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

해야되는거 
- 페이징 오류 해결 (완료)
- 단골 손님 리스트(store-detail) (완료)
  - 해당 월별 단골(store-detail-by-month) (완료)
  - 매장 별 단골(store-detail) (완료)
- 가장많이 팔린 음료(완료)
- (item) 월별 매출액 그래프 (완료)
- (user-detail) 자주방문한 매장 top 5 (완료)
- (user-detail) 자주 주문한 상품 top 5 (완료)
- 헤더 제거하기 (완료)
- 검색기능 수정하기 (완료)

- css
- api/ render 구분하기
- 회원가입 폼만들기
- admin / user 따로 구분해서 만들기
- 상점등록, 상품 주문, 유저 생성 , 삭제 전부 구현하기
