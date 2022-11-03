from app import db, app
from app.models import Category, Product
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')

class ProductView(ModelView):
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    can_view_details = True
    column_exclude_list = ['image']
    can_export = True
    column_export_list = ['id', 'name', 'description']
    column_labels = {
        'name': 'Sản phẩm',
        'description': 'Mô tả',
        'price': 'Giá'
    }
class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category, db.session, name = 'Danh mục'))
admin.add_view(ProductView(Product, db.session, name = 'Sản phẩm'))
admin.add_view(StatsView(name='Thống kê - báo cáo'))