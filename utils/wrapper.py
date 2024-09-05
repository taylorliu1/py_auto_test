import threading
import time

class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

class Go():
    def __init__(self, need_return=False, timeout=60):
        self.need_return = need_return
        self.timeout = timeout


    def __call__(self, f):
        print('execute Decorator__call__()')
        def wrap(*args):
            # print('execute wrap()')
            t = MyThread(target=f, args=args)
            print('execute ' + f.__name__ + '()')
            if not self.need_return:
                t.start()
                # t.join()
                return t
            else:
                t.setDaemon(True)
                t.start()
                sleep_num = int(self.timeout // 1)
                sleep_nums = round(self.timeout % 1, 1)
                for i in range(sleep_num):
                    time.sleep(1)
                    res = t.get_result()
                    if res:
                        return res
                time.sleep(sleep_nums)
                if t.get_result():
                    return t.get_result()
                else:
                    return"time out"
            print(f.__name__ + '()execte done')
        return wrap