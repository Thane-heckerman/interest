from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import re
import requests
import bs4
import json
from .forms import RegistrationForms
from django.contrib.auth.decorators import login_required
from Home.models import History, statusTracking
from django.contrib.auth.models import User
from django.conf import settings
# Create your views here.

#tạo hàm login

#tạo hàm register
def register(request):
    form = RegistrationForms()
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Home/')
    return render(request,'register.html', {'form':form})    
#tạo hàm logout



#trang chủ
def index(request):
    return render(request, 'mainpage.html')


#logic code
@login_required
def interest(request):
    user_id = request.user.id
    data = History.objects.all().order_by('-id').filter(user_id = user_id)[:10]
    return render(request, 'home.html', {'data':data})

#delete_history
def delete_history(request,id):
    history = History.objects.filter(id = id) #pk - primary key
    history.delete()
    return HttpResponseRedirect('/Home/interest/')    

def get_interest_rate(url,str):
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    pattern = re.compile(str)
    td_elements = soup.find('td', string = pattern)
        
    interest_rates = []
    if len(td_elements) == 0:
        return('error')
    else:
        for td in td_elements:
            interest_rate = td.find_next('td').text.strip().strip('%').replace(',','.')
            interest_rates.append(interest_rate)
            rate = float(interest_rates[0])
        return rate
# vcb

vcb_interest = []
url_vcb='https://portal.vietcombank.com.vn/UserControls/TVPortal.TyGia/pListLaiSuat.aspx?CusstomType=1&BacrhID=1&InrateType=&isEn=False&numAfter=2'

months = ['Không kỳ hạn',
        r'\u0031\u0034\u0020\u006e\u0067\u00e0\u0079', 
        r'\u0031\u0020\u0074\u0068\u00e1\u006e\u0067',
        r'\u0033\u0020\u0074\u0068\u00e1\u006e\u0067',
        r'\u0036\u0020\u0074\u0068\u00e1\u006e\u0067',
        r'\u0031\u0032\u0020\u0074\u0068\u00e1\u006e\u0067']
for i in months:
    a = get_interest_rate(url_vcb,i)
    vcb_interest.append(a)
# print('vcb: ' ,vcb_interest)


# vietin

url_vietin = 'https://www.vietinbank.vn/web/home/vn/lai-suat'
response = requests.get(url_vietin)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')

vietin_interest = set(re.findall(r'\d+,\d+',html))
vietin_interest = sorted([float(item.replace(',','.')) for item in vietin_interest])

# print('vietin: ',vietin_interest)
# interest_vietin = float(interest[42].replace(',','.'))
# dict2 = {'vietin': interest_vietin}

# # 6 tháng
# unicode_str = ['Dưới 1 tháng',
#                r'\u0054\u1eeb\u0020\u0031\u0020\u0074\u0068\u00e1\u006e\u0067\u0020\u0111\u1ebf\u006e\u0020\u0064\u01b0\u1edb\u0069\u0020\u0032\u0020\u0074\u0068\u00e1\u006e\u0067\u000d',
#                r'\u0044\u01b0\u01a1\u0301\u0069\u0020\u0031\u0020\u0074\u0068\u00e1\u006e\u0067',
#                r'\u0074\u1eeb\u0301\u0020\u0031\u0020\u0074\u0068\u00e1\u006e\u0067\u0020\u0111\u00ea\u0301\u006e\u0020\u0064\u01b0\u1edb\u0069\u0020\u0032\u0020\u0074\u0068\u00e1\u006e\u0067',
#                r'\u0054\u1eeb\u0301\u0020\u0033\u0020\u0074\u0068\u00e1\u006e\u0067\u0020\u0111\u00ea\u0301\u006e\u0020\u0064\u01b0\u1edb\u0069\u0020\u0034\u0020\u0074\u0068\u00e1\u006e\u0067',
#                r'\u0054\u1eeb\u0020\u0036\u0020\u0074\u0068\u0061\u0301\u006e\u0067\u00A0\u0111\u00ea\u0301\u006e\u0020\u0064\u01b0\u1edb\u0069\u0020\u0037\u0020\u0074\u0068\u0061\u0301\u006e\u0067', 
#                r'\u0031\u0032\u0020\u0074\u0068\u00e1\u006e\u0067']
# for i in unicode_str:
#     vietin = get_interest_rate(url_vietin,i)
#     print(vietin)



# bidv

url_bidv = 'https://bidv.com.vn/ServicesBIDV/InterestDetailServlet'
response = requests.get(url_bidv).content
decode = json.loads(response)
# print(decode)
bidv_interest = set()
for item in decode['hcm']['data']:
    bidv_interest.add(float(item['VND']))
bidv_interest = list(bidv_interest)


# tcb
# thông tin lãi suất của tcb là file download 

tcb_interest = [0.5, 4.30, 6.45]


#def hàm lập dict cho các mốc thời gian và return là một kết quả sau đó viết function js để truyền kết quả đó vào trong hàm lowest 
#lập dict cho các mốc thời gian
below_one_month = {'vcb': vcb_interest[0] , 'tcb': tcb_interest[0] , 'bidv': bidv_interest[0] , 'vietin': vietin_interest[2] }
one_month =  {'vcb': vcb_interest[2] , 'tcb': tcb_interest[1] , 'bidv': bidv_interest[1] , 'vietin': vietin_interest[3] }
two_months =  {'vcb': vcb_interest[2] , 'tcb': tcb_interest[1] ,'bidv': bidv_interest[1] , 'vietin': vietin_interest[3] }
three_months =  {'vcb': vcb_interest[3] , 'tcb': tcb_interest[1] , 'bidv': bidv_interest[2] , 'vietin': vietin_interest[6] }
four_months =  {'vcb': vcb_interest[3] , 'tcb': tcb_interest[1] , 'bidv': bidv_interest[2] , 'vietin': vietin_interest[6] }
five_months =  {'vcb': vcb_interest[3] , 'tcb': tcb_interest[1] , 'bidv': bidv_interest[2] , 'vietin': vietin_interest[6] }
six_months =  {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] ,'bidv': bidv_interest[3] , 'vietin': vietin_interest[8] }
seven_months = {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[3] , 'vietin': vietin_interest[8] }
eight_months = {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[3] , 'vietin': vietin_interest[8] }
nine_months = {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[3] , 'vietin': vietin_interest[8] }
ten_months = {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[4] , 'vietin': vietin_interest[10] }
eleven_months = {'vcb': vcb_interest[4] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[4] , 'vietin': vietin_interest[10] }
twelve_months =  {'vcb': vcb_interest[5] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[4] , 'vietin': vietin_interest[10] }
twenty_four_months = {'vcb': vcb_interest[5] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[4] , 'vietin': vietin_interest[10] }
thirty_six_months = {'vcb': vcb_interest[5] , 'tcb': tcb_interest[2] , 'bidv': bidv_interest[4] , 'vietin': vietin_interest[10] }


# gộp views dưới thành 1 views mà truyền vào các tham số là các dict về thông tin lãi suất
@login_required

def lowest1(request):

    lowest = min(below_one_month.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
    
@login_required

def lowest2(request):
    lowest = min(one_month.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest3(request):
    lowest = min(two_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest4(request):
    lowest = min(three_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest5(request):
    lowest = min(four_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest6(request):
    lowest = min(five_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest7(request):
    lowest = min(six_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest8(request):
    lowest = min(seven_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest9(request):
    lowest = min(eight_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest10(request):
    lowest = min(nine_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest11(request):
    lowest = min(ten_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest12(request):
    lowest = min(eleven_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest13(request):
    lowest = min(twelve_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest14(request):
    lowest = min(twenty_four_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response
@login_required

def lowest15(request):
    lowest = min(thirty_six_months.items(), key=lambda x: x[1])
    res = str(lowest[0]) + ':' + ' ' + str(lowest[1])
    response = HttpResponse(res)
    return response

#Hàm update db is_enabled

def changeStatus(request):
    user_id = request.user
    user = statusTracking.objects.get(user_id_id = user_id )
    print(user)

    status = user.is_enabled
    print(status)
    
    if status == True:  
        print('true')
        context = {'status': 'đang tắt',
                   'action': 'bật ghi lịch sử'}
        statusTracking.objects.filter(user_id=user_id).update(is_enabled=False)
        
        
        # return HttpResponse('đã tắt')
    
    # else is_enabled == False:
    else:
        print('false')
        context = {'status': 'đang bật',
                   'action': 'tắt ghi lịch sử'}
        statusTracking.objects.filter(user_id=user_id).update(is_enabled=True)
        
        # return HttpResponse('đã bật')
    
    return render(request,'onofftracking.html', context=context)

#Hàm redirect đến trang toggle history tracking

def redirectToggle(request):
    return render (request, 'onofftracking.html')

