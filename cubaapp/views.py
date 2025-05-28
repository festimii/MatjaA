from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import UploadExcelForm
from django.contrib           import messages
from .forms                   import UploadExcelForm
from .models import ExcelUploadLog, ExcelRecord
from .services.excel_importer import import_excel_from_file, logger
from django.shortcuts import redirect, render
from django.urls     import reverse
import logging


@login_required(login_url="/login_home")
def index(request):
    context = { "breadcrumb":{"title":"Default","parent":"Dashboard","child":"Default"},}
    return render(request,'index.html',context)


@login_required(login_url="/login_home")
def dashboard_02(request):
    context = { "breadcrumb":{"title":"E-Commerce","parent":"Dashboard","child":"E-Commerce"},}
    return render(request,"general/dashboard/dashboard-02.html",context)


@login_required(login_url="/login_home")
def dashboard_03(request):
    context = { "breadcrumb":{"title":"Online Course","parent":"Dashboard","child":"Online Course"},}
    return render(request,"general/dashboard/dashboard-03.html",context)


@login_required(login_url="/login_home")
def dashboard_04(request):
    context = { "breadcrumb":{"title":"Crypto","parent":"Dashboard","child":"Crypto"},}
    return render(request,"general/dashboard/dashboard-04.html",context)


@login_required(login_url="/login_home")
def dashboard_05(request):
    context = { "breadcrumb":{"title":"Social","parent":"Dashboard","child":"Social"},}
    return render(request,"general/dashboard/dashboard-05.html",context)


@login_required(login_url="/login_home")
def dashboard_06(request):
    context = { "breadcrumb":{"title":"NFT","parent":"Dashboard","child":"NFT"},}
    return render(request,"general/dashboard/dashboard-06.html",context)


@login_required(login_url="/login_home")
def dashboard_07(request):
    context = { "breadcrumb":{"title":"School Management","parent":"Dashboard","child":"School Management"},}
    return render(request,"general/dashboard/dashboard-07.html",context)


@login_required(login_url="/login_home")
def dashboard_08(request):
    context = { "breadcrumb":{"title":"POS","parent":"Dashboard","child":"POS"},}
    return render(request,"general/dashboard/dashboard-08.html",context)


@login_required(login_url="/login_home")
def dashboard_09(request):
    context = { "breadcrumb":{"title":"CRM","parent":"Dashboard","child":"CRM"},}
    return render(request,"general/dashboard/dashboard-09.html",context)


@login_required(login_url="/login_home")
def dashboard_10(request):
    context = { "breadcrumb":{"title":"Analytics","parent":"Dashboard","child":"Analytics"},}
    return render(request,"general/dashboard/dashboard-10.html",context)


@login_required(login_url="/login_home")
def dashboard_11(request):
    context = { "breadcrumb":{"title":"HR Dashboard","parent":"Dashboard","child":"HR Dashboard"},}
    return render(request,"general/dashboard/dashboard-11.html",context)


# #---------------Widgets

@login_required(login_url="/login_home")
def general_widget(request):
    context = { "breadcrumb":{"title":"General","parent":"Widgets", "child":"General"}}
    return render(request,"general/widget/general-widget.html",context)

@login_required(login_url="/login_home")
def chart_widget(request):
    context = { "breadcrumb":{"title":"Chart","parent":"Widgets", "child":"Chart"}}
    return render(request,"general/widget/chart-widget.html",context)


# #-----------------Layout
@login_required(login_url="/login_home")
def box_layout(request):
    context = {'layout':'box-layout', "breadcrumb":{"title":"Box Layout","parent":"Page Layout", "child":"Box Layout"}}
    return render(request,"general/page-layout/box-layout.html",context)

@login_required(login_url="/login_home")
def layout_rtl(request):
    context = {'layout':'rtl', "breadcrumb":{"title":"RTL Layout","parent":"Page Layout", "child":"RTL Layout"}}
    return render(request,"general/page-layout/layout-rtl.html",context)

@login_required(login_url="/login_home")
def layout_dark(request):
    context = {'layout':'dark-only', "breadcrumb":{"title":"Layout Dark","parent":"Page Layout", "child":"Layout Dark"}}
    return render(request,"general/page-layout/layout-dark.html",context)

@login_required(login_url="/login_home")
def hide_on_scroll(request):
    context = { "breadcrumb":{"title":"Hide Menu On Scroll","parent":"Page Layout", "child":"Hide Menu On Scroll"}}
    return render(request,"general/page-layout/hide-on-scroll.html",context)


@login_required(login_url="/login_home")
def footer_light(request):
    context = { "breadcrumb":{"title":"Footer Light","parent":"Page Layout", "child":"Footer Light"}}
    return render(request,"general/page-layout/footer-light.html",context)

@login_required(login_url="/login_home")
def footer_dark(request):
    context = { "breadcrumb":{"title":"Footer Dark","parent":"Page Layout", "child":"Footer Dark"}}
    return render(request,"general/page-layout/footer-dark.html",context)

@login_required(login_url="/login_home")
def footer_fixed(request):
    context = { "breadcrumb":{"title":"Footer Fixed","parent":"Page Layout", "child":"Footer Fixed"}}
    return render(request,"general/page-layout/footer-fixed.html",context)


#--------------------------------Applications---------------------------------

#---------------------Project
@login_required(login_url="/login_home")
def project_details(request):
    context = { "breadcrumb":{"title":"Project Details","parent":"Projects", "child":"Project Details"}}
    return render(request,"applications/projects/scope-project.html",context)


@login_required(login_url="/login_home")
def projects(request):
    context = { "breadcrumb":{"title":"Project List","parent":"Projects", "child":"Project List"}}
    return render(request,"applications/projects/project-list.html",context)

@login_required(login_url="/login_home")
def projectcreate(request):
    context = { "breadcrumb":{"title":"Project Create","parent":"Projects", "child":"Project Create"}}
    return render(request,"applications/projects/projectcreate.html",context)


#-------------------File Manager
@login_required(login_url="/login_home")
def file_manager(request):
    context = { "breadcrumb":{"title":"File Manager","parent":"Apps", "child":"File Manager"}}
    return render(request,"applications/file-manager/file-manager.html",context)

#------------------------Kanban Board
@login_required(login_url="/login_home")
def kanban(request):
    context = { "breadcrumb":{"title":"Kanban Board","parent":"Apps", "child":"Kanban Board"}}
    return render(request,"applications/kanban/kanban.html",context)


#------------------------ Ecommerce
@login_required(login_url="/login_home")
def add_products(request):
    context = { "breadcrumb":{"title":"Add Product","parent":"ECommerce", "child":"Add Product"}}
    return render(request,"applications/ecommerce/products/add-products.html",context)


@login_required(login_url="/login_home")
def product_grid(request):
    context = { "breadcrumb":{"title":"Product Grid","parent":"Ecommerce", "child":"Product Grid"}}
    return render(request,"applications/ecommerce/products/product-grid.html",context)


@login_required(login_url="/login_home")
def list_products(request):
    context = { "breadcrumb":{"title":"Product List","parent":"Ecommerce", "child":"Product List"}}
    return render(request,"applications/ecommerce/products/list-products.html",context)


@login_required(login_url="/login_home")
def product_details(request):
    context = { "breadcrumb":{"title":"Product Details","parent":"Ecommerce", "child":"Product Details"}}
    return render(request,"applications/ecommerce/products/product-details.html",context)




@login_required(login_url="/login_home")
def category(request):
    context = { "breadcrumb":{"title":"Category","parent":"Ecommerce", "child":"Category"}}
    return render(request,"applications/ecommerce/category.html",context)


@login_required(login_url="/login_home")
def seller_list(request):
    context = { "breadcrumb":{"title":"Seller List","parent":"Ecommerce", "child":"Seller List"}}
    return render(request,"applications/ecommerce/seller/seller-list.html",context)


@login_required(login_url="/login_home")
def seller_details(request):
    context = { "breadcrumb":{"title":"Seller Details","parent":"Ecommerce", "child":"Seller Details"}}
    return render(request,"applications/ecommerce/seller/seller-details.html",context)


@login_required(login_url="/login_home")
def order_history(request):
    context = { "breadcrumb":{"title":"Order History","parent":"Ecommerce", "child":"Order History"}}
    return render(request,"applications/ecommerce/orders/order-history.html",context)


@login_required(login_url="/login_home")
def order_details(request):
    context = { "breadcrumb":{"title":"Order Details","parent":"Ecommerce", "child":"Order Details"}}
    return render(request,"applications/ecommerce/orders/order-details.html",context)


@login_required(login_url="/login_home")
def invoice_1(request):
    return render(request,"applications/ecommerce/invoice-1.html")

@login_required(login_url="/login_home")
def invoice_2(request):
    return render(request,"applications/ecommerce/invoice-2.html")

@login_required(login_url="/login_home")
def invoice_3(request):
    return render(request,"applications/ecommerce/invoice-3.html")

@login_required(login_url="/login_home")
def invoice_4(request):
    return render(request,"applications/ecommerce/invoice-4.html")

@login_required(login_url="/login_home")
def invoice_5(request):
    return render(request,"applications/ecommerce/invoice-5.html")

@login_required(login_url="/login_home")
def invoice_6(request):
    context = { "breadcrumb":{"title":"Invoice","parent":"Ecommerce", "child":"Invoice"}}
    return render(request,"applications/ecommerce/invoice-template.html",context)

@login_required(login_url="/login_home")
def cart(request):
    context = { "breadcrumb":{"title":"Cart","parent":"Ecommerce", "child":"Cart"}}
    return render(request,"applications/ecommerce/cart.html",context)

@login_required(login_url="/login_home")
def list_wish(request):
    context = { "breadcrumb":{"title":"Wishlist","parent":"Ecommerce", "child":"Wishlist"}}
    return render(request,"applications/ecommerce/list-wish.html",context)

@login_required(login_url="/login_home")
def checkout(request):
    context = { "breadcrumb":{"title":"Checkout","parent":"Ecommerce", "child":"Checkout"}}
    return render(request,"applications/ecommerce/checkout.html",context)


#------------------------ Letter-Box
@login_required(login_url="/login_home")
def mail_box(request):
    context = { "breadcrumb":{"title":"Mail Box","parent":"Email", "child":"Mail Box"}}
    return render(request,"applications/mail-box/mail-box.html",context)


#--------------------------------chat
@login_required(login_url="/login_home")
def private_chat(request):
    context = { "breadcrumb":{"title":"Private Chat","parent":"Chat", "child":"Private Chat"}}
    return render(request,"applications/chat/private-chat.html",context)

@login_required(login_url="/login_home")
def group_chat(request):
    context = { "breadcrumb":{"title":"Group Chat","parent":"Chat", "child":"Group Chat"}}
    return render(request,"applications/chat/group-chat.html",context)



#---------------------------------user
@login_required(login_url="/login_home")
def user_profile(request):
    context = { "breadcrumb":{"title":"User Profile","parent":"Users", "child":"User Profile"}}
    return render(request,"applications/users/user-profile.html",context)

@login_required(login_url="/login_home")
def edit_profile(request):
    context = { "breadcrumb":{"title":"User Edit","parent":"Users", "child":"User Edit"}}
    return render(request,"applications/users/edit-profile.html",context)

@login_required(login_url="/login_home")
def user_cards(request):
    context = { "breadcrumb":{"title":"User Cards","parent":"Users", "child":"User Cards"}}
    return render(request,"applications/users/user-cards.html",context)



#------------------------bookmark
@login_required(login_url="/login_home")
def bookmark(request):
    context = { "breadcrumb":{"title":"Bookmarks","parent":"Apps", "child":"Bookmarks"}}
    return render(request,"applications/bookmark/bookmark.html",context)


#------------------------contacts
@login_required(login_url="/login_home")
def contacts(request):
    context = { "breadcrumb":{"title":"Contacts","parent":"Apps", "child":"Contacts"}}
    return render(request,"applications/contacts/contacts.html",context)


#------------------------task
@login_required(login_url="/login_home")
def task(request):
    context = { "breadcrumb":{"title":"Tasks","parent":"Apps", "child":"Tasks"}}
    return render(request,"applications/task/task.html",context)


#------------------------calendar
@login_required(login_url="/login_home")
def calendar_basic(request):
    context = { "breadcrumb":{"title":"Calender Basic","parent":"Apps", "child":"Calender Basic"}}
    return render(request,"applications/calendar/calendar-basic.html",context)


#------------------------social-app
@login_required(login_url="/login_home")
def social_app(request):
    context = { "breadcrumb":{"title":"Social App","parent":"Apps", "child":"Social App"}}
    return render(request,"applications/social-app/social-app.html",context)


#------------------------to-do
@login_required(login_url="/login_home")
def to_do(request):
    context = { "breadcrumb":{"title":"To-Do","parent":"Apps", "child":"To-Do"}}
    return render(request,"applications/to-do/to-do.html",context)


#------------------------search
@login_required(login_url="/login_home")
def search(request):
    context = { "breadcrumb":{"title":"Search Result","parent":"Search Pages", "child":"Search Result"}}
    return render(request,"applications/search/search.html",context)



#--------------------------------Forms & Table-----------------------------------------------
#--------------------------------Forms------------------------------------
#------------------------form-controls


@login_required(login_url="/login_home")
def form_validation(request):
    context = { "breadcrumb":{"title":"Validation Forms","parent":"Form Controls", "child":"Validation Forms"}}
    return render(request,"forms-table/forms/form-controls/form-validation.html",context)


@login_required(login_url="/login_home")
def base_input(request):
    context = { "breadcrumb":{"title":"Base Inputs","parent":"Form Controls", "child":"Base Inputs"}}
    return render(request,"forms-table/forms/form-controls/base-input.html",context)


@login_required(login_url="/login_home")
def radio_checkbox_control(request):
    context = { "breadcrumb":{"title":"Checkbox & Radio","parent":"Form Controls", "child":"Checkbox & Radio"}}
    return render(request,"forms-table/forms/form-controls/radio-checkbox-control.html",context)


@login_required(login_url="/login_home")
def input_group(request):
    context = { "breadcrumb":{"title":"Input Groups","parent":"Form Controls", "child":"Input Groups"}}
    return render(request,"forms-table/forms/form-controls/input-group.html",context)


@login_required(login_url="/login_home")
def input_mask(request):
    context = { "breadcrumb":{"title":"Input Mask","parent":"Form Controls", "child":"Input Mask"}}
    return render(request,"forms-table/forms/form-controls/input-mask.html",context)


@login_required(login_url="/login_home")
def megaoptions(request):
    context = { "breadcrumb":{"title":"Mega Options","parent":"Form Controls", "child":"Mega Options"}}
    return render(request,"forms-table/forms/form-controls/megaoptions.html",context)




#---------------------------form widgets

@login_required(login_url="/login_home")
def datepicker(request):
    context = { "breadcrumb":{"title":"Datepicker","parent":"Form Widgets", "child":"Datepicker"}}
    return render(request,"forms-table/forms/form-widgets/datepicker.html",context)


@login_required(login_url="/login_home")
def touchspin(request):
    context = { "breadcrumb":{"title":"Touchspin","parent":"Form Widgets", "child":"Touchspin"}}
    return render(request,'forms-table/forms/form-widgets/touchspin.html',context)


@login_required(login_url="/login_home")
def select2(request):
    context = { "breadcrumb":{"title":"Select2","parent":"Form Widgets", "child":"Select2"}}
    return render(request,'forms-table/forms/form-widgets/select2.html',context)


@login_required(login_url="/login_home")
def switch(request):
    context = { "breadcrumb":{"title":"Switch","parent":"Form Widgets", "child":"Switch"}}
    return render(request,'forms-table/forms/form-widgets/switch.html',context)


@login_required(login_url="/login_home")
def typeahead(request):
    context = { "breadcrumb":{"title":"Typeahead","parent":"Form Widgets", "child":"Typeahead"}}
    return render(request,'forms-table/forms/form-widgets/typeahead.html',context)


@login_required(login_url="/login_home")
def clipboard(request):
    context = { "breadcrumb":{"title":"Clipboard","parent":"Form Widgets", "child":"Clipboard"}}
    return render(request,'forms-table/forms/form-widgets/clipboard.html',context)


#-----------------------form layout

@login_required(login_url="/login_home")
def form_wizard_one(request):
    context = { "breadcrumb":{"title":"Form Wizard 1","parent":"Form Layout", "child":"Form Wizard 1"}}
    return render(request,'forms-table/forms/form-layout/form-wizard.html',context)


@login_required(login_url="/login_home")
def form_wizard_two(request):
    context = { "breadcrumb":{"title":"Form Wizard 2","parent":"Form Layout", "child":"Form Wizard 2"}}
    return render(request,'forms-table/forms/form-layout/form-wizard-two.html',context)


@login_required(login_url="/login_home")
def two_factor(request):
    context = { "breadcrumb":{"title":"Two Factor","parent":"Form Layout", "child":"Two Factor"}}
    return render(request,'forms-table/forms/form-layout/two-factor.html',context)



#----------------------------------------------------Table------------------------------------------
#------------------------bootstrap table

@login_required(login_url="/login_home")
def basic_table(request):
    context = { "breadcrumb":{"title":"Bootstrap Basic Tables","parent":"Bootstrap Tables", "child":"Bootstrap Basic Tables "}}
    return render(request,'forms-table/table/bootstrap-table/bootstrap-basic-table.html',context)


@login_required(login_url="/login_home")
def table_components(request):
    context = { "breadcrumb":{"title":"Table Components","parent":"Bootstrap Tables", "child":"Table Components"}}
    return render(request,'forms-table/table/bootstrap-table/table-components.html',context)


#------------------------data table

@login_required(login_url="/login_home")
def datatable_basic_init(request):
    context = { "breadcrumb":{"title":"Basic DataTables","parent":"Data Tables", "child":"Basic DataTables"}}
    return render(request,'forms-table/table/data-table/datatable-basic-init.html',context)


@login_required(login_url="/login_home")
def datatable_advance(request):
    context = { "breadcrumb":{"title":"Advance Init","parent":"Data Tables", "child":"Advance Init"}}
    return render(request,'forms-table/table/data-table/datatable-advance.html',context)


@login_required(login_url="/login_home")
def datatable_API(request):
    context = { "breadcrumb":{"title":"API DataTables","parent":"Data Tables", "child":"API DataTables"}}
    return render(request,'forms-table/table/data-table/datatable-API.html',context)


@login_required(login_url="/login_home")
def datatable_data_source(request):
    context = { "breadcrumb":{"title":"DATA Source DataTables","parent":"Data Tables", "child":"DATA Source DataTables"}}
    return render(request,'forms-table/table/data-table/datatable-data-source.html',context)


#-------------------------------EX.data-table

@login_required(login_url="/login_home")
def ext_autofill(request):
    context = { "breadcrumb":{"title":"Autofill Datatables","parent":"Extension Data Tables", "child":"Autofill Datatables"}}
    return render(request,'forms-table/table/Ex-data-table/datatable-ext-autofill.html',context)


#--------------------------------jsgrid_table

@login_required(login_url="/login_home")
def jsgrid_table(request):
    context = { "breadcrumb":{"title":"JS Grid Tables","parent":"Tables", "child":"JS Grid Tables"}}
    return render(request,'forms-table/table/js-grid-table/jsgrid-table.html',context)




#------------------Components------UI Components-----Elements ----------->

#-----------------------------Ui kits

@login_required(login_url="/login_home")
def typography(request):
    context = { "breadcrumb":{"title":"Typography","parent":"Ui Kits", "child":"Typography"}}
    return render(request,'components/ui-kits/typography.html', context)


@login_required(login_url="/login_home")
def avatars(request):
    context = { "breadcrumb":{"title":"Avatars","parent":"Ui Kits", "child":"Avatars"}}
    return render(request,'components/ui-kits/avatars.html', context)


@login_required(login_url="/login_home")
def divider(request):
    context = { "breadcrumb":{"title":"Divider","parent":"Ui Kits", "child":"Divider"}}
    return render(request,'components/ui-kits/divider.html', context)


@login_required(login_url="/login_home")
def helper_classes(request):
    context = { "breadcrumb":{"title":"Helper Classes","parent":"Ui Kits", "child":"Helper Classes"}}
    return render(request,'components/ui-kits/helper-classes.html', context)


@login_required(login_url="/login_home")
def grid(request):
    context = { "breadcrumb":{"title":"Grid","parent":"Ui Kits", "child":"Grid"}}
    return render(request,'components/ui-kits/grid.html', context)


@login_required(login_url="/login_home")
def tagpills(request):
    context = { "breadcrumb":{"title":"Tag & Pills","parent":"Ui Kits", "child":"Tag & Pills"}}
    return render(request,'components/ui-kits/tag-pills.html', context)


@login_required(login_url="/login_home")
def progressbar(request):
    context = { "breadcrumb":{"title":"Progress","parent":"Ui Kits", "child":"Progress"}}
    return render(request,'components/ui-kits/progress-bar.html', context)


@login_required(login_url="/login_home")
def modal(request):
    context = { "breadcrumb":{"title":"Modal","parent":"Ui Kits", "child":"Modal"}}
    return render(request,'components/ui-kits/modal.html', context)


@login_required(login_url="/login_home")
def alert(request):
    context = { "breadcrumb":{"title":"Alerts","parent":"Ui Kits", "child":"Alerts"}}
    return render(request,'components/ui-kits/alert.html', context)


@login_required(login_url="/login_home")
def popover(request):
    context = { "breadcrumb":{"title":"Popover","parent":"Ui Kits", "child":"Popover"}}
    return render(request,'components/ui-kits/popover.html', context)


@login_required(login_url="/login_home")
def placeholder(request):
    context = { "breadcrumb":{"title":"Placeholders","parent":"Ui Kits", "child":"Placeholders"}}
    return render(request,'components/ui-kits/placeholders.html', context)


@login_required(login_url="/login_home")
def tooltip(request):
    context = { "breadcrumb":{"title":"Tooltip","parent":"Ui Kits", "child":"Tooltip"}}
    return render(request,'components/ui-kits/tooltip.html', context)


@login_required(login_url="/login_home")
def dropdown(request):
    context = { "breadcrumb":{"title":"Dropdowns","parent":"Ui Kits", "child":"Dropdowns"}}
    return render(request,'components/ui-kits/dropdown.html', context)


@login_required(login_url="/login_home")
def accordion(request):
    context = { "breadcrumb":{"title":"Accordions","parent":"Ui Kits", "child":"Accordions"}}
    return render(request,'components/ui-kits/according.html', context)


@login_required(login_url="/login_home")
def bootstraptab(request):
    context = { "breadcrumb":{"title":"Bootstrap Tabs","parent":"Ui Kits", "child":"Bootstrap Tabs"}}
    return render(request,'components/ui-kits/tab-bootstrap.html', context)


@login_required(login_url="/login_home")
def offcanvas(request):
    context = {"breadcrumb":{"title":"Offcanvas","parent":"Ui Kits", "child":"Offcanvas"}}
    return render(request,'components/ui-kits/offcanvas.html', context)


@login_required(login_url="/login_home")
def navigate_links(request):
    context = {"breadcrumb":{"title":"Navigate Links","parent":"Ui Kits", "child":"Navigate Links"}}
    return render(request,'components/ui-kits/navigate-links.html', context)


@login_required(login_url="/login_home")
def lists(request):
    context = {"breadcrumb":{"title":"Lists","parent":"Ui Kits", "child":"Lists"}}
    return render(request,'components/ui-kits/list.html', context)



#-------------------------------Bonus Ui

@login_required(login_url="/login_home")
def scrollable(request):
    context = {"breadcrumb":{"title":"Scrollable","parent":"Bonus Ui", "child":"Scrollable"}}
    return render(request,'components/bonus-ui/scrollable.html', context)


@login_required(login_url="/login_home")
def tree(request):
    context = {"breadcrumb":{"title":"Tree View","parent":"Bonus Ui", "child":"Tree View"}}
    return render(request,'components/bonus-ui/tree.html', context)


@login_required(login_url="/login_home")
def toasts(request):
    context = {"breadcrumb":{"title":"Toasts","parent":"Bonus Ui", "child":"Toasts"}}
    return render(request,'components/bonus-ui/toasts.html', context)


@login_required(login_url="/login_home")
def blockUi(request):
    context = {"breadcrumb":{"title":"Block Ui","parent":"Bonus Ui", "child":"Block Ui"}}
    return render(request,'components/bonus-ui/block-ui.html', context)


@login_required(login_url="/login_home")
def rating(request):
    context = {"breadcrumb":{"title":"Rating","parent":"Bonus Ui", "child":"Rating"}}
    return render(request,'components/bonus-ui/rating.html', context)


@login_required(login_url="/login_home")
def dropzone(request):
    context = {"breadcrumb":{"title":"Dropzone","parent":"Bonus Ui", "child":"Dropzone"}}
    return render(request,'components/bonus-ui/dropzone.html', context)


@login_required(login_url="/login_home")
def tour(request):
    context = {"breadcrumb":{"title":"Tour","parent":"Bonus Ui", "child":"Tour"}}
    return render(request,'components/bonus-ui/tour.html', context)


@login_required(login_url="/login_home")
def sweetalert2(request):
    context = {"breadcrumb":{"title":"Sweet Alert","parent":"Bonus Ui", "child":"Sweet Alert"}}
    return render(request,'components/bonus-ui/sweet-alert2.html', context)


@login_required(login_url="/login_home")
def animatedmodal(request):
    context = {"breadcrumb":{"title":"Animated Modal","parent":"Bonus Ui", "child":"Animated Modal"}}
    return render(request,'components/bonus-ui/modal-animated.html', context)


@login_required(login_url="/login_home")
def owlcarousel(request):
    context = {"breadcrumb":{"title":"Owl Carousel","parent":"Bonus Ui", "child":"Owl Carousel"}}
    return render(request,'components/bonus-ui/owl-carousel.html', context)


@login_required(login_url="/login_home")
def ribbons(request):
    context = {"breadcrumb":{"title":"Ribbons","parent":"Bonus Ui", "child":"Ribbons"}}
    return render(request,'components/bonus-ui/ribbons.html', context)



@login_required(login_url="/login_home")
def pagination(request):
    context = {"breadcrumb":{"title":"Paginations","parent":"Bonus Ui", "child":"Paginations"}}
    return render(request,'components/bonus-ui/pagination.html', context)


@login_required(login_url="/login_home")
def scrollspy(request):
    context = {"breadcrumb":{"title":"ScrollSpy","parent":"Bonus Ui", "child":"ScrollSpy"}}
    return render(request,'components/bonus-ui/scrollspy.html', context)


@login_required(login_url="/login_home")
def breadcrumb(request):
    context = {"breadcrumb":{"title":"Breadcrumb","parent":"Bonus Ui", "child":"Breadcrumb"}}
    return render(request,'components/bonus-ui/breadcrumb.html', context)


@login_required(login_url="/login_home")
def rangeslider(request):
    context = {"breadcrumb":{"title":"Range Slider","parent":"Bonus Ui", "child":"Range Slider"}}
    return render(request,'components/bonus-ui/range-slider.html', context)


@login_required(login_url="/login_home")
def ratios(request):
    context = {"breadcrumb":{"title":"Ratios","parent":"Bonus Ui", "child":"Ratios"}}
    return render(request,'components/bonus-ui/ratios.html', context)


@login_required(login_url="/login_home")
def imagecropper(request):
    context = {"breadcrumb":{"title":"Image Cropper","parent":"Bonus Ui", "child":"Image Cropper"}}
    return render(request,'components/bonus-ui/image-cropper.html', context)


@login_required(login_url="/login_home")
def basiccard(request):
    context = {"breadcrumb":{"title":"Basic Card","parent":"Bonus Ui", "child":"Basic Card"}}
    return render(request,'components/bonus-ui/basic-card.html', context)


@login_required(login_url="/login_home")
def creativecard(request):
    context = {"breadcrumb":{"title":"Creative Card","parent":"Bonus Ui", "child":"Creative Card"}}
    return render(request,'components/bonus-ui/creative-card.html', context)


@login_required(login_url="/login_home")
def draggablecard(request):
    context = {"breadcrumb":{"title":"Draggabble Card","parent":"Bonus Ui", "child":"Draggabble Card"}}
    return render(request,'components/bonus-ui/draggable-card.html', context)


@login_required(login_url="/login_home")
def timeline(request):
    context = {"breadcrumb":{"title":"Timeline","parent":"Bonus Ui", "child":"Timeline"}}
    return render(request,'components/bonus-ui/timeline-v-1.html', context)


#---------------------------------Animation


@login_required(login_url="/login_home")
def animate(request):
    context = {"breadcrumb":{"title":"Animate","parent":"Animation", "child":"Animate"}}
    return render(request,'components/animation/animate.html', context)


@login_required(login_url="/login_home")
def scrollreval(request):
    context = {"breadcrumb":{"title":"Scroll Reveal","parent":"Animation", "child":"Scroll Reveal"}}
    return render(request,'components/animation/scroll-reval.html', context)


@login_required(login_url="/login_home")
def AOS(request):
    context = {"breadcrumb":{"title":"AOS Animation","parent":"Animation", "child":"AOS Animation"}}
    return render(request,'components/animation/AOS.html', context)


@login_required(login_url="/login_home")
def tilt(request):
    context = {"breadcrumb":{"title":"Tilt Animation","parent":"Animation", "child":"Tilt Animation"}}
    return render(request,'components/animation/tilt.html', context)


@login_required(login_url="/login_home")
def wow(request):
    context = {"breadcrumb":{"title":"Wow Animation","parent":"Animation", "child":"Wow Animation"}}
    return render(request,'components/animation/wow.html', context)


@login_required(login_url="/login_home")
def flashicon(request):
    context = {"breadcrumb":{"title":"Flash Icons","parent":"Animation", "child":"Flash Icons"}}
    return render(request,'components/icons/flash-icon.html', context)



#--------------------------Icons

@login_required(login_url="/login_home")
def flagicon(request):
    context = {"breadcrumb":{"title":"Flag Icons","parent":"Icons", "child":"Flag Icons"}}
    return render(request,'components/icons/flag-icon.html', context)


@login_required(login_url="/login_home")
def fontawesome(request):
    context = {"breadcrumb":{"title":"Font Awesome Icon","parent":"Icons", "child":"Font Awesome Icon"}}
    return render(request,'components/icons/font-awesome.html', context)


@login_required(login_url="/login_home")
def icoicon(request):
    context = {"breadcrumb":{"title":"Ico Icon","parent":"Icons", "child":"Ico Icon"}}
    return render(request,'components/icons/ico-icon.html', context)


@login_required(login_url="/login_home")
def themify(request):
    context = {"breadcrumb":{"title":"Themify Icon","parent":"Icons", "child":"Themify Icon"}}
    return render(request,'components/icons/themify-icon.html', context)


@login_required(login_url="/login_home")
def feather(request):
    context = {"breadcrumb":{"title":"Feather Icons","parent":"Icons", "child":"Feather Icons"}}
    return render(request,'components/icons/feather-icon.html', context)


@login_required(login_url="/login_home")
def whether(request):
    context = {"breadcrumb":{"title":"Whether Icon","parent":"Icons", "child":"Whether Icon"}}
    return render(request,'components/icons/whether-icon.html', context)


#--------------------------------Buttons

@login_required(login_url="/login_home")
def buttons(request):
    context = {"breadcrumb":{"title":"Buttons","parent":"Buttons", "child":"Buttons"}}
    return render(request,'components/buttons/buttons.html', context)



#-------------------------------Charts

@login_required(login_url="/login_home")
def apex(request):
    context = {"breadcrumb":{"title":"Apex Chart","parent":"Charts", "child":"Apex Chart"}}
    return render(request,'components/charts/chart-apex.html', context)


@login_required(login_url="/login_home")
def google(request):
    context = {"breadcrumb":{"title":"Google Chart","parent":"Charts", "child":"Google Chart"}}
    return render(request,'components/charts/chart-google.html', context)


@login_required(login_url="/login_home")
def sparkline(request):
    context = {"breadcrumb":{"title":"Sparkline Chart","parent":"Charts", "child":"Sparkline Chart"}}
    return render(request,'components/charts/chart-sparkline.html', context)


@login_required(login_url="/login_home")
def flot(request):
    context = {"breadcrumb":{"title":"Flot Chart","parent":"Charts", "child":"Flot Chart"}}
    return render(request,'components/charts/chart-flot.html', context)


@login_required(login_url="/login_home")
def knob(request):
    context = {"breadcrumb":{"title":"Knob Chart","parent":"Charts", "child":"Knob Chart"}}
    return render(request,'components/charts/chart-knob.html', context)


@login_required(login_url="/login_home")
def morris(request):
    context = {"breadcrumb":{"title":"Morris Chart","parent":"Charts", "child":"Morris Chart"}}
    return render(request,'components/charts/chart-morris.html', context)


@login_required(login_url="/login_home")
def chartjs(request):
    context = {"breadcrumb":{"title":"ChartJS Chart","parent":"Charts", "child":"ChartJS Chart"}}
    return render(request,'components/charts/chartjs.html', context)


@login_required(login_url="/login_home")
def chartist(request):
    context = {"breadcrumb":{"title":"Chartist Chart","parent":"Charts", "child":"Chartist Chart"}}
    return render(request,'components/charts/chartist.html', context)


@login_required(login_url="/login_home")
def peity(request):
    context = {"breadcrumb":{"title":"Peity Chart","parent":"Charts", "child":"Peity Chart"}}
    return render(request,'components/charts/chart-peity.html', context)



#------------------------------------------Pages-------------------------------------

#-------------------------sample-page

@login_required(login_url="/login_home")
def sample_page(request):
    context = {"breadcrumb":{"title":"Sample Page","parent":"Pages", "child":"Sample Page"}}
    return render(request,'pages/sample-page/sample-page.html',context)

#--------------------------internationalization

@login_required(login_url="/login_home")
def internationalization(request):
    context = {"breadcrumb":{"title":"Internationalization","parent":"Pages", "child":"Internationalization"}}
    return render(request,'pages/internationalization/internationalization.html',context)




# ------------------------------error page

@login_required(login_url="/login_home")
def error_400(request):
    return render(request,'pages/error-pages/error-400.html')


@login_required(login_url="/login_home")
def error_401(request):
    return render(request,'pages/error-pages/error-401.html')


@login_required(login_url="/login_home")
def error_403(request):
    return render(request,'pages/error-pages/error-403.html')


@login_required(login_url="/login_home")
def error_404(request):
    return render(request,'pages/error-pages/error-404.html')


@login_required(login_url="/login_home")
def error_500(request):
    return render(request,'pages/error-pages/error-500.html')


@login_required(login_url="/login_home")
def error_503(request):
    return render(request,'pages/error-pages/error-503.html')


#----------------------------------Authentication



@login_required(login_url="/login_home")
def login_simple(request):
    return render(request,'pages/authentication/login.html')


@login_required(login_url="/login_home")
def login_one(request):
    return render(request,'pages/authentication/login_one.html')


@login_required(login_url="/login_home")
def login_two(request):
    return render(request,'pages/authentication/login_two.html')


@login_required(login_url="/login_home")
def login_bs_validation(request):
    return render(request,'pages/authentication/login-bs-validation.html')


@login_required(login_url="/login_home")
def login_tt_validation(request):
    return render(request,'pages/authentication/login-bs-tt-validation.html')


@login_required(login_url="/login_home")
def login_validation(request):
    return render(request,'pages/authentication/login-sa-validation.html')


@login_required(login_url="/login_home")
def sign_up(request):
    return render(request,'pages/authentication/sign-up.html')


@login_required(login_url="/login_home")
def sign_one(request):
    return render(request,'pages/authentication/sign-up-one.html')


@login_required(login_url="/login_home")
def sign_two(request):
    return render(request,'pages/authentication/sign-up-two.html')


@login_required(login_url="/login_home")
def sign_wizard(request):
    return render(request,'pages/authentication/sign-up-wizard.html')


@login_required(login_url="/login_home")
def unlock(request):
    return render(request,'pages/authentication/unlock.html')


@login_required(login_url="/login_home")
def forget_password(request):
    return render(request,'pages/authentication/forget-password.html')


@login_required(login_url="/login_home")
def reset_password(request):
    return render(request,'pages/authentication/reset-password.html')


@login_required(login_url="/login_home")
def maintenance(request):
    return render(request,'pages/authentication/maintenance.html')



#---------------------------------------comingsoon

@login_required(login_url="/login_home")
def comingsoon(request):
    return render(request,'pages/comingsoon/comingsoon.html')


@login_required(login_url="/login_home")
def comingsoon_video(request):
    return render(request,'pages/comingsoon/comingsoon-bg-video.html')


@login_required(login_url="/login_home")
def comingsoon_img(request):
    return render(request,'pages/comingsoon/comingsoon-bg-img.html' )


#----------------------------------Email-Template

@login_required(login_url="/login_home")
def basic_temp(request):
    return render(request,'pages/email-templates/basic-template.html')


@login_required(login_url="/login_home")
def email_header(request):
    return render(request,'pages/email-templates/email-header.html')


@login_required(login_url="/login_home")
def template_email(request):
    return render(request,'pages/email-templates/template-email.html')


@login_required(login_url="/login_home")
def template_email_2(request):
    return render(request,'pages/email-templates/template-email-2.html')


@login_required(login_url="/login_home")
def ecommerce_temp(request):
    return render(request,'pages/email-templates/ecommerce-templates.html')


@login_required(login_url="/login_home")
def email_order(request):
    return render(request,'pages/email-templates/email-order-success.html')




@login_required(login_url="/login_home")
def pricing(request):
    context = { "breadcrumb":{"title":"Pricing","parent":"Pages", "child":"Pricing"}}
    return render(request,"pages/pricing/pricing.html",context)


#--------------------------------------faq

@login_required(login_url="/login_home")
def FAQ(request):
    context = {"breadcrumb":{"title":"FAQ","parent":"FAQ", "child":"FAQ"}}
    return render(request,'pages/FAQ/faq.html',context)


#------------------------------------------Miscellaneous----------------- -------------------------

#--------------------------------------gallery

@login_required(login_url="/login_home")
def gallery_grid(request):
    context = {"breadcrumb":{"title":"Gallery","parent":"Gallery", "child":"Gallery"}}
    return render(request,'miscellaneous/gallery/gallery.html',context)



@login_required(login_url="/login_home")
def gallery_description(request):
    context = {"breadcrumb":{"title":"Gallery Grid With Description","parent":"Gallery", "child":"Gallery Grid With Description"}}
    return render(request,'miscellaneous/gallery/gallery-with-description.html',context)



@login_required(login_url="/login_home")
def masonry_gallery(request):
    context = {"breadcrumb":{"title":"Masonry Gallery","parent":"Gallery", "child":"Masonry Gallery"}}
    return render(request,'miscellaneous/gallery/gallery-masonry.html',context)



@login_required(login_url="/login_home")
def masonry_disc(request):
    context = {"breadcrumb":{"title":"Masonry Gallery With Description","parent":"Gallery", "child":"Masonry Gallery With Description"}}
    return render(request,'miscellaneous/gallery/masonry-gallery-with-disc.html',context)



@login_required(login_url="/login_home")
def hover(request):
    context = {"breadcrumb":{"title":"Image Hover Effects","parent":"Gallery", "child":"Image Hover Effects"}}
    return render(request,'miscellaneous/gallery/gallery-hover.html',context)

#------------------------------------Blog

@login_required(login_url="/login_home")
def blog_details(request):
    context = {"breadcrumb":{"title":"Blog Details","parent":"Blog", "child":"Blog Details"}}
    return render(request,'miscellaneous/blog/blog.html',context)


@login_required(login_url="/login_home")
def blog_single(request):
    context = {"breadcrumb":{"title":"Blog Single","parent":"Blog", "child":"Blog Single"}}
    return render(request,'miscellaneous/blog/blog-single.html',context)


@login_required(login_url="/login_home")
def add_post(request):
    context = {"breadcrumb":{"title":"Add Post","parent":"Blog", "child":"Add Post"}}
    return render(request,'miscellaneous/blog/add-post.html',context)


#---------------------------------job serach

@login_required(login_url="/login_home")
def job_cards(request):
    context = {"breadcrumb":{"title":"Cards View","parent":"Job search", "child":"Cards View"}}
    return render(request,'miscellaneous/job-search/job-cards-view.html',context)


@login_required(login_url="/login_home")
def job_list(request):
    context = {"breadcrumb":{"title":"List View","parent":"Job search", "child":"List View"}}
    return render(request,'miscellaneous/job-search/job-list-view.html',context)


@login_required(login_url="/login_home")
def job_details(request):
    context = {"breadcrumb":{"title":"Job Details","parent":"Job search", "child":"Job Details"}}
    return render(request,'miscellaneous/job-search/job-details.html',context)


@login_required(login_url="/login_home")
def apply(request):
    context = {"breadcrumb":{"title":"Apply","parent":"Job search", "child":"Apply"}}
    return render(request,'miscellaneous/job-search/job-apply.html',context)

#------------------------------------Learning

@login_required(login_url="/login_home")
def course_list(request):
    context = {"breadcrumb":{"title":"Course List","parent":"Course", "child":"Course List"}}
    return render(request,'miscellaneous/courses/course-list-view.html',context)


@login_required(login_url="/login_home")
def course_detailed(request):
    context = {"breadcrumb":{"title":"Course Details","parent":"Course", "child":"Course Details"}}
    return render(request,'miscellaneous/courses/course-detailed.html',context)


#----------------------------------------Maps
@login_required(login_url="/login_home")
def data_map(request):
    context = {"breadcrumb":{"title":"Map JS","parent":"Maps", "child":"Map JS"}}
    return render(request,'miscellaneous/maps/map-js.html',context)


@login_required(login_url="/login_home")
def vector_maps(request):
    context = {"breadcrumb":{"title":"Vector Maps","parent":"Maps", "child":"Vector Maps"}}
    return render(request,'miscellaneous/maps/vector-map.html',context)


#------------------------------------Editors

@login_required(login_url="/login_home")
def quilleditor(request):
    context = {"breadcrumb":{"title":"Quill Editor","parent":"Editors", "child":"Quill Editor"}}
    return render(request,'miscellaneous/editors/quilleditor.html',context)


@login_required(login_url="/login_home")
def ckeditor(request):
    context = {"breadcrumb":{"title":"Ck Editor","parent":"Editors", "child":"Ck Editor"}}
    return render(request,'miscellaneous/editors/ckeditor.html',context)


@login_required(login_url="/login_home")
def ace_code(request):
    context = {"breadcrumb":{"title":"ACE Code Editor","parent":"Editors", "child":"ACE Code Editor"}}
    return render(request,'miscellaneous/editors/ace-code-editor.html',context)


#----------------------------knowledgebase
@login_required(login_url="/login_home")
def knowledgebase(request):
    context = {"breadcrumb":{"title":"Knowledgebase","parent":"Knowledgebase", "child":"Knowledgebase"}}
    return render(request,'miscellaneous/knowledgebase/knowledgebase.html',context)


#-----------------------------support-ticket
@login_required(login_url="/login_home")
def support_ticket(request):
    context = { "breadcrumb":{"title":"Support ticket","parent":"Support ticket", "child":"Support Ticket"}}
    return render(request,"miscellaneous/support-ticket/support-ticket.html",context)


#---------------------------------------------------------------------------------------

def signup_home(request):
    """
    GET:  render the signup form
    POST: validate + create user, or re-render form with errors
    """
    if request.method == "GET":
        return render(request, "sign-up.html")

    # ┌────────────────────────────┐
    # │         POST branch        │
    # └────────────────────────────┘
    email    = request.POST.get("email", "").strip()
    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")

    # 1) email uniqueness check
    if User.objects.filter(email=email).exists():
        messages.error(request, "That email is already registered.")
        return render(request, "sign-up.html", {
            "email": email,
            "username": username,
        })

    # 2) attempt to create the user
    try:
        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
    except Exception as e:
        logger.exception("Error creating user in signup_home")
        messages.error(
            request,
            "We hit an unexpected problem; please try again."
        )
        return render(request, "sign-up.html", {
            "email": email,
            "username": username,
        })

    # 3) success → redirect to login or home
    messages.success(request, "Account created!")
    return redirect('list_products')


def logout_view(request):
    logout(request)
    return redirect('login_home')


def login_home(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if 'next' in request.GET:
                    nextPage = request.GET['next']
                    return HttpResponseRedirect(nextPage)
                return redirect("list_products")
            else:
                messages.error(request,"Wrong credentials")
                return redirect("login_home")
        else:
            messages.error(request,"Wrong credentials")
            return redirect("login_home")
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{"form":form,})


@login_required(login_url="/login_home")
def upload_excel(request):
    if request.method != "POST":
        return redirect("list_products")

    form = UploadExcelForm(request.POST, request.FILES)
    if not form.is_valid():
        for err in form.errors.get("file", []):
            messages.error(request, err)
        return redirect("list_products")

    f = form.cleaned_data["file"]

    if ExcelUploadLog.objects.filter(user=request.user, file_name=f.name).exists():
        messages.error(
            request,
            f"E keni ngarkuar tashmë “{f.name}”. Ju lutemi riemëroni skedarin përpara se ta ngarkoni përsëri."
        )
        return redirect("list_products")

    try:
        result = import_excel_from_file(f, user=request.user)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect("list_products")

    ExcelUploadLog.objects.create(
        user=request.user,
        file_name=f.name,
        row_count=result["imported"],
        batch_id=result["batch_id"]
    )

    messages.success(request, f"✅ U importuan {result['imported']} rreshta.")
    if result["skipped"]:
        messages.warning(request, f"⚠️ U anashkaluan {len(result['skipped'])} rreshta për mungesë të dhënash.")
    if result["rejected"]:
        rejected_str = "; ".join(f"{s} prej {p} deri {d}" for s, p, d in result["rejected"])
        messages.warning(request, f"❌ {len(result['rejected'])} rreshta u refuzuan për shkak të mbivendosjes: {rejected_str}")

    return redirect("list_products")


@login_required(login_url="/login_home")
def delete_excel_batch(request, batch_id):
    if request.method != "POST":
        messages.error(request, "Kërkesa e fshirjes duhet të jetë POST.")
        return redirect("list_products")

    deleted, _ = ExcelRecord.objects.filter(batch_id=batch_id, user=request.user).delete()
    ExcelUploadLog.objects.filter(batch_id=batch_id, user=request.user).delete()
    messages.success(request, f"✅ U fshinë {deleted} rreshta dhe logu përkatës.")
    return redirect("list_products")