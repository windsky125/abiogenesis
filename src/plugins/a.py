# coding=utf-8
"""
    @project: automation_tools
    @Author：gaojs
    @file： test008.py
    @date：2022/8/17 17:36
    @blogs: https://www.gaojs.com.cn
"""
import requests


def dayly_news(news_type):
    """
    每日新闻:news_type	支持类型top(推荐,默认)guonei(国内)guoji(国际)yule(娱乐)tiyu(体育)junshi(军事)keji(科技)caijing(财经)youxi(游戏)qiche(汽车)jiankang(健康)
    """
    url = f'http://v.juhe.cn/toutiao/index?type={news_type}&page=1&page_size=30&is_filter=0&key=cb53bd41a74ef445a2d1b7fcfebe6fa0'
    resp = requests.get(url=url)
    with open('title.txt', mode='a+', encoding='utf=8') as fin:
        fin.write(news_type + ' 新闻 ' + '\n')
        fin.write('\n')
    t = eval(resp.text)
    try:
        for i in range(30):
            s = t.get('result').get('data')[i].get('title')
            # i = i + 1
            with open('title.txt', mode='a+', encoding='utf=8') as fin:
                fin.write(str(i+1) + '.' + s + '\n')
    except Exception as e:
        print(e)
    finally:
        with open('title.txt', mode='a+', encoding='utf=8') as fin:
            fin.write('\n')


if __name__ == '__main__':
    dayly_news('guonei')
    dayly_news('guoji')
    dayly_news('yule')
    dayly_news('tiyu')
    dayly_news('junshi')
    dayly_news('keji')
    dayly_news('caijing')
    dayly_news('youxi')
    dayly_news('qiche')
    dayly_news('jiankang')