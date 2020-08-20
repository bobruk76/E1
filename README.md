# E1
# Игра в виселицу
[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/bobruk76/E1/master.png?style=flat-square

[build]: https://travis-ci.org/bobruk76/E1
* склонировать этот репозиторий;
* перейти в папку с ним; 
* создать виртуальное окружение `python -m venv venv`;
* активировать его `source venv/bin/activate` (или `virtualenv venv`)
* установить зависимости `requirements pip install -r requirements.txt`;
* переменную окружения сделать равно текущей директории (текущую директорию можно узнать выполнив команду `pwd`) PYTHONPATH: `export PYTHONPATH=current_folder` (или `set PYTHONPATH=current_folder`)
* Запустить приложение можно с помощью команды `python app.py`.
* Запустить тесты можно с помощью команды `pytest tests/test_pytest.py`
* Создать отчёт по тестовому покрытию  `pytest --cov=. tests/test_pytest.py`