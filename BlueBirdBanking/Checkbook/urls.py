from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page index.html.
    path('', views.home, name='index'),
    # sets the url path to Create a new account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    #sets the url bath to balance sheet page balancesheet.html.
    path('<int:pk>/balance/', views.balance, name='balance'),
    #sets the url path to add new transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]