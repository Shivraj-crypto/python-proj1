print("Sushant")
class shape:
    def __init__(self, len, bth, rd):
        self.len = len
        self.rd = rd
        self.bth = bth

    def Assign_value(self):
        rof = Rectangle(self.len,self.bth)
        aor = rof.area_of_rect()
        por = rof.perimeter_of_rect()

        cof = circle(self.rd)
        poc = cof.perimeter_of_circ()
        aoc = cof.area_of_circ()

        print("Area of Rectangle : " + str(aor))
        print("perimeter of Rectangle : " + str(por))

        print("Area of circle : " + str(aoc))
        print("perimeter of circle : " + str(poc))


class Rectangle(shape):
    def __init__(self, len, bth):
        self.len = len
        self.bth = bth

    def perimeter_of_rect(self):
        return 2 * (self.len + self.bth)

    def area_of_rect(self):
        return self.len * self.bth


class circle(shape):

    def __init__(self, rd):
        self.rd = rd

    def perimeter_of_circ(self):
        return 2 * 3.141 * self.rd

    def area_of_circ(self):
        return 3.141 * self.rd * self.rd


a = float(input("Length of Rectangle : "))
b = float(input("Breadth of Rectangle : "))
c = float(input("Radius of circle : "))

Main_1 = shape(a, b, c)
Main_1.Assign_value()