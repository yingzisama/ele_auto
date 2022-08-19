——各模块分类
run.py      -启动入口
config.py   -设备号以及一直配置项
conftest.py -一些测试方法配置
module      -各页面操作方法封装
testsuites  -测试用例
logs        -运行log打印
reports     -Html测试报告存放
tools       -工具类
result      -json类型测试报告
assert_pic  -图像识别图片存放处


——module页面命名规则
home    首页
Focus   关注页
live    开播页
message 消息页
mind    我的页
host    主播直播页
audience    观众直播间页面

——testsuites测试用例命名规则：test_module_case
例如——跳转到消息页：test_message_jump

——测试报告查看命令
allure serve ./result   查看生成的测试报告

测试账号
测试3
观众账号：Test12230543
主播端开播账号：10003294
（初始账号部分数据为空，有些用例跑不起来，请使用测试账号跑）

