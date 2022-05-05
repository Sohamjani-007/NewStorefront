from django.forms import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Avg, Max, Min, Sum
from django.http import HttpResponse
from store.models import Collection, Customer, Order, Product, OrderItem
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem, Tag

from tags.models import TaggedItem

# Create your views here.
# request handler or action or request --> response


def say_hello(request):


    soham = {'likes': 'pizza', 'place': "Joe's",
             'products': ['apple', 'banana', 'grapes', 'mangoes']}
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=10)
    # Shows inventory AND unit_price
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=10))
    # # Q helps to implement a binary OR, AND, NOT i.e inventory__lt OR unit_price__lt
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=10))
    # # Shows inventory__lt AND NOT unit_price__lt
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # # Shows referencing fields inventory EQUALS unit_price
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    # # Shows referencing fields inventory of product with the id of its collection.
    # queryset = Product.objects.filter(collection__id=1).order_by('unit_price')
    # # Collection__id is filtered and then it is sorted ascending order unit_price.
    # queryset = Product.objects.filter(collection__id=1).order_by('-title')
    # # Collection__id is filtered and then it is sorted descending order unit_price.
    # product = Product.objects.order_by('unit_price')[0]
    # # Here, as we acctess a individual element, queryset is evalated and we get actual object.
    # product = Product.objects.earliest('unit_price')
    # # Earliest is a method and return the first object.
    # product = Product.objects.latest('unit_price')
    # # Latest is a method and return the last object.
    # queryset = Product.objects.all()[:5]
    # # 1, 2, 3, 4
    # queryset = Product.objects.all()[5:10]
    # # 5, 6, 7, 8, 9
    # queryset = Product.objects.filter(pk=0).exists()
    # # shows in bool
    # queryset = Product.objects.filter(pk=0).first()
    # # Show no error and tell first is null
    # queryset = Product.objects.values('id', 'title', 'collection__id')
    # # values gives dicionary output and allows selected columns to appear.
    # queryset = Product.objects.values_list('id', 'title', 'collection__id')
    # # values gives tuple output and allows selected columns to appear.
    # queryset = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order('title')
    # # id__in = look up type. # distinct = its a method of queryset to get rid of duplicates.
    # queryset = Order.objects.select_related('customer').order_by('placed_at')[:-5]
    # # As there (-placed_at) or [:-5] this will give the last 5 customers who placed order.
    # queryset = Product.objects.select_related('collection').all()
    # # select_related('customer')= Customer(Database table) = will contain all the attributes in it.

    # result = Product.objects.filter('collection_id').aggregate(count=Count('id'), min_price=Min('unit_price'))
    # # from Product class and collection_id attribute, we count how many IDs are there and whats the min price of it.
    # # Remember filter always comes before aggregate method.

    # ## EXCERCISE --
    # # How many orders do we have?
    # result = Order.objects.aggregate(count=Count('id'))
    # # How many units of product 1 have we sold?
    # result = OrderItem.objects.filter('product_id=1').aggregate(sold=Sum('quantity'))
    # # How many orders has customer 1 placed?
    # result = Order.objects.filter('customer_id=1').aggregate(count=Count('id'))
    # # What is the min, max and average price of the products in collection 3?
    # result = Product.objects.filter('collection__id=3').aggregate(count=Count('id'), min_price=Min('unit_price'), maxprice=Max('unit_price'), avg_price=Avg('unit_price'))

    # queryset = Customer.objects.annotate(is_new=Value(True))
    # # Annotating a new field in column of database
    # # Value is an expression.
    # queryset = Customer.objects.annotate(is_new=F('id'))
    # # this refers is_new field to actual id field of customers.

    # # Calling Database Functions
    # queryset = Customer.objects.annotate(

    #     full_name = Func(F('first_name', Value(' '), F('last_name'), function=Concat)
    # ))

    # queryset = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '), ('last_name')
    # ))
    # # Here, we do not needadd1 to put F, function=CONCAT

    # queryset = Customer.objects.annotate(order_count=Count('order'))
    # # Annotate --> Adds a extra order table in database.
    # # Count --> method from aggregate.
    # # Customer is no field called order but Order has a field called customer which has Customer Class.
    # # Therefore, this creates a reverse relational by Django or related_name=order.Thus no of order from customer is counted.

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )
    # # This will create a new field for Product which discounted unit_price by 0.8
    # # and the output will be given in DecimalField.

    # ## EXCERCISE -
    # queryset = Customer.objects.filter('customer_id').annotate(last_order=Max('order__id'))
    # # Customer and their last order
    # result = Collection.objects.aggregate(product_count=Count('product_id'))
    # # Collection and count of their products.
    # result = Customer.objects.annotate(order_count=Count('order').filter('order_count__gt=5'))
    # # Customers with more than 5 orders.
    # result = Customer.objects.annotate(total_spent=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity')))
    # # Customers and the total amount they’ve spent.
    # result = Product.objects.annotate(top_five=Sum(
    #     F('orderitem__unit_price') *
    #     F('orderitem__quantity'))).order_by('-top_five')[:5]
    # # Top 5 best-selling products and their total sales.


    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.select_related('tag').filter(content_type = content_type,object_id=1)
    return render(request, 'hello.html', soham)
    # return render(request, 'hello.html', soham, {'tags' : list(queryset)})
    # return render(request, 'hello.html', {'name': 'Soham', 'products': product})



