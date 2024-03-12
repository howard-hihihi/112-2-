from datetime import datetime

now_time = datetime.now()
time_str = now_time.strftime("%Y-%m-%d %H_%M_%S")

print("now_time:", now_time)
print("time_str:", time_str)
print(type(now_time))
print(type(time_str))