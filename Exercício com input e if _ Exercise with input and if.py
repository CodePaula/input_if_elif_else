#!/usr/bin/env python
# coding: utf-8

# In[ ]:


turno = input("Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno. ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")


# In[ ]:


shift = input("In which shift do you study? Type M for morning, V for vespertine or N for night. ")

if shift == "M":
    print("Good morning!")
elif shift == "V":
    print("Good afternoon!")
elif shift == "N":
    print("Good evening!")
else:
    print("Invalid value.")

