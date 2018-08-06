##九歌API使用说明
###九歌介绍

###接口整体说明

1. 第一次发送藏头诗关键词  https://jiuge.thunlp.cn/sendPoem Post方式
2. 检查古诗生成情况  https://jiuge.thunlp.cn/getPoem Post方式

###sendPoem

url: https://jiuge.thunlp.cn/sendPoem post方式

输入参数(json格式)：

```
{
    "type":"JueJu"
    "yan":"5"或者"7"
    "keyword":关键词list，不能超过4个。
    "user_id":每个人不同的id
}
```
其中 type参数不动，yan参数 为"5"或者"7",剩余两个为每个用户不同的东西。

返回数据的格式：
```
如果返回的为 "mgc"，表示 关键词无法生成古诗；
如果返回的为其他（必定为数字），表示 前面还有  X首古诗等待排队
```

###getPoem

url: https://jiuge.thunlp.cn/sendPoem post方式

输入参数(json格式)：

```
{
    "type":"JueJu"
    "yan":"5"或者"7"
    "keyword":关键词list，不能超过4个。
    "user_id":每个人不同的id
}
```

其中 type参数不动，yan参数 为"5"或者"7",剩余两个为每个用户不同的东西，与 sendPoem 参数相同即可。

返回数据的格式（json格式）：

```
{
    "code":"0"（表示还在生成中）
    "content": 数字（表示前面还有X首诗等待）
}
或者
{
    "code":"1"
    "content": 数组（表示生成的古诗 ["第一句","第二句","第三句","第四句"]
}
```
