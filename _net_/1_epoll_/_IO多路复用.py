I/O多路复用（multiplexing）

select、poll 和 epoll 都是 Linux API 提供的 IO 复用方式

(1)select 时间复杂度O(n)  2001年

无差别轮询 client(1000) -> server(1000 socker_fd)

所以select具有O(n)的无差别轮询复杂度，同时处理的流越多，无差别轮询时间就越长。
同时处理最大连接数有限制1024/32位。

(2)poll 时间复杂度O(n) 2002年
poll本质上和select没有区别
但是它没有最大连接数的限制.
Linux 2.5.44版本后，poll被epoll取代。

(3)epoll 时间复杂度O(1)  2003年

epoll会把哪个流发生了怎样的I/O事件通知我们，事件触发，Linux2.6内核级别支持,没有最大连接数的限制。

int epoll_create(int size);
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);

epoll.wait() -> 返回网络事件

EPOLLIN 收到消息
EPOLLOUT 发送消息
EPOLLHUP 断开

工作模式：

水平触发（LT）：默认工作模式，即当epoll_wait检测到某描述符事件就绪并通知应用程序时，
应用程序可以不立即处理该事件；下次调用epoll_wait时，会再次通知此事件。

边缘触发（ET）： 当epoll_wait检测到某描述符事件就绪并通知应用程序时，应用程序必须立即处理该事件。
如果不处理，下次调用epoll_wait时，不会再次通知此事件。

