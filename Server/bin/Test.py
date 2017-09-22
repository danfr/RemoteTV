import time

from bin.Worker import Worker

w = Worker()
w.play_new_stream("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(10)
w2 = Worker()
w2.play_new_stream("https://www.youtube.com/watch?v=vTIIMJ9tUc8")
