#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# adicionando a informação solicitada
turno = input("Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno. ")

# as condicionais vão testar se a resposta digitada corresponde às opções aceitas pela variável "turno" (M, V ou N)
# se for M, o resultado será "Bom dia!"
if turno == "M":
    print("Bom dia!")
# como mais de uma condição precisa ser testada, usamos elif
# se for V, o resultado será "Boa tarde!"
elif turno == "V":
    print("Boa tarde!")
# se for N, o resultado será "Boa noite!"
elif turno == "N":
    print("Boa noite!")
# se nenhuma das condições forem atendidas (M, V ou N), o resultado será inválido
else:
    print("Valor inválido.")


# In[ ]:


# adding the requested information
shift = input("In which shift do you study? Type M for morning, V for vespertine or N for night. ")

# the conditionals will test if the typed answer corresponds with the accepted options for the variable "shift" (M, V or N)
# if it's M, the outcome will be "Good morning!"
if shift == "M":
    print("Good morning!")
# as more than one conditional needs to be tested, we use elif
# if it's V, the outcome will be "Good afternoon!"
elif shift == "V":
    print("Good afternoon!")
# if it's N, the outcome will be "Good evening!"
elif shift == "N":
    print("Good evening!")
# if none of the conditionals were satisfied (M, V or N), the outcome will be invalid
else:
    print("Invalid value.")

