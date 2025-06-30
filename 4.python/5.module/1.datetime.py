import datetime
#import datetime as dt -> dt라는 별명으로 부르겠다.

#datetime
#module.function
print('#1 datetime.MinYEAR')
print(datetime.MINYEAR)

print('#2 datetime.MAXYEAR')
print(datetime.MAXYEAR)

print('#3 datetime.now()')
# yyyy- MM -DD 
print(datetime.datetime.now())


print('#4 datetime.now().strftime()')
print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().strftime('%H :%M :%S'))

print('#5 particle time ; My birthday')

print(datetime.datetime(2004,1,5,9,17,00))
