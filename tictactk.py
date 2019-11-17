import tkinter as tk
import tkinter.font as font


def analise(game):    #analisa todas as possibilidades de haver ganhador, se houver retorna True 
    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        p1.configure(bg='#7bc263');p2.configure(bg='#7bc263');p3.configure(bg='#7bc263')
        return True
    elif game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X':
        p1.configure(bg='#7bc263');p4.configure(bg='#7bc263');p7.configure(bg='#7bc263')
        return True
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        p7.configure(bg='#7bc263');p8.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        p4.configure(bg='#7bc263');p5.configure(bg='#7bc263');p6.configure(bg='#7bc263')
        return True
    elif game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X':
        p3.configure(bg='#7bc263');p6.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[0][1] == 'X' and game[1][1] == 'X' and game[2][1] == 'X':
        p2.configure(bg='#7bc263');p5.configure(bg='#7bc263');p8.configure(bg='#7bc263')
        return True
    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        p1.configure(bg='#7bc263');p5.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':  
        p3.configure(bg='#7bc263');p5.configure(bg='#7bc263');p7.configure(bg='#7bc263')
        return True
    
    elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        p1.configure(bg='#7bc263');p2.configure(bg='#7bc263');p3.configure(bg='#7bc263')
        return True
    elif game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'O':
        p1.configure(bg='#7bc263');p4.configure(bg='#7bc263');p7.configure(bg='#7bc263')
        return True
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        p7.configure(bg='#7bc263');p8.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        p4.configure(bg='#7bc263');p5.configure(bg='#7bc263');p6.configure(bg='#7bc263')
        return True
    elif game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O':
        p3.configure(bg='#7bc263');p6.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O':
        p2.configure(bg='#7bc263');p5.configure(bg='#7bc263');p8.configure(bg='#7bc263')
        return True
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        p1.configure(bg='#7bc263');p5.configure(bg='#7bc263');p9.configure(bg='#7bc263')
        return True
    elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':  
        p3.configure(bg='#7bc263');p5.configure(bg='#7bc263');p7.configure(bg='#7bc263')
        return True
    else:
        pass

class contador(object):     #cria um contador global
    cont = 1
    
def play(buttonpressed):     #recebe as jogadas, modifica a interface de acordo com a jogada e entrega os resultados
    game = [[p1['text'], p2['text'], p3['text']],   
	    [p4['text'], p5['text'], p6['text']],     #transforma o jogo em uma matriz usando os valores(text) dos botões
	    [p7['text'], p8['text'], p9['text']]]
    
    if not analise(game):       #   executa se ninguem tiver ganho
        if buttonpressed['text'] == '':
            contador.cont += 1   #sempre que um player joga, o contador aumenta em 1, alternando entre par e impar

            if contador.cont % 2 == 0:
                label.configure(text='Vez do jogador O')    #   quando par, o botão recebe X
                buttonpressed.configure(text='X')

            elif contador.cont % 2 == 1:
                label.configure(text='Vez do jogador X')    #   quando impar, o botão recebe O
                buttonpressed.configure(text='O')

    # atualiza a matriz com os novos valores dos botões para ver se há ganhador          
    game = [[p1['text'], p2['text'], p3['text']],
	    [p4['text'], p5['text'], p6['text']],
	    [p7['text'], p8['text'], p9['text']]]
    
    if analise(game) or contador.cont==10:  # executa se houver algum ganhador ou se foi expirado o numero de jogadas
        #disablebutton()
        playagain = tk.Button(root, text='Jogar novamente', command=lambda: resetgame(playagain))
        playagain.place(relwidth=0.3, relheight=0.1, relx=0.34, rely=0.5)
        if contador.cont==10 and not analise(game):
            label.configure(text='Empate!')
        elif analise(game):
            if contador.cont % 2 == 0: label.configure(text='Jogador X venceu!')  #o ultimo valor do cont revela o ganhador
            elif contador.cont % 2 == 1: label.configure(text='Jogador O venceu!')
'''
def disablebutton():
    p1.configure(state='disabled'); p2.configure(state='disabled'); p3.configure(state='disabled')
    p4.configure(state='disabled'); p5.configure(state='disabled'); p6.configure(state='disabled')
    p7.configure(state='disabled'); p8.configure(state='disabled'); p9.configure(state='disabled')
'''
def resetgame(playagain):    #reseta o tabuleiro para um novo jogo
    contador.cont = 1
    playagain.destroy()
    label.configure(text='Vez do jogador X')    # primeira jogada sempre será do X, pois o contador starta par
    p1.configure(text='', bg='white'); p2.configure(text='', bg='white'); p3.configure(text='', bg='white')
    p4.configure(text='', bg='white'); p5.configure(text='', bg='white'); p6.configure(text='', bg='white')
    p7.configure(text='', bg='white'); p8.configure(text='', bg='white'); p9.configure(text='', bg='white')
'''
def getnames():
    userentry = tk.Frame(root, bd=3, bg='#ededed', borderwidth=2)
    userentry.place(relwidth=0.72, relheight=0.35, relx=0.135, rely=0.35)

    entryname1 = tk.Entry(userentry, text='X')
    entryname1.place(relwidth=0.55, relheight=0.17, relx=0.1, rely=0.35)
    entryname2 = tk.Entry(userentry, text='Y')
    entryname2.place(relwidth=0.55, relheight=0.17, relx=0.1, rely=0.56)

    go = tk.Button(userentry, text='Jogar', command=play(go))
    go.place(relwidth=0.3, relheight=0.18, relx=0.66, rely=0.45)    
'''

#===========criação da interface============

root = tk.Tk()
root.title('Jogo da Velha')

canvas = tk.Canvas(root, height=500, width=500) 
canvas.pack()

gameframe = tk.Frame(root, bg='#c23838', bd=3)
gameframe.place(relx=0.5, rely=0.57, relwidth=0.8, relheight=0.8, anchor='center')

upFrame = tk.Frame(root, bg='#d3d3d3', bd=3)
upFrame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.13, anchor='center')

labelfont = font.Font(family='helvetica', size=16, weight='bold')
label = tk.Label(upFrame, bg='#d3d3d3', bd=3, text='Vez do jogador X', font=labelfont)
label.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=1, anchor='center')


gamefont = font.Font(family='arial', size=40)
p1 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p1))
p1.place(relwidth=0.29, relheight=0.29, relx=0.05, rely=0.05)

p2 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p2))
p2.place(relwidth=0.29, relheight=0.29, relx=0.35, rely=0.05)

p3 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p3))
p3.place(relwidth=0.29, relheight=0.29, relx=0.65, rely=0.05)

p4 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p4))
p4.place(relwidth=0.29, relheight=0.29, relx=0.05, rely=0.35)

p5 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p5))
p5.place(relwidth=0.29, relheight=0.29, relx=0.35, rely=0.35)

p6 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p6))
p6.place(relwidth=0.29, relheight=0.29, relx=0.65, rely=0.35)

p7 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p7))
p7.place(relwidth=0.29, relheight=0.29, relx=0.05, rely=0.65)

p8 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p8))
p8.place(relwidth=0.29, relheight=0.29, relx=0.35, rely=0.65)

p9 = tk.Button(gameframe, text='', font=gamefont, command=lambda:play(p9))
p9.place(relwidth=0.29, relheight=0.29, relx=0.65, rely=0.65)




root.mainloop()