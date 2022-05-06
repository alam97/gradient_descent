import math


def f(x, y):
    return (2*x**2 - 5 * x * y) * math.exp(-5 * y**2 - 3 * x**2)


def fdx(x, y):
    return pow(math.e, -3*pow(x,2) - 5*pow(y,2)) * (-12 * pow(x,3) + 30*pow(x,2)*y + 4*x -5 *y)

def fdy(x, y):
    return -5 * x * pow(math.e, -3*pow(x,2) - 5*pow(y,2)) * (4*x*y - 10*pow(y,2)+1)


def gradient(a, x0, y0, e, n):
    # a przyjmuje jako mala wartosc stala
    a = a
    xStart = [x0, y0]
    xNext = [0, 0]
    # do zapisu pliku
    lines = []
    lines.append("===================================== GRADIENT PROSTY")
    line = f'Punkt startowy funkcji x = {xStart[0]}, y = {xStart[1]}, f(x, y) = {f(xStart[0], xStart[1])}'
    lines.append(line)
    for i in range(1, n+1):
        print(line)
        # xk+1 = xk + ak * dk
        # dk (kierunek) to antygradient czyli xk+1 = xk - ak*dk
        xNext[0] = xStart[0] - fdx(xStart[0], xStart[1]) * a
        xNext[1] = xStart[1] - fdy(xStart[0], xStart[1]) * a
        line = f'{i}. x= {xNext[0]}, y= {xNext[1]}, f(x,y) = {f(xNext[0], xNext[1])}'
        lines.append(line)
        # warunek stopu
        d = math.sqrt(math.pow((xNext[0] - xStart[0]), 2) + math.pow((xNext[1] - xStart[1]), 2))
        if d < e:
            line = f'Znaleziono rozwiazanie: Interacja {i}., x= {xNext[0]}, y= {xNext[1]}, f(x,y) = {f(xNext[0], xNext[1])} '
            print(line)
            lines.append(line)
            break
        xStart[0] = xNext[0]
        xStart[1] = xNext[1]
    return lines


if __name__ == '__main__':
    lines = gradient(0.5, -0.4, -0.4, 1e-8, 40)
    lines2 = gradient(0.5, 0.4, 0.4, 1e-8, 40)
    # zapisuje do pliku
    with open('zadanie2.txt', 'w') as f:
        f.write('\n'.join(lines))
        f.write('\n')
        f.write('\n')
        f.write('\n'.join(lines2))
