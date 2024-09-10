from datetime import datetime
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test
from book.models import Book
from order.forms import OrderCreateForm, OrderEditForm
from order.models import Order


@login_required
def create_order(request, id_book):
    book = get_object_or_404(Book, pk=id_book)
    title = 'Ordering'

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            plated_end_at = form.cleaned_data['plated_end_at']
            user = request.user
            Order.create(user=user, book=book, plated_end_at=plated_end_at)
            return render(request, 'order/order_approved.html', {
                'title': title,
                'book': book,
            })
    else:
        form = OrderCreateForm()

    return render(request, 'order/create_order.html', {
        'title': title,
        'book': book,
        'form': form,
    })


@login_required
def orders_by_user_id(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    orders = user.orders.all()
    close = len(list(filter(lambda x: x.end_at is not None, orders)))
    open_ = len(list(filter(lambda x: x.end_at is None, orders)))
    title = 'My orders'
    if request.user.pk == user_id or request.user.is_staff:
        return render(request=request, template_name='order/order_by_id.html', context={
            'title': title,
            'orders': orders,
            'user_name': user.last_name + ' ' + user.first_name,
            'closed_orders': close,
            "open_orders": open_,
        })
    else:
        raise Http404("You do not have permission to view these orders.")


@login_required
@user_passes_test(lambda u: u.is_staff)
def all_orders(request):
    orders = Order.objects.all()
    title = 'Orders'
    close = len(list(filter(lambda x: x.end_at is not None, orders)))
    open_ = len(list(filter(lambda x: x.end_at is None, orders)))
    return render(request=request, template_name='order/orders.html', context={
        'title': title,
        'orders': orders,
        'closed_orders': close,
        "open_orders": open_,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def order_bel_by_id(request, order_id):
    if Order.delete_by_id(order_id):
        return redirect('orders:list_orders')


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_order_by_id(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:orders_by_user_id', order.user.pk)
    else:
        form = OrderEditForm(instance=order)
    return render(request, 'order/edit_order.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def order_close_by_id(request, order_id):
    if order_id:
        order = get_object_or_404(Order, id=order_id)
        order.update(end_at=datetime.now())
        return redirect('orders:orders_by_user_id', order.user.pk)
