from allfiles import *
cl= client(4,93)
serv = server()
serv.registr(cl.i,cl.s,cl.v,cl.g)
cl.autent()

serv.autent(cl.A,cl.N)
cl.autent2(serv.B,serv.s,serv.k)

print("U клиента ",cl.u)
print("U сервера ",serv.u)
print("S клиента ",cl.S)
print("S сервера ",serv.S)
print("K клиента ",cl.K)
print("K сервера ",serv.K)
print("m клиента ",cl.m)
print("m сервера ",serv.m)

cl.r = serv.chekM(cl.m)
print(cl.r)
print(cl.r_cl)