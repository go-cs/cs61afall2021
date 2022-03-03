'''
Author: your name
Date: 2022-03-01 21:42:42
LastEditTime: 2022-03-01 22:09:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc12.py
'''
import re
def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    # for _____________________:
    #     'Use as many lines as necessary'
    #return bool(re.search(pattern, email))
    domains_list = "|".join([domain.replace(".", "\.") for domain in domains])
    return bool(re.search(rf"^\w+@({domains_list})$", email))