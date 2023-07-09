def area_of_a_circle(radius):
	pi = 3.142
	area = pi * (radius ** 2)
	return area

def main(num):
	area = area_of_a_circle(num)
	print("The area of the circle is {}".format(area))

if __name__ == "__main__":
		main(5)