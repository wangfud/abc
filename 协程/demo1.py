import asyncio

async def cancel_me():
    print('cancel_me(): before sleep')
    try:
        await asyncio.sleep(3600) #模拟一个耗时任务
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    #通过协程创建一个任务，需要注意的是，在创建任务的时候，就会跳入到异步开始执行
    #创建一个任务就相当于是运行了异步函数cancel_me
    #3.7版本
    # task = asyncio.create_task(cancel_me())
    #3.7以前
    task = asyncio.ensure_future(cancel_me())
    #等待一秒钟
    await asyncio.sleep(1)
    print('main函数休息完了')
    #发出取消任务的请求
    task.cancel()
    try:
        await task  #因为任务被取消，触发了异常
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")
# 3.7版本运行运行实践循环的方式
# asyncio.run(main())
#3.6版本运行事件循环的方式
task = asyncio.ensure_future(cancel_me())
# loop=asyncio.get_event_loop()
# loop.run_until_complete(main())

