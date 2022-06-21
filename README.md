樂思蜀的 Pinterest API 产品发布模块

关注我的微信公众号：evanwzw

欢迎多交流讨论，我的邮箱：wzwmail[at]gmail.com

第1步 申请Tocken

登录Pinterest，访问下面网址，获取Tocken：

https://developers.pinterest.com/tools/access_token/

（权限建议将4个都选上：read_public、write_public、read_relationships、write_relationships）

第2步 下载本工具

点击右上方“Clone or download”按钮下载。

第3步 修改工具中的Tocken设置

使用编辑器打开文件“tocken”，将内容替换成第1步获取的Tocken。

第4步 制作CSV格式产品列表

按照test.csv的格式，字段必须为：

产品URL地址，产品图片地址，产品名称（可以自己定义，这是Pin中的文字信息）

将产品CSV文件放到products_csv文件夹，可以是1个或多个文件。

第5步 上传

将程序上传到服务器。

本地运行请挂上VP那个N，Pin已经被土啬！

第6步 获取 Board ID

运行：

python list_my_boards.py

找到你要发布的Board，将ID复制下来；

编辑 pin.py

将第22行中board_id的值替换为你要发布的Board对应的ID。

第7步 导入CSV文件中的产品信息到数据库

命令行运行：

python import.py

第8步 设置定时任务

不同服务器操作系统，请自行搜索设置定时任务的方法。

建议设置为每1小时运行1次（发1帖），过高的频率可能导致Pin降低权重甚至封号。

---------

赞助：
Noracora
https://noracora.com/
