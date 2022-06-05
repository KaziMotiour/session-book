from django.shortcuts import render
import requests
from .models import Product
from datetime import datetime
# Create your views here.


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'p_index.html', context)


def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    recently_viewed_product = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        recently_viewed_product = Product.objects.filter(
            pk__in=request.session['recently_viewed'])
        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()

    else:
        request.session['recently_viewed'] = [product_id]

   

    currentDT = datetime.now()

    userInfo = [
        {
            'id': 1,
            'username': 'motiour',
            'text_answer':'',
            'check_box_answer':[]
        },
        {
            'id': 2,
            'username': 'sayam',
            'text_answer':'',
            'check_box_answer':[]
        }
    ]

    set_answer1 = [{
                    'start_time' : currentDT.hour,
                    'is_compete' : False,
                    'survy_title' : '',
                    'question' : [{
                        'title' : '',
                        'type' : '',
                        'text_anwer' : '',
                        'select_anser' : []
                }]
            }  
    ]

    set_answer2 = [{
        'question' : [{
                        'title' : '',
                        'type' : '',
                        'text_anwer' : '',
                        'select_anser' : []
                }]
    }]

    # For quesiton session  
    # request.session['quesions2'] = userInfo
    exist_item = None

    if len(list(filter(lambda x : x['username']=='motiour', request.session['quesions2']))) >=1:
        index = [user['username'] for user in request.session['quesions2']].index('motiour')
        print(index)
        removed_user  =  request.session['quesions2'].pop(index) 
        removed_user['text_answer'] = 'hello motiour'
        request.session['quesions2'].insert(index, removed_user)
    
    else:
        print('not found')
        pass

    # fro quesion2 session

    # request.session['quesions']
    
    print(request.session.items())
    request.session.modified = True

    context = {
        'product': product,
        'recently_viewed_product': recently_viewed_product
    }
    return render(request, 'product.html', context)


def load_product(request):

    r = requests.get('http://fakestoreapi.com/products')
    print(r.json())
    # for item in r.json():
    #     product = Product(
    #         title = item['title'],
    #         description = item['description'],
    #         price = item['price'],
    #         image_url = item['image'],
    #     )
    #     product.save()
    return render(request, 'p_index.html')
