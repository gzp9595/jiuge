from PIL import Image, ImageFont, ImageDraw
import time
import datetime

def add_ideal(ans, yan, jtype, tt, ideal, lk = u'九歌作'):
    ys = (0xFF,0xFF,0xFF)
    im = Image.open('../old/' + str(ans) + '.jpg')
    draw = ImageDraw.Draw(im)
    # newfont = ImageFont.truetype('IdealColor/static/fonts/PingFang Heavy.ttf', 150)
    newfont = ImageFont.truetype('../font/STXINGKA.ttf', 90)
    # print time.strftime('%H_%M_%S', time.localtime(time.time()))
    # print 'color', color[ans]
    # print 'pos', pos
    # print 'ideal', ideal
    # print 'font', newfont
    title = ""
    if(yan == 5):
        title = u'五绝'
    else:
        title = u'七绝'
    if(jtype == 1):
        title += u'︿藏头﹀'
    elif(jtype == 2):
        title += u'︿集句﹀'
    title += '·' + tt
    tmp = len(title) / 2.0 * 90
    for i in range(len(title)):
        draw.text((880, 880 + i * 90 - tmp), title[i], ys, font=newfont)

    py = 0
    if(len(ideal[0]) == 7):
        for i in range(4):
            for j in range(7):
                draw.text((720 - i * 150, 580 + j * 90), ideal[i][j], ys, font=newfont)
    else:
        for i in range(4):
            for j in range(5):
                draw.text((720 - i * 150, 670 + j * 90), ideal[i][j], ys, font=newfont)
    # im.show()
    newfont = ImageFont.truetype('../font/STXINGKA.ttf', 65)
    if(lk):
        tmp = len(lk) / 2.0 * 65
        for i in range(len(lk)):
            draw.text((130 , 980 + i * 65 - tmp), lk[i], ys, font=newfont)

    ntime = datetime.datetime.now()
    time_dy = [u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九']

    tmp = ntime.strftime("%Y")
    time_time = ""
    for i in range(4):
        time_time += time_dy[int(tmp[i])]
    time_time += u'年'
    tmp = ntime.strftime("%m")
    if(tmp[0] == '0'):
        time_time += time_dy[int(tmp[1])]
    else:
        time_time += time_dy[int(tmp[0])] + time_dy[int(tmp[1])]
    time_time += u'月'
    tmp = ntime.strftime("%d")
    if(tmp[0] == '0'):
        time_time += time_dy[int(tmp[1])]
    else:
        time_time += time_dy[int(tmp[0])] + time_dy[int(tmp[1])]
    time_time += u'日'
    print(time_time)
    for i in range(len(time_time)):
        draw.text((130 , 1145 + i * 60), time_time[i], ys, font=newfont)

    time_str = str(time.time())
    filename = '../new/' + time_str + '.jpg'
    im.save(filename)
    return time_str + '.jpg'

for i in range(11, 57):
    add_ideal(i, 7, 2, u'一二三四五六七', [u"一二三四五六七",u"一二三四五六七",u"一二三四五六七",u"一二三四五六七"], u'郭导做作')