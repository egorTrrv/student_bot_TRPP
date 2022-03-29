import setuptools
# создание описания на основе readme
with open("README.md", "r") as fh:
	long_description = fh.read()

# определение requests как requirements для того, чтобы этот пакет работал; зависимости проекта
# requirements = ["requests<=2.21.0"]

setuptools.setup(
	# имя дистрибутива пакета
	name="super_bot",
	# номер версии пакета
	version="0.0.1",
	# имя автора
	author="egorTrrv",
	# его почта
	author_email="",
	# краткое описание (будет отображаться на PyPi)
	description="Super Multifunction Comprehensive Ultimative Student Bot (SMCUSB)",
	# длинное описание (будет отображаться на PyPi, использует readme для заполнения)
	long_description=long_description,
	# url, представляющий домашнюю страницу проекта
	url="https://github.com/egorTrrv/super_bot",
	# находит все пакеты внутри проекта и объединяет их в дистрибутив
	packages=setuptools.find_packages(),
	# зависимости, которые будут установлены вместе с пакетом
	install_requires=requirements
	# предоставляет pip некоторые метаданные о пакете (отображается на странице PyPi)
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: :: ",
		"Operating System :: OS Independent",
	],
	# требуемая версия Python
	python_requires='>=3.6',
)