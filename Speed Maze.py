from os import system, name
from time import sleep as s
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Load high score from file
def load_high_score():
    try:
        with open("hs12.txt", "r") as file:
            xrx = file.read()
            return float(xrx) if xrx else float('inf')
    except FileNotFoundError:
        return float('inf')

# Save high score to file
def save_high_score(score):
    with open("hs12.txt", "w") as file:
        file.write(str(score))

# Initialize high score
xrx = load_high_score()

while True:
    clear()
    input("""Hello, welcome to the maze game! Use your controls to navigate through the maze and get a new high score.
        Controls:     
            ^       r : restart
            w       
      <-- a s d --> 
            v
        
    [Press enter to start the timer and game]""")
    start_time = time.time()

    lb = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
          "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
          "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
          "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
          "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
          "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
          "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
          "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    l = ["X ", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
         "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
         "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
         "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
         "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
         "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
         "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
         "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    wasd = ["w", "a", "s", "d"]
    _y = ["a", "b", "c", "d", "e", "f", "g", "h"]
    _x = ["1", "2", "3", "4", "5", "6", "7", "8"]
    w_na = ["a1", "a2", "a3", "a4", "a5", "a5", "a6", "a7", "a8"]
    a_na = ["a1", "b1", "c1", "d1", "e1", "f1", 'g1', "h1", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a4", "b4", "c4", "d4", "e4", "g4", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a8", "b8", "c8", "d8", "e8", "f8", "g8"]
    d_na = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "b4", "c4", "d4", "e4", "g4", "h4", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]
    s_na = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    
    tx = 0
    ty = 0

    while True:
        if _y[ty] + _x[tx] == "a8":
            end_time = time.time()
            xrt = end_time - start_time

            if xrt < xrx:
                xrx = xrt
                save_high_score(xrx)
            
            s(0.3)
            clear()
            print(f"""Your High Score: {xrx}
What you got: {xrt}""")
            input("To restart, press [enter]")
            break

        clear()
        print(f""" Your location: {_y[ty]}{_x[tx]} | High Score: {xrx}
        _____________________________________
       |{l[0]} | {l[1]}   {l[2]} | {l[3]}   {l[4]} | {l[5]}   {l[6]} | {l[7]}|
       |{l[8]} | {l[9]} | {l[10]} | {l[11]} | {l[12]} | {l[13]} | {l[14]} | {l[15]}|    
       |{l[16]} | {l[17]} | {l[18]} | {l[19]} | {l[20]} | {l[21]} | {l[22]} | {l[23]}|
       |{l[24]} | {l[25]} | {l[26]} | {l[27]} | {l[28]} | {l[29]} | {l[30]} | {l[31]}|
       |{l[32]} | {l[33]} | {l[34]} | {l[35]} | {l[36]} | {l[37]} | {l[38]} | {l[39]}|
       |{l[40]} | {l[41]} | {l[42]} | {l[43]} | {l[44]} | {l[45]} | {l[46]} | {l[47]}|
       |{l[48]} | {l[49]} | {l[50]} | {l[51]} | {l[52]} | {l[53]} | {l[54]} | {l[55]}|
       |{l[56]}   {l[57]} | {l[58]}   {l[59]} | {l[60]}   {l[61]} | {l[62]}   {l[63]}|
        ``````````````````````````````````````""")
        
        dir_ = input("\nDirection to move >>> ").strip().lower()
        if dir_ == "r":
            break

        if dir_ == "w" and _y[ty] + _x[tx] not in w_na:
            pr = _y[ty] + _x[tx]
            ty -= 1
        elif dir_ == "a" and _y[ty] + _x[tx] not in a_na:
            pr = _y[ty] + _x[tx]
            tx -= 1
        elif dir_ == "s" and _y[ty] + _x[tx] not in s_na:
            pr = _y[ty] + _x[tx]
            ty += 1
        elif dir_ == "d" and _y[ty] + _x[tx] not in d_na:
            pr = _y[ty] + _x[tx]
            tx += 1
        else:
            continue

        ttg = 0
        for x in range(64):
            if lb[ttg] == pr:
                l[ttg] = lb[ttg]
                break
            ttg += 1
        
        ttg = 0
        for x in range(64):
            if _y[ty] + _x[tx] == l[ttg]:
                l[ttg] = "X "
                break
            ttg += 1