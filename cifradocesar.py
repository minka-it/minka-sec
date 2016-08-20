#enconding
#!/usr/bin/python
#-*- coding: utf-8 -*-

mensaje= "VprPGS{jnvg_bar_cyhf_1_vf_3?}"
mensaje2=""

for i in range(0,255):
	for x in mensaje:
		print ord(x)+i % 255
		mensaje2 = mensaje2 + chr(ord(x)+i % 255)
	if mensaje2[0]=="I":
		print mensaje2
	mensaje2=""