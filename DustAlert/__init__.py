import datetime
import logging

import azure.functions as func
from .dust import get_dust_information
from .mail import send_mail


def is_dust_severe(d, threshold=1):
    return True
    if d['pm25_grade'] >= threshold or d['pm10_grade'] >= threshold:
        return True


def format_mail_content(d):
    content = '오늘의 미세먼지 정보입니다.\n\n'
    content += f'미세먼지 - {d["pm10"]} ㎍/㎥ ({d["pm10_grade_str"]})\n'
    content += f'초미세먼지 - {d["pm25"]} ㎍/㎥ ({d["pm25_grade_str"]})\n'
    return content


def main(mytimer: func.TimerRequest) -> None:
    d = get_dust_information()
    if is_dust_severe(d):
        send_mail(format_mail_content(d))
        logging.info('Mail Sent at ' + str(datetime.datetime.now()))
