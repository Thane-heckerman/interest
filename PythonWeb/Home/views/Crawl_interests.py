import re
import requests
import bs4
import json

#phải có thêm hàm init và cuối file phải có hàm main
# tài liệu: https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
class Interest_rate:
    def __init__(self):
        self.vcb_interest = []
        self.tcb_interest = []
        self.vietin_interest = []
        self.bidv_interest = []
    
    def vcb_interest_rate(self):
        url_vcb='https://portal.vietcombank.com.vn/UserControls/TVPortal.TyGia/pListLaiSuat.aspx?CusstomType=1&BacrhID=1&InrateType=&isEn=False&numAfter=2'

        html = requests.get(url_vcb).content
        soup = bs4.BeautifulSoup(html, 'html.parser')
        months = ['Không kỳ hạn',
                r'\u0031\u0034\u0020\u006e\u0067\u00e0\u0079', 
                r'\u0031\u0020\u0074\u0068\u00e1\u006e\u0067',
                r'\u0033\u0020\u0074\u0068\u00e1\u006e\u0067',
                r'\u0036\u0020\u0074\u0068\u00e1\u006e\u0067',
                r'\u0031\u0032\u0020\u0074\u0068\u00e1\u006e\u0067']
        for i in months:
            pattern = re.compile(i)
            td_elements = soup.find('td', string = pattern)
            # print(td_elements)
            for td in td_elements:
                interest_rate = td.find_next('td').text.strip().strip('%').replace(',','.')
                self.vcb_interest.append(float(interest_rate))
        return self.vcb_interest

    # vietin
    def vietin_interest_rate(self):
        url_vietin = 'https://www.vietinbank.vn/web/home/vn/lai-suat'
        response = requests.get(url_vietin)
        html = response.text
        vietin_interest = set(re.findall(r'\d+,\d+',html))
        vietin_interest = sorted([float(item.replace(',','.')) for item in vietin_interest])
        self.vietin_interest = vietin_interest
        return self.vietin_interest
    
    # bidv
    def bidv_interest_rate(self):
        url_bidv = 'https://bidv.com.vn/ServicesBIDV/InterestDetailServlet'
        response = requests.get(url_bidv).content
        decode = json.loads(response)
        # print(decode)
        bidv_interest = set()
        for item in decode['hcm']['data']:
            bidv_interest.add(float(item['VND']))
        bidv_interest = sorted(list(bidv_interest))
        self.bidv_interest = bidv_interest
        return self.bidv_interest


    # tcb
    # thông tin lãi suất của tcb là file download 
    def tcb_interest_rate(self):
        self.tcb_interest = [0.5, 4.30, 6.45]
        return self.tcb_interest 

    def interest_by_month(self):
        self.tcb_interest_rate()
        self.bidv_interest_rate()
        self.vietin_interest_rate()
        self.vcb_interest_rate()

    #def hàm lập dict cho các mốc thời gian và return là một kết quả sau đó viết function js để truyền kết quả đó vào trong hàm lowest 
    #lập dict cho các mốc thời gian
        below_one_month = {'vcb': self.vcb_interest[0] , 'tcb': self.tcb_interest[0] , 'bidv': self.bidv_interest[0] , 'vietin': self.vietin_interest[2] }
        one_month =  {'vcb': self.vcb_interest[2] , 'tcb': self.tcb_interest[1] , 'bidv': self.bidv_interest[1] , 'vietin': self.vietin_interest[3] }
        two_months =  {'vcb': self.vcb_interest[2] , 'tcb': self.tcb_interest[1] ,'bidv': self.bidv_interest[1] , 'vietin': self.vietin_interest[3] }
        three_months =  {'vcb': self.vcb_interest[3] , 'tcb': self.tcb_interest[1] , 'bidv': self.bidv_interest[2] , 'vietin': self.vietin_interest[6] }
        four_months =  {'vcb': self.vcb_interest[3] , 'tcb': self.tcb_interest[1] , 'bidv': self.bidv_interest[2] , 'vietin': self.vietin_interest[6] }
        five_months =  {'vcb': self.vcb_interest[3] , 'tcb': self.tcb_interest[1] , 'bidv': self.bidv_interest[2] , 'vietin': self.vietin_interest[6] }
        six_months =  {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] ,'bidv': self.bidv_interest[3] , 'vietin': self.vietin_interest[8] }
        seven_months = {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[3] , 'vietin': self.vietin_interest[8] }
        eight_months = {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[3] , 'vietin': self.vietin_interest[8] }
        nine_months = {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[3] , 'vietin': self.vietin_interest[8] }
        ten_months = {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[4] , 'vietin': self.vietin_interest[10] }
        eleven_months = {'vcb': self.vcb_interest[4] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[4] , 'vietin': self.vietin_interest[10] }
        twelve_months =  {'vcb': self.vcb_interest[5] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[4] , 'vietin': self.vietin_interest[10] }
        twenty_four_months = {'vcb': self.vcb_interest[5] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[4] , 'vietin': self.vietin_interest[10] }
        thirty_six_months = {'vcb': self.vcb_interest[5] , 'tcb': self.tcb_interest[2] , 'bidv': self.bidv_interest[4] , 'vietin': self.vietin_interest[10] }

        return below_one_month,one_month,two_months,three_months,four_months,five_months,six_months,seven_months,eight_months,nine_months,ten_months,eleven_months,twelve_months,twenty_four_months,thirty_six_months 
               
# if __name__ == "__main__":
#     scraper = Interest_rate()
#     scraper.interest_by_month()
#     interest_data = scraper.interest_by_month()
#     print(interest_data)

'''Note: để tương tác với một att của class thì phải tạo một obj chính là class đó sau đó 
python mới truyền vào hàm attr của object đó argument self'''


