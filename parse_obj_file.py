# name of the array that hols vertex coordinates -> vertices
# name of the array that hols texture coordinates -> textures
# name of the array that hols vertex normals -> normals
# name of the array that hols vertices -> quads and triangles

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file_name_source = input("Enter .obj file name: ")
file_name_source += ".obj"
file_path_source = os.path.join(dir_path, file_name_source)

file_name_destination = file_name_source[:-4] + "_output.obj"
file_path_destination = os.path.join(dir_path, file_name_destination)

print(file_path_source)
print(file_path_destination)

f1 = open(file_path_source)
f2 = open(file_path_destination, 'x')

lines = f1.readlines()
searchquery = "v "

f2.write("var vertices = [\n")
for line in lines:
	if line.startswith(searchquery):
		line = line.strip("\n")
		line = line.split(" ", 1)
		line = line[1].split()
		f2.write("	")
		for element in line:
			f2.write(element)
			f2.write(", ")
		f2.write("\n")
f2.write("];\n\n")

searchquery = "vt "
f2.write("var textures = [\n")
for line in lines:
	if line.startswith(searchquery):
		line = line.strip("\n")
		line = line.split(" ", 1)
		line = line[1].split()
		f2.write("	")
		for element in line:
			f2.write(element)
			f2.write(", ")
		f2.write("\n")
f2.write("];\n\n")

searchquery = "vn "
f2.write("var normals = [\n")
for line in lines:
	if line.startswith(searchquery):
		line = line.strip("\n")
		line = line.split(" ", 1)
		line = line[1].split()
		f2.write("	")
		for element in line:
			f2.write(element)
			f2.write(", ")
		f2.write("\n")
f2.write("];\n\n")

searchquery = "f "
f2.write("var quads = [\n")
for line in lines:
	if line.startswith(searchquery):
		line = line.strip("\n")
		line = line.split(" ", 1)
		line = line[1].split()
		if len(line) == 4:
			f2.write("	")
			for element in line:
				element = element.split("/")
				for inner_element in element:
					f2.write(inner_element)
					f2.write(", ")
			f2.write("\n")
f2.write("];\n\n")

searchquery = "f "
f2.write("var triangles = [\n")
for line in lines:
	if line.startswith(searchquery):
		line = line.strip("\n")
		line = line.split(" ", 1)
		line = line[1].split()
		if len(line) == 3:
			f2.write("	")
			for element in line:
				element = element.split("/")
				for inner_element in element:
					f2.write(inner_element)
					f2.write(", ")
			f2.write("\n")
f2.write("];\n\n")

f1.close()
f2.close()
