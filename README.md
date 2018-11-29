# el_spiders

#### 项目介绍
3.6

#### 软件架构
本架构实现分布式，异步请求，监控功能，自动更新。


#### 安装教程

1. python3.6版本
2. Git clone https://gitee.com/yuansupachong/el_spiders.git
3. 安装依赖包，通过requirements一键安装
4. 从目录el_spiders/toos/history_copy/下   拷贝_spider_copy.cfg到(并更名)---->  el_spiders/manager/_spider.cfg
    作用是启动爬虫的配置
5. 从目录el_spiders/toos/history_copy/下   拷贝env_copy.py到(并更名)---->  el_spiders/manager/env.py
    作用是配置此项目爬虫信息监控所需mysql，rabbitmq的环境所在机器ip



#### 使用说明
1. setting.default_mysql(env.py) 谁都使用了：
    runner.py 中使用了配置mysql，rab未使用，用以读取spider_info，以及注册爬虫信息。(爬虫的运行可以不依赖此注册，及读取spider_info)
    也就是说，env里的配置不影响爬虫运行，只不过信息注册到了其他机器的数据库，防止给其他机器误解，和所连机器监控不到。
    monitor 模块下

2. 通过 el_spiders/manager/run.py 启动爬虫，与_spider.cfg配合。
3. 启动 monitor/all_monitor_pid.py 加入实时监控，pid汇报及kill,server运行状况，机器性能等。
4. 启动 monitor/all_distribute_run.py 接受爬虫启动指令，主要在爬虫自动更新时使用。

####qi
setting.rabbitmq_ip 设置为0,表示不声明队列，为-1不起作用。
#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)