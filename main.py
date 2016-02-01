__author__ = "Michael Papesca"

import practice

# Start of program
practice.startprogram()

practice.receiveboardpieces()
practice.checksuccess()
# for i in xrange(0, 8):
#     print "\nValue: ", practice.globalPiecesInfo[i].value
#     print "Position: ", practice.globalPiecesInfo[i].position
#     print "Distance: ", practice.globalPiecesInfo[i].distance
#     print "Coordinates: (", practice.globalPiecesInfo[i].x_coor, ", ", practice.globalPiecesInfo[i].y_coor, ")"
# x = practice.moveblankspace(practice.UP)
success = practice.solve()

if success:
    print "Success!"
# End of program
