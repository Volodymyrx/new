# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt
import codecs


# def generate_page(head, body):
#     return f'<html>{head}{body}</html>'


def generate_head(title):
    return f'<head><meta charset="utf-8"><title>{title}</title></head>'


def generate_article(header, paragraphs):
    article = f'<h1>{header}</h1>'
    for row in paragraphs:
        article += f'<p>{row}</p>'
    return f'<article>{article}</acticle>'


def generate_footer(link, text) -> str:
    return f'<p><a href="{link}">{text}</a></p>'


def generate_body(article, footer) -> str:
    return f'<body>{article}{footer}</body>'


def create_html(data: dict) -> bool:
    # create file html
    head = generate_head(data['title'])
    article = generate_article(data['name_article'],
                               data['text_article'])
    footer = generate_footer(data['link'], data['a_text'])
    body = generate_body(article, footer)

    page = f'<!DOCTYPE html><html lang="en">{head}{body}</html>'
    try:
        with codecs.open(data['file_name_html'], 'w', 'utf-8') as fp:
            fp.write(page)
        is_ok = True
    except:
        is_ok = False
    return is_ok


data_index_html = {
    'file_name_html': 'index.html',
    'title': 'Main page horoscope',
    'name_article': 'Что день ' + str(dt.now().date()) + ' готовит',
    'text_article': generate_prophecies(),
    'link': 'about.html',
    'a_text': 'About project',
}

data_about_html = {
    'file_name_html': 'about.html',
    'title': 'About page horoscope',
    'name_article': 'Описание проекта',
    'text_article': ['Эта страница о проекте обучения по курсу школы '
                     'SkillFactory - изучение Python - генерация Горскопа'],
    'link': 'index.html',
    'a_text': 'Main page Horoscope',
}
print('index.html - ok? ', create_html(data_index_html))
print('about.html - ok? ', create_html(data_about_html))
