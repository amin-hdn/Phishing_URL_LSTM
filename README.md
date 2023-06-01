# Phishing_URL_LSTM
Detect phishing URL using Deep Learning, (LSTM network).

"This paper focuses on using DL algorithms for detecting
phishing URLs. Particularly, a novel hybrid deep learning
model, which combines the power of a Deep Neural Network (DNN) model
using **the lexical and statistical analysis**
of URLs and a long short-term memory network (LSTM)-
based model using character embedding-based features,
was proposed and validated using phishing detection
datasets." from an article ??

## Fisrt we should tranform URL to a DATA informations :
  HOW ?  **the lexical and statistical analysis** using DNN

### THERE ARE 3 THINGS we should analyse :
  #### 1. Lexical Features:
  These refer to statistical features extracted from the literal URL string. For example, length of the URL string, number of digits, number of parameters in its query part, if the URL is encoded.
  those the feartures that you can extract.
  
  ![alt text](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*laAcBkYX2GMMm7gJNGWwWQ.png)
  
  all features that I found in this article [article](https://sci-hub.st/https://link.springer.com/chapter/10.1007/978-3-319-46298-1_30)
  
| Entropy Domain and Extension        |                     |  |
|-------------------------------------|---------------------|--|
| CharacterContinuityRate             |                     |  |
| Features related with Length Ratio  |                     |  |
|                                     | argPathRatio        |  |
|                                     | argUrlRatio         |  |
|                                     | argDomain           |  |
|                                     | domainUrlRatio      |  |
|                                     | pathUrlRatio        |  |
|                                     | PathDomainRatio     |  |
| Features related to count of Letter |                     |  |
|                                     | Symbol Count Domain |  |
|                                     | Domain token count  |  |
|                                     | Query Digit Count   |  |
|                                     | tld                 |  |
| Number Rate of                      |                     |  |
|                                     | Domain              |  |
|                                     | DirectoryName       |  |
|                                     | FileName            |  |
|                                     | URL                 |  |
|Features related to Length           |                     |  |
|                                     | url Len             |  |
|                                     | domain Len          |  |
|                                     | file Name Len       |  |
|                                     | Longest WordLength3 |  |
|                                     | Longest Path Token Length           |  |
|                                     | avgpathtokenlen     |  |
|ldl getArg                           |                     |  |
|spcharUrl                            |                     |  |

  _______________
Continuity rate: We categorize the character type in the URL as letter, digit and symbol.
Then we record the longest continuous length for each type.   [article](https://sci-hub.st/https://onlinelibrary.wiley.com/doi/abs/10.1111/coin.12422)
  
  #### 2. Host-Based Features:
  these are characteristics of the host-name properties of the URL. These provide information about the host of the webpage, for example, country of registration, domain name properties, open ports, named servers, connection speed, time to live from registration.
  
    ![alt text](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*LVgaeM48ny2kr36FMIxlBg.png)
    
    
  _______________
  
  #### 3. Content Features: (optional)
  These are obtained from the downloaded HTML code of the webpage. These features capture the structure of the webpage and the content embedded in it. These will include information on script tags, embedded objects, executables, hidden elements. 
  _______________

  
  
## Second we should create a LSTM Model Network Model :
  HOW ?  character embedding-based features using (LSTM) 
## Third we should verify :
