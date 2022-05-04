from path_planning_py.robot import robot

def main():
    r = robot.Robot()
    nPoints = 0

    retrys = 0
    while True:
        try:
            retrys +=1
            if retrys > 10:
                print("Max error input exceeded")
                return
            nPoints = int(input("How many points would you like to add to the path?:\n"))
            break
        except:
            print("{} is not a valid number".format(nPoints))
    print("{} points will be added to the path".format(nPoints))

    for i in range(nPoints):
        retrys = 0
        while True:
            try:
                retrys +=1
                if retrys > 10:
                    print("Max error input exceeded")
                    return
                pointStr = input("Provide X Y Z coordinates for point {} (whitespace separator):\n".format(i))
                point = [float(coord) for coord in pointStr.split(" ")]
                if len(point) != 3:
                    print("{} is not a valid point. Provide 3 coordinates for X Y and Z".format(pointStr))
                else:
                    r.addWaypoint(point)
                    print("Appended point {}".format(point))
                    break
            except:
                print("{} is not a valid point".format(pointStr))

    r.move()



if __name__ == '__main__':
    main()