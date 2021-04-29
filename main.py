from weather_crawler import weather

if __name__ == '__main__':
    res = weather(url="http://www.weather.com.cn/weather/101270101.shtml")
    print(res)
