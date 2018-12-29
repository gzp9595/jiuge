# -*- coding:utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import time
import qrcode

# server_dir = "/home/ljn/Projects/jiuge-photo"

tilte_map = {
        u"五言绝句": 0,
        u"七言绝句": 1,
        u'归字谣': 2,
        u'如梦令': 3,
        u'梧桐影': 4,
        u'渔歌子': 5,
        u'捣练子': 6,
        u'忆江南': 7,
        u'忆王孙': 8,
        u'河满子': 9,
        u'思帝乡': 10,
        u'醉吟商': 11,
        u'卜算子': 12,
        u'点绛唇': 13,
        u'踏莎行': 14,
        u'画堂春': 15,
        u'浣溪沙': 16,
        u'武陵春': 17,
        u'采桑子': 18,
        u'海棠春': 19,
        u'苏幕遮': 20,
        u'蝶恋花': 21,
        }

title_id = {}
for i in tilte_map.keys():
    title_id[tilte_map[i]] = i

title_locate = [
        (455, 330, 65, 60),
        (455, 320, 65, 60),
        (460, 330, 65, 75),
        (510, 330, 65, 75),
        (460, 330, 65, 75),
        (485, 335, 65, 75),
        (480, 330, 65, 75),
        (480, 330, 65, 75),
        (480, 330, 65, 75),
        (480, 350, 65, 75),
        (205, 140, 65, 75),
        (205, 140, 65, 75),
        (200, 115, 65, 75),
        (200, 115, 65, 75),
        (200, 115, 60, 78),
        (200, 115, 65, 75),
        (200, 115, 65, 75),
        (200, 115, 65, 75),
        (200, 115, 65, 75),
        (200, 115, 65, 75),
        (200, 90, 65, 75),
        (200, 90, 65, 75),
        ]

content_locate = [
        (370, 300, 50, 75, 65),
        (370, 225, 50, 75, 65),
        (370, 240, 50, 75, 65),
        (450, 260, 50, 63, 65),
        (375, 240, 50, 75, 65),
        (400, 270, 50, 75, 65),
        (405, 270, 50, 75, 65),
        (405, 270, 50, 75, 65),
        (405, 250, 50, 75, 65),
        (410, 265, 50, 63, 65),
        (170, 250, 50, 55, 63),
        (170, 250, 50, 55, 63, 63),
        (145, 225, 50, 55, 63, 60),
        (145, 200, 50, 55, 63, 60),
        (145, 225, 45, 50, 55, 50),
        (145, 235, 45, 50, 63, 60),
        (145, 235, 45, 50, 63, 60),
        (150, 240, 45, 50, 55, 50),
        (150, 240, 45, 50, 63, 60),
        (155, 215, 45, 50, 55, 50),
        (160, 190, 40, 45, 41, 45),
        (165, 190, 40, 45, 54, 55),
        ]
content_shape = [
        [[5,5,5,5]],
        [[7,7,7,7]],
        [[1,7,3,5]],
        [[6,6,5,6,2,2,6]],
        [[3,3,7,7]],
        [[7,7,3,3,7]],
        [[3,3,7,7,7]],
        [[3,5,7,7,5]],
        [[7,7,7,3,7]],
        [[6,6,6,6,6,6]],
        [[3,5,6,3,6,3,5,3]],
        [[4,6,4],[5,6,4]],
        [[5,5,7,5],[5,5,7,5]],
        [[4,7,4,5],[4,5,3,4,5]],
        [[4,4,7,7,7],[4,4,7,7,7]],
        [[7,6,7,4],[6,6,7,4]],
        [[7,7,7],[7,7,7]],
        [[7,5,7,5],[7,5,7,3,3]],
        [[7,4,4,7],[7,4,4,7]],
        [[7,3,4,5,5],[7,3,4,5,5]],
        [[3,3,4,5,7,4,5],[3,3,4,5,7,4,5]],
        [[7,4,5,7,7],[7,4,5,7,7]],
        ]

def add_ideal(ans, title, content, server_dir):
    im = Image.open(server_dir+'/share/old/' + str(ans) + '.jpg')
    draw = ImageDraw.Draw(im)
    # index = tilte_map[title]
    print(content)
    for i in range(len(content)):
        if(content[i] == u"-"):
            del content[i]
            break
    content = "".join(content)
    index = title
    title = title_id[index]
    if index < 10:
        titlefont = ImageFont.truetype(server_dir+'/share/font/STXINGKA.ttf', title_locate[index][2])
        for i in range(len(title)):
            draw.text((title_locate[index][0], title_locate[index][1] + i * title_locate[index][3]), title[i], (0xFF,0xFF,0xFF), font=titlefont)

        contentfont = ImageFont.truetype(server_dir+'/share/font/STXINGKA.ttf', content_locate[index][2])
        k = 0
        for i in range(len(content_shape[index][0])):
            for j in range(content_shape[index][0][i]):
                draw.text((content_locate[index][0]-i*content_locate[index][3], content_locate[index][1] + j * content_locate[index][4]), content[k], (0xFF,0xFF,0xFF), font=contentfont)
                k += 1
    else:
        titlefont = ImageFont.truetype(server_dir+'/share/font/STXINGKA.ttf', title_locate[index][2])
        for i in range(len(title)):
            draw.text((title_locate[index][0] + i * title_locate[index][3], title_locate[index][1]), title[i], (0xFF,0xFF,0xFF), font=titlefont)

        contentfont = ImageFont.truetype(server_dir+'/share/font/STXINGKA.ttf', content_locate[index][2])
        k = 0
        for i in range(len(content_shape[index][0])):
            for j in range(content_shape[index][0][i]):
                draw.text((content_locate[index][0] + j*content_locate[index][3], content_locate[index][1] + i * content_locate[index][4]), content[k], (0xFF,0xFF,0xFF), font=contentfont)
                k += 1
        if len(content_shape[index]) == 2:
            for i in range(len(content_shape[index][1])):
                for j in range(content_shape[index][1][i]):
                    draw.text((content_locate[index][0] + j *content_locate[index][3], content_locate[index][1] + (i + len(content_shape[index][0])) * content_locate[index][4] + content_locate[index][5]), content[k], (0xFF,0xFF,0xFF), font=contentfont)
                    k += 1



    time_str = str(time.time())
    filename = '/share/new/' + time_str + '.jpg'
    im.save(server_dir+filename)
    img = qrcode.make("https://jiuge.thunlp.cn/pic_share/"+time_str+".jpg")
    img.save(server_dir + filename.replace(".jpg", "ew.jpg"))
    return time_str + '.jpg'

test_content = [
        u"床前明月光疑是地上霜举头望明月低头思故乡",
        u"测"*7*4,
        u"星秋色思君谈月明情怀远忆昔日西征",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        u"为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨为向东坡传语人在玉堂深处别后有谁来雪压小桥无路归去归去江上一犁春雨",
        ]
if __name__ == "__main__":
    #title = u"七言绝句"
    title = u"归字谣"
    title = u'如梦令'
    title = u'梧桐影'
    title = u'渔歌子'
    title = u'捣练子'
    title = u'忆江南'
    title = u'忆王孙'
    title = u'河满子'
    title = u'思帝乡'
    title = u'醉吟商'
    title = u'卜算子'
    title = u'点绛唇'
    title = u'踏莎行'
    title = u'画堂春'
    title = u'浣溪沙'
    title = u'武陵春'
    # title = u'采桑子'
    # title = u'海棠春'
    # title = u'苏幕遮'
    # title = u'蝶恋花'
    index = tilte_map[title]
    add_ideal("demo"+str(index+1), title, test_content[index])
