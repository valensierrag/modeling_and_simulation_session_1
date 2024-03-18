from classexample import Point

# just to test that Point was imported as expected
# a = Point(5,5)
# print(a)


class ColorPoint(Point):
    # this is a class that inherits from Point:
    COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadu"]

    def __init__(self, x, y, color):
        #self.x = x
        #self.y = y
        super().__init__(x, y) #calling the parend init method
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are: {self.COLORS}")

    @classmethod
    def add_extra_color(cls, color):
        """
        Add a new valid color to the list
        :param color: the name of the color to add
        :return:
        """
        cls.COLORS.append(color)

    @property
    # particular to each individual instance
    def distance_orig(self):
        """
        Return the distance from origin of the point instance
        :return:
        """
        return(self.x**2 + self.y**2)**0.5
    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"

# 5 random color points
# import random
# = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadu"]
# for _ in range(5):
#    color_point = ColorPoint(random.randint(1,100),
#                             random.randint(0,100),
#                             random.choice(colors))
#    color_points.append(color_point)
#
# print(color_points)

if __name__== "__main__" :
    # we added this if to not show all the below lines when importing into advanced point
    ColorPoint.add_extra_color("orange")
    red_point = ColorPoint(10,10,"red")
    orange_point = ColorPoint(20,20,"orange")
    print(ColorPoint.COLORS)
    red_point.x = 30
    print(f"{red_point} has a distance to origin = {red_point.distance_orig}")
    # without the () after orig it is just saying what it is (a method)
    # a property is almost a method that has no parameter and it just calls itself
