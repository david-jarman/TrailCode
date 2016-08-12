def towers(n, source, target, aux, num_moves):
    if n > 0:
        num_moves += 1
        num_moves = towers(n-1, source, aux, target, num_moves)

        target.append(source.pop())
        
        print "------"                
        print "Source: "
        print A
        
        print "Aux: "
        print B
        
        print "Target: "
        print C

        num_moves = towers(n-1, aux, target, source, num_moves)
    return num_moves

A = [7,6,5,4,3,2,1]
B = []
C = []

moves = towers(len(A), A, C, B, 0)
        
print "DONE"

print "Source: "
print A
        
print "Aux: "
print B
        
print "Target: "
print C

print "Moves: %s" % moves
