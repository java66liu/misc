#!/usr/bin/env python
#coding: utf-8

import multiprocessing
import time
import os

def consumer(input_q):
    while True:
        item = input_q.get()
        print("%d consumer %s " % (os.getpid(), item))
        time.sleep(1)
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        print("producer ", item)
        output_q.put(item)

if __name__ == "__main__":
    #Queue in two process
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.daemon = True
    cons_p2.start()

    sequence = []
    for i in range(100):
        sequence.append(i)

    producer(sequence, q)

    q.join()
