# Семинар по парсингу

## Задание
Необходимо разработать программу-парсер для сайта https://books.toscrape.com.
Программа должна обходить все страницы с книгами из заданного раздела (раздел задается урлом, с которого надо начинать обход).
Парсинг страниц надо осуществлять
* при помощи механизма css-селекторов;
* при помощи механизма xpath-ов.

Обход страниц с книгами сделать
* однопоточным;
* многопоточным;
* асинхронным.

## Материалы
1. Ryan Mitchell. Web scraping with python. https://library-it.com/wp-content/uploads/2020/10/web-scraping-with-python.pdf
2. CSS и XPath для QA: чтобы разобраться с локаторами, нужно всего лишь…: https://habr.com/ru/companies/skyeng/articles/588282/.
3. Документация Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/.
4. Документация lxml, раздел про xpath: https://lxml.de/xpathxslt.html.
5. Документация python пакета concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html.
6. Python Asyncio: The Complete Guide: https://superfastpython.com/python-asyncio/.
