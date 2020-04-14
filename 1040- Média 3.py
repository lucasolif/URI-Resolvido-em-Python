n1, n2, n3, n4= map(float, input().split())

media=((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
print("Media:","{:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 6.9 >= media >= 5.0:
    print("Aluno em exame.")
    nota_exame= float(input())
    print("Nota do exame:","{:.1f}".format(nota_exame))
    media_final= (nota_exame + media)/2
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print("Media final:","{:.1f}".format(media_final))
    else:
        media_final <= 4.9
        print("Aluno reprovado.")
        print("Media final]:","{:.1f}".format(media_final))
