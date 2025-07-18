from app.models.stores import Store

def get_stores(session) -> list[Store]:
    store_list = session.query(Store).all()
    session.commit()
    return store_list

# store paginated
def store_paginated(session, page=1, per_page=10):
    pagination = session.query(Store).paginate(page=page, per_page=per_page, error_out=False)
    return pagination  