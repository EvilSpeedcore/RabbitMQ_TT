import json
import pika
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver


def get_news():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
    driver.create_options()

    driver.get('https://www.yandex.ru/')
    home_news = driver.find_element_by_xpath(
        xpath="//a[@class='home-link home-link_blue_yes content-tabs__link'][@tabindex='-1']"
    )
    home_news.click()
    soup = BeautifulSoup(driver.page_source, 'html.parser', parse_only=SoupStrainer('ol'))
    news_block = soup.find('ol', class_='list news__list')
    news_titles = [article.next_element['aria-label'] for article in news_block]
    return news_titles


#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Queue
channel.queue_declare(queue='rpc_queue')


#  Callback
def on_request(ch, method, props, body):
    response = get_news()

    #  Publish
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=json.dumps(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


#  Consume
channel.basic_consume(on_request, queue='rpc_queue')
print(" [x] Awaiting RPC requests")
channel.start_consuming()
