
d_start = int(input()[3:])
h_start, m_start, s_start = [int(n) for n in input().split(' : ')]

d_end = int(input()[3:])
h_end, m_end, s_end = [int(n) for n in input().split(' : ')]

dias = (d_end - d_start) * 24 * 60 * 60 
horas = (h_end - h_start) * 60 * 60
minutos = (m_end - m_start) * 60 
segundos = s_end - s_start 

total = dias + horas + minutos + segundos 
segundos = total % 60
minutos = total // 60

horas = minutos // 60 
minutos = minutos % 60

dias = horas // 24
horas = horas % 24

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')