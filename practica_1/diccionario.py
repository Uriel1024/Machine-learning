#El programa va a funcionar consultando constantemente un diccionara para poder saber si el objeto en el que el usuario esta pensando cumple con las caracteristicas


#Estas son las carecteristicas principales que describen a las cosas que puede tener el usuario en mente
caracteristicas = ["objeto", "persona", "lugar", "vivo", "animal", "tecnologico",
"natural", "comestible", "transporte", "humano", "lugar_cerrado", "escribir", "entretenimiento",
"pequenio", "grande", "antiguo", "util_diario","humano_creo","semillas","crece_tierra","animal_proviene","escuela","investigacion"]


pensamiento = {


	#objetos
	"lapiz" : {"objeto": True, "oficina": True, "escuela": True,  "escribir": True, "humano_creo":True},
	"celular" : {"objeto": True, "tecnologico": True, "util_diario": True, "pequenio": True, "humano_creo": True, "escribir":True},
	"silla" : {"objeto": True, "humano_creo": True, "util_diario": True},
	"automovil" : {"objeto": True, "transporte": True, "tecnologico":True, "humano_creo": True, "grande":True},
	"balon" : {"objeto": True, "entretenimiento": True, "pequenio": True},
	"teclado" : {"objeto": True, "escribir": True	, "tecnologico": True, "humano_creo": True, "util_diario": True, },
	"reloj" : {"objeto":True, "tecnologico": True, "pequenio": True, "util_diario":True, "humano_creo": True},
	"compudatora" : {"objeto": True, "tecnologico":True, "escribir":True, "entretenimiento": True, "util_diario":True,"humano_creo": True },
	"cubierto" : {"objeto": True,  "util_diario": True, "pequeno": True, "humano_creo":True},
	"television" : {"objeto": True, "tecnologico": True, "entretenimiento": True, "humano_creo": True},
	"fruta" : {"objeto": True, "comestible": True, "natural": True, "semillas":True},
	"verdura" : {"objeto": True, "comestible": True, "natural":True},
	"tuberculo" : {"objeto": True, "comestible": True, "natural":True, "crece_tierra":True},
	"carne" : {"objeto": True, "comestible":True, "natural": True, "animal_proviene": True},
	"botella" : {"objeto":True, "humano_creo":True, "util_diario": True},
	"leche" : {"objeto": True, "animal_proviene": True, "comestible": True, "natural": True},
	"huevo" : {"objeto": True, "animal_proviene": True, "comestible": True, "natural": True, "pequenio": True},

 	#lugares

	"paris" : {"lugar": True, "famoso": True, "lugar_cerrado": False},
	"playa" : {"lugar": True, "natural": True, "entretenimiento": True},
	"cine" : {"lugar": True, "lugar_cerrado": True, "entretenimiento": True},
	"escuela" : {"lugar": True, "lugar_cerrado": True, "util_diario": True},
	"museo" : {"lugar": True, "lugar_cerrado": True, "antiguo": True},
	"desierto" : {"lugar": True, "natural": True, "grande": True},
	"volcan" : {"lugar": True, "natural": True, "grande": True},
	"oficina" : {"lugar": True, "lugar_cerrado": True, "util_diario": True},
	"parque" : {"lugar": True, "natural": True, "entretenimiento": True},
	"marte" : {"lugar": True, "natural": True, "famoso": True},
	"escom" : {"lugar": True, "escribir":True, "humano_creo":True, "escuela": True, 'investigacion': True, "lugar":True},
	"cic" : {"lugar":True, "escribir": True, "humano_creo":True, "investigacion": True, 'escuela': True, "lugar_cerrado":True}


}

#Las preguntas que se hacen con base en las caracteristicas.

preguntas = {
	"objeto" :"¿Es un objeto fisico? (s/n): ",
	"persona" : "¿Es una persona real o ficticia? (s/n): ",
	"lugar" : "¿Es un lugar? (s/n): ",
	"animal":  "¿Es algun tipo de animal? (s/n): " ,
	"vivo": "¿Es algo que esta o estuvo vivo? (s/n): ",
	"tecnologico": "Esta relacionado con la tecnologia? (s/n): ",
	"natural": "¿Es algo que se obtiene directamente de la naturaleza? (s/n): ",
	"comestible": "¿Es algo comestible para el ser humano? (s/n): ",
	"transporte": "¿Es algun medio de transporte? (s/n): ",
	"humano": "¿Es un ser humano? (s/n): ",
	"lugar_cerrado": "¿Es un lugar cerrado (no cuenta con espacios abiertos) ? (s/n): ",
	"escribir": "¿Sirve para escribir? (s/n): ",
	"entretenimiento": "¿Es alguna forma de entretenimiento? (s/n): ",
	"pequenio": "¿Es un objeto pequenio? (s/n): ",
	"grande": "¿Es un objeto grande? (s/n): ",
	"antiguo": "¿Es algo antiguo o historico? (s/n): ",
	"util_diario": "¿Es algo que se le puede sacar provecho en el dia a dia (una herramienta)? (s/n): ",
	"humano_creo": "¿Fue creado por los humanos? (s/n): ",
	"semillas": "¿Contiene semillas? (s/n): ",
	"crece_tierra": "¿Es algo que crece dentro de la tierra(bajo tierra)? (s/n): ",
	"animal_proviene": "¿Es algo que proviene de un animal? (s/n): ",
	"escuela": "¿Es una escuela? (s/n): ",
	"investigacion": "¿Es un centro de investigacion? (s/n): ",
	}

