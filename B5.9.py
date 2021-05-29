import time
# Создаём класс-секундомер
class MyDecorator:
	"""docstring for class MyDecorator"""
	def __init__(self):
		self.avg_time = 0

	def __enter__(self):
		return self.avg_time

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def __call__(self, num_runs):
		def act_decorator(func):
			for j in range(num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
				self.avg_time += (t1 - t0)
				self.avg_time /= num_runs
			print("Выполнение заняло %.5f секунд" % self.avg_time)
		return act_decorator


#  Использование класса-секундомер как контекстный менеджер
with MyDecorator():
    #  Декоратор как объект класса-секундомера
    mydec = MyDecorator()

    # Используем декоратор для измерения скорости работы функций
    @mydec(10)
    def my_function():
        count = 0
        for j in range(1000000):
            count += 1
        print("func done")