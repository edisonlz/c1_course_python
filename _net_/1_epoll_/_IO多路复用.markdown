#### I/O多路复用（multiplexing）

select、poll 和 epoll 都是 Linux API 提供的 IO 复用方式

#### (1)select
无差别轮询 client(1000) -> server(1000 socker_fd)  时间复杂度O(n) 

所以select具有O(n)的无差别轮询复杂度，同时处理的流越多，无差别轮询时间就越长。
同时处理最大连接数有限制1024/32位。

总结：
* 1.连接数受限
* 2.查找配对速度慢
* 3.数据由内核拷贝到用户态

#### (2)poll 
poll  解决了 select 的第一个问题。

#### (3)epoll
epoll解决了这三个问题。
* 1. 连接数受限 :不受限。
* 2. 查找配对速度慢 :事件触发
* 3. 数据由内核拷贝到用户态 : mmap 系统层面数据共享.

epoll会把哪1个流发生了怎样的I/O事件通知我们，事件触发，Linux2.6内核级别支持,没有最大连接数的限制。


```c
int epoll_create(int size);
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
```

```c
epoll.wait() -> 返回网络事件
EPOLLO  建立连接
EPOLLIN 收到消息
EPOLLOUT 发送消息
EPOLLHUP 断开
```

工作模式：

水平触发（LT）：默认工作模式，即当epoll_wait检测到某描述符事件就绪并通知应用程序时，
应用程序可以不立即处理该事件；下次调用epoll_wait时，会再次通知此事件。

边缘触发（ET）： 当epoll_wait检测到某描述符事件就绪并通知应用程序时，应用程序必须立即处理该事件。
如果不处理，下次调用epoll_wait时，不会再次通知此事件。

