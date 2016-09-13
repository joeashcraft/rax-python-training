"""Lab 06.

Using range(-40, 120, 10) as input, create three comprehensions. Assume the
values in the range represent Fahrenheit temperatures. The comprehensions should
calculate the corresponding Centigrade temperature.
(Centigrade = 5.0/9.0 * (Fahrenheit - 32))

* Create a list and a set using comprehensions. Both the list and the
set should contain tuples which contain each
Fahrenheit/Centigrade pair. Exclude the entries for Fahrenheit
temperatures zero and 50.

* Create a dictionary comprehension with the Fahrenheit
temperatures as keys and Centigrade temperatures as values. Use
the same exclusions as above.
"""


def f_to_c(f):
    c = (5.0 / 9.0 * (f - 32))
    return c

f_temps = range(-40, 120, 10)

my_list = list((f, f_to_c(f)) for f in f_temps if f not in [0, 50])
my_set  = set((f, f_to_c(f)) for f in f_temps if f not in [0, 50])
my_dict = dict((f, f_to_c(f)) for f in f_temps if f not in [0, 50])
