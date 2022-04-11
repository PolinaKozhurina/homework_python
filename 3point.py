import numpy
import string
import matplotlib.pyplot as plt

T = 0.5
num_m = [100, 500, 1000, 10000]
for i in range(0, 4):
    num = num_m[i]

    x_arr = numpy.linspace(0, 1, num)
    u_arr = numpy.array([1 if 0.1 <= i <= 0.2 else 0 for i in x_arr])
    u_arr_new = numpy.zeros(num)
    u_arr_an = numpy.array([1 if 0.1 <= i <= 0.2 else 0 for i in x_arr])
    u_arr_new_an = numpy.zeros(num)


    def calc_left_corner(u_arr, u_arr_1):
        h = 1 / num
        tau = 1 / (10 * num)
        return (u_arr - u_arr_1)*tau/(2*h) + 0.5*(u_arr + u_arr_1)

    def calc_left_corner_analitic(u_arr, u_arr_k):
        h = 1 / num
        tau = 1 / num
        return (u_arr - u_arr_k) * tau / h + u_arr_k

    for t in range(int(T*(10*num))):
        for j in range(1, num-1):
            u_arr_new[j] = calc_left_corner(u_arr[j-1], u_arr[j+1])
        u_arr = u_arr_new.copy()
    for t in range(int(T * (num))):
            for j in range(1, num-1):
                u_arr_new_an[j] = calc_left_corner_analitic(u_arr_an[j - 1], u_arr_an[j+1])
            u_arr_an = u_arr_new_an.copy()
    plt.title('Linear advection')
    plt.xlabel('x coordinate')
    plt.ylabel('function value')
    plt.grid()
    plt.plot(x_arr, u_arr_new)
plt.plot(x_arr_an, u_arr_new_an)
plt.show()