import time

from DetectFunction import *

if __name__=='__main__':
    s = time.time()
    print(detect(ipt_weights='best.pt', ipt_source='inference/images/bus.jpg', ipt_device='gpu'))
    e = time.time()
    print(f'\nTime to call function {round(e-s, 2)}')

