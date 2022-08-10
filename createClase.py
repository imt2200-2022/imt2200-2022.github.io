import os, glob

#### datos del a clase, completar

ncl=1
clase='clase%d'%ncl
contenidos=['Introducción - Programa del Curso']
title='Inotrducción a Ciencia de Datos'
dia='Martes'
fecha='09/08'
bloque='Introducción'


#### copiar archivos
path_clases='/Users/paguirre/drive/Cursos/IMT2200_IntroCienciaDatos/IMT2200_2022/imt2200_clases_local'
os.system('cp %s/%s/IMT2200_%s.pdf clases/clases-pdf/'%(path_clases,clase,clase))

#####
string_cont=''
for cont in contenidos:
    string_cont=string_cont+'\t\t\t\t\t\t\t <li><p>%s</p></li>\n'%cont
print(string_cont)
strings={'claseX':clase,
         'CLASE X: X':'CLASE %d: %s'%(ncl,title),'<li><p>ContenidoXXX</p></li>':string_cont}

template=open('clases/clase-template.html','r')
output=open('clases/%s.html'%clase,'w')

for line in template.readlines():
    for s in strings.keys():
        if s in line:
            line=line.replace(s,strings[s])
    output.write(line)
output.close()

os.system('git add clases/%s.html'%s)

#### actualiza clases.html

clases=open('clases.html','r').readlines()
output=open('clases.html.temp','w')
stop=False
for line in clases:
    if clase in line:
        stop=True
    if not stop and 'FIN CLASES' in line :
        line='\t\t\t\t\t\t\t<li><a href="clases/%s.html"><h4>CLASE %d: %s</h4></a></li>\n \t\t\t\t\t\t\t<!-- FIN CLASES -->\n'%(clase,ncl,title)
    output.write(line)
output.close()

os.system('mv clases.html.temp clases.html')

### actualiza index.html
index=open('index.html','r').readlines()
output=open('index.html.temp','w')
stop=False
for line in index:
    if clase in line:
        stop=True
    if not stop and 'FIN CLASES' in line :
        line='\t\t\t\t\t\t\t\t\t<tr class="r2"><td class="c1">%d</td><td class="c2">%s</td><td class="c3">%s</td><td class="c4">%s</td>\n \t\t\t\t\t\t\t\t\t<td class="c5"><a href="clases/%s.html" style="font-weight: bolder;">%s</a></td></tr>\n \t\t\t\t\t\t\t<!-- FIN CLASES -->\n' %(ncl,dia,fecha,bloque,clase,title)

    output.write(line)
output.close()

os.system('mv index.html.temp index.html')

### actualiza GitHub
os.system('git pull')
os.system('git add clases/%s.html'%clase)
os.system('git add clases/clases-pdf/IMT2200_%s.pdf'%clase)
os.system('git add clases.html')
os.system('git add index.html')
os.system('git commit -m "agregar %s"'%clase)
os.system('git push')
