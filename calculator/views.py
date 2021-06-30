from django.shortcuts import render
# Create your views here.
from .calkwh import calculate as c


def peek(request):
    if request.method == 'POST':
        # 여기서 들어온 아이템을 (이름, 수량)의 튜플형태의 리스트로 변환해주고
        # 그것을 c에 넣어서 새로운 창으로 연결시켜준다.
        pass

    return render(request, 'calculator/peek.html')
