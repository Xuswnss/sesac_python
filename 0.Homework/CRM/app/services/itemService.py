from app.models.items import Item


def get_items(session,page =1, per_page=10):
    pagination = session.query(Item).paginate(page = page, per_page=per_page, error_out =False)
    return pagination