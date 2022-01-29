from random import sample

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#  sample功能：从序列a中随机抽取n个元素，并将n个元素生以list形式返回
def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    content = '<h3>今天推荐的水果是：</h3>'
    content += '<hr>'
    content += '<ul>'
    for fruit in selected_fruits:
        content += f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)




