from math import log
from re import compile
from urllib.parse import urlparse
from socket import gethostbyname
from pyquery import PyQuery
from requests import get
from json import dump
from string import ascii_lowercase
from numpy import array
import time

class LexicalURLFeature:
    def __init__(self, url:str) :
        self.description = 'description'
        self.url = url
        # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        self.urlParse = urlparse(url) 
        self.host = self.__get_ip()

    def __get_ip(self):
        try:
            ip = self.urlParse.netloc if self.url_host_is_ip() else gethostbyname(self.urlParse.netloc)
            return ip
        except:
            return None
        
    def __get_entropy(self, text:str): # H(x) = sigma(pi*log2(1/pi))
        text = text.lower()
        probs = [text.count(c) / len(text) for c in set(text)]
        entropy = -sum([p * log(p) / log(2.0) for p in probs])
        return entropy
        
    # extract lexical features

    def url_scheme(self):
        print(self.url)
        print(self.urlParse)
        return self.urlParse.scheme
    
    def url_path_length(self):
        return len(self.urlParse.path)
    
    def url_host_length(self):
        return len(self.urlParse.netloc)
    
    def url_host_is_ip(self):
        host = self.urlParse.netloc
        pattern = compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        match = pattern.match(host)
        return match is not None
    
    def url_has_port_in_string(self):
        has_port = self.urlParse.netloc.split(':')
        return len(has_port) > 1 and has_port[-1].isdigit() #  ??? Why the second condition there any posibility that :Port can something else ???
    
    def number_of_digits(self):
        digits = [i for i in self.url if i.isdigit()]
        return len(digits)
    
    def number_of_parameters(self):
        params = self.urlParse.query
        return 0 if params == '' else len(params.split('&'))
    
    # def number_of_parameters(self):
    #     params = self.urlParse.query
    #     return 0 if params == '' else params.count('&') + 1
    
    def number_of_fragments(self):
        frags = self.urlParse.fragment
        return frags.count('#') if frags != '' else 0
    

    # def number_of_fragments(self):
    #     frags = self.urlParse.fragment
    #     return len(frags.split('#')) - 1 if frags == '' else 0

    def is_encoded(self):
        return '%' in self.url
    
    def num_encoded_char(self):
        if self.is_encoded() : return self.url.count('%')

    def url_string_entropy(self):
        return self.__get_entropy(self.url)
    
    def number_of_subdirectories(self):
        d = self.urlParse.path.split('/')
        return len(d)-1

    # def number_of_subdirectories(self):
    #     d = self.urlParse.path.count('/') 
    #     return d


    def number_of_periods(self):
        periods = [i for i in self.urlParse.path if i == '.'] 
        return len(periods)
    
    def number_of_dots(self):
        dots = [i for i in self.url if i == '.'] ## ??
        return len(dots)
    

    # def number_of_periods(self):
    #     periods = self.urlParse.count('.')
    #     return periods

    def has_client_in_string(self):
        return 'client' in self.url.lower()
    
    def has_admin_in_string(self):
        return 'admin' in self.url.lower() 
    
    def has_server_in_string(self):
        return 'server' in self.url.lower()

    def has_login_in_string(self):
        return 'login' in self.url.lower()
    
    def get_tld(self): # https://miro.medium.com/v2/resize:fi
                                           #----
      return self.urlParse.netloc.split('.')[-1].split(':')[0]
    
    def CharacterContinuityRate(self):
        if not self.url_host_is_ip():
            Domain = self.urlParse.netloc.split('.')[1]
            counter = dict()
            counter['digit'] = 0
            counter['alpha'] = 0
            counter['symbol'] = 0
            counter_digit__ = 0
            counter_alpha__ = 0
            counter_symbol__ = 0
            was_alpha = False
            was_digit = False
            was_symbol = False

            for c in Domain :

                if c.isdigit() :
                    if was_digit :
                        counter_digit__ +=1
                    else : 
                        was_alpha, was_symbol, was_digit = False ,False, True
                        counter_digit__  = 1
                    counter['digit']= max(counter['digit'], counter_digit__)

                        

                    
                elif c.isalpha() :
                    if was_alpha :
                        counter_alpha__ +=1
                    else : 
                        was_digit, was_symbol, was_alpha = False ,False, True
                        counter_alpha__  = 1
                    counter['alpha']= max(counter['alpha'], counter_alpha__)

                else  :                  
                    if was_symbol : 
                        counter_symbol__ +=1
                    else : 
                        was_digit, was_alpha, was_symbol = False ,False, True
                        counter_symbol__  = 1
                    counter['symbol']= max(counter['symbol'], counter_symbol__)
            return (counter['alpha']+ counter['digit']+ counter['symbol'])/len(Domain)
        else :
            return 4/15


    def domain_token_count(self):
        token_count= self.url.count('/') - 2
        return token_count

    def Path_Domain_ratio(self):
        path_ = len(self.urlParse.path)
        domain_ = len(self.urlParse.netloc)
        return path_ / domain_
    

    def Path_URL_ratio(self):
        path_ = len(self.urlParse.path)
        URL_ = len(self.url)
        return path_ / URL_
    
    def  Query_Digit_Count(self):# Number of digits in the query part of the URL.
        digits = [i for i in self.urlParse.query if i.isdigit()]
        return len(digits)



############# Calculate the tld's uses by benign and Malicious URLS , to find which tld more used by malicious URLS
# import numpy as np

# #create dummies from TLD column
# tldmat = pd.get_dummies(data.tld)

# ##label new dummies matrix
# tldmat['tag'] = data['tag']

# ### subset malicious and benign sampls
# tldmal = tldmat[tldmat['tag'] == 'malware']
# tldben = tldmat[tldmat['tag'] == 'benign']

# dd = []
# for i in tldmat.columns[:-1]:
#     md = np.mean(tldmal[i]) - np.mean(tldben[i])
#     y = ttest_ind(tldmal[i], tldben[i])
#     d2 = [i, md, y[1]]
#     dd.append(d2)
    
# dd = pd.DataFrame(dd)
# dd.columns = ['Feature', 'Mean_Difference', 'P_Value']
# dd = dd.sort_values(['Mean_Difference', 'P_Value'], ascending=[False, True])

################################# we care about it later
    
if __name__ == "__main__":
    start_time = time.time_ns()
    URL_exemple = r"https://miro.abc123@_8at.com/v2/resize:fit:1100/format:webp/1*laAcBkYX2GMMm7gJNGWwWQ.png"
    object_ = LexicalURLFeature(URL_exemple)
    # print("######################  url_host_is_ip ##################################")
    # print(object_.url_host_is_ip())
    # print("######################  url_host_length ##################################")
    # print(object_.url_host_length())
    # print("######################  url_path_length ##################################")
    # print(object_.url_path_length())
    # print("######################  url_scheme ##################################")
    print(object_.urlParse.netloc)
    print(object_.CharacterContinuityRate())
    print("--- %s seconds ---"  % (time.time_ns() - start_time))
