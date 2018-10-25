#Clase Docente

class Docente:
	def __init__(self, a, b):
		self.nombres=a
		self.ciudad=b

	def agregar_nombres(self,a):
		self.nombres=a

	def obtener_nombres(self):
		return self.nombres

	def agregar_ciudad(self,a):
		self.ciudad=b

	def obtener_ciudad(self):
		return self.ciudad

	def presentar_datos(self):
		string="%s\n\n%s" %(self.obtener_nombres(),self.obtener_ciudad())

#Clase Estudiante

class Estudiante:
	def __init__(self,a,lista_docentes):
		self.nombres=a
		self.docentes=lista_docentes

	def agregar_nombres(self,a):
		self.nombres=a

	def obtener_nombres(self):
		return self.nombres

	def agregar_docentes(self,lista_docentes):
		self.docentes=lista_docentes

	def obtener_docentes(self):
		return self.docentes

	def presentar_datos(self):
		string="\nEstudiante: %s\n"%(self.obtener_nombres())
		string="%s\n%s"%(string,"Docentes:")

		for x in range(0,len(self.docentes)):
			string = "%s\n\n%s->%s" %(string,self.docentes[x].obtener_nombres(),self.docentes[x].obtener_ciudad())

		return string