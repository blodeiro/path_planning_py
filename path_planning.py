from path_planning_py.robot import robot

import matplotlib.pyplot as plt

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
    plotPoints(r.ideal_path, r.real_path)

def plotPoints(ideal_points, real_path):
    ax = plt.figure().add_subplot(projection='3d')

    x = [p[0] for p in ideal_points]
    y = [p[1] for p in ideal_points]
    z = [p[2] for p in ideal_points]
    
    ax.scatter(x, y, z, c='#00FF00')


    color = '#FF0000'
    for real_points in real_path:
        x_real = [p[0] for p in real_points]
        y_real = [p[1] for p in real_points]
        z_real = [p[2] for p in real_points]
        u = [x0 - x1 for (x0, x1) in zip(x_real[1:], x_real[:-1])]
        v = [y0 - y1 for (y0, y1) in zip(y_real[1:], y_real[:-1])]
        w = [z0 - z1 for (z0, z1) in zip(z_real[1:], z_real[:-1])]
        ax.quiver(x_real[:-1], y_real[:-1], z_real[:-1], u, v, w, color=color)
        if color == '#FF0000':
            color = '#0000FF'
        else:
            color = '#FF0000'

    plt.show()


if __name__ == '__main__':
    main()