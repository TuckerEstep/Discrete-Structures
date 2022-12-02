class Data_tracker:
    def __init__(self):
        self.number_of_times_function_called = 0
        self.if_count = 0
        self.add_count = 0
        self.subtract_count = 0
        self.start_time = 0
        self.stop_time = 0
        self.assignment_count = 0

    def increment_assignment_count(self):
        self.assignment_count += 1

    def increment_function_call_count(self):
        self.number_of_times_function_called += 1

    def increment_if_count(self):
        self.if_count += 1

    def increment_add_count(self):
        self.add_count += 1

    def increment_subtract_count(self):
        self.subtract_count += 1

    def print_function_data(self):
        print("--- %s seconds ---" % (self.stop_time - self.start_time))



def recur_fibo(n, recursive_data):
    recursive_data.increment_function_call_count()
    recursive_data.increment_if_count()
    if n <= 1:
        return n
    else:
        recursive_data.increment_add_count()
        recursive_data.increment_subtract_count()
        recursive_data.increment_subtract_count()
        return(recur_fibo(n-1, recursive_data) + recur_fibo(n-2, recursive_data))

import time

recursive_data = Data_tracker()

number_of_terms = int(input('how many terms would you like?'))

recursive_data.start_time = time.time()

if number_of_terms <= 0:
   print("Plese enter a positive integer")
else:
   print(f"Fibonacci number for {number_of_terms} terms:")
   print(recur_fibo((number_of_terms - 1), recursive_data))

recursive_data.stop_time = time.time()

print('\n\nRECUSIVE DATA')
recursive_data.print_function_data()


iterative_data = Data_tracker()

n1, n2 = 0, 1
count = 0

if number_of_terms <= 0:
    iterative_data.start_time = time.time()
    print("Please enter a positive integer")
elif number_of_terms == 1:
    iterative_data.start_time = time.time()
    print("Fibonacci sequence upto",number_of_terms,":")
    print(n1)
else:
   iterative_data.start_time = time.time()
   while count < number_of_terms:
       iterative_data.increment_if_count()
       iterative_data.increment_add_count()
       nth = n1 + n2
       iterative_data.increment_assignment_count()
       n1 = n2
       iterative_data.increment_assignment_count()
       n2 = nth
       iterative_data.increment_assignment_count()
       count += 1

iterative_data.stop_time = time.time()
print('\n\nITERATIVE DATA')
iterative_data.print_function_data()