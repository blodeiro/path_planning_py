from ..geometry import utils

class Robot:
    def __init__(self, params = {}) -> None:
        self.position = params.get("position", [0,0,0])
        self.rotMatrix = params.get(
            "rotation",
            [[1,0,0],[0,1,0],[0,0,1]])
        self.stepSize = params.get("step", 10)
        self.zoneDeviation = params.get("deviation", 1)
        self.ideal_path = []

    def addWaypoint(self, waypoint : list) -> None:
        self.ideal_path.append(waypoint)

    def reorient(self, nextWaypoint : int) -> None:
        direction = utils.normalize(
            self.ideal_path[nextWaypoint], self.position)
        if self.rotMatrix[0] != direction:
            self.rotMatrix = utils.getRotMatrix(direction)
            print("Reoriented with direction {}".format(self.rotMatrix[0]))

    def move(self) -> bool:
        if len(self.ideal_path) == 0:
            print("Undefined path")
            return True
        nextWaypoint = 0
        stepNum = 0
        #stepToComplete = self.stepSize
        while nextWaypoint < len(self.ideal_path):
            waypointDistance = utils.pointDistance(self.position, self.ideal_path[nextWaypoint])
            while waypointDistance <= self.zoneDeviation:
                print("Waypoint {} reached in step {}".format(nextWaypoint,stepNum))
                nextWaypoint += 1
                if nextWaypoint == len(self.ideal_path):
                    print("End reached in step {}".format(stepNum))
                    return True
                waypointDistance = utils.pointDistance(self.position, self.ideal_path[nextWaypoint])
            self.reorient(nextWaypoint)
            stepToComplete = self.stepSize
            while (waypointDistance - self.zoneDeviation) <= stepToComplete:
                self.position = utils.movePointTowards(
                        self.position,
                        self.ideal_path[nextWaypoint],
                        (waypointDistance - self.zoneDeviation)
                    )
                stepToComplete -= (waypointDistance - self.zoneDeviation)
                print("Waypoint {} reached in step {}".format(nextWaypoint,stepNum))
                nextWaypoint += 1
                if nextWaypoint == len(self.ideal_path):
                    print("End reached in step {}".format(stepNum))
                    return True
                self.reorient(nextWaypoint)
                waypointDistance = utils.pointDistance(self.position, self.ideal_path[nextWaypoint])
            self.position = utils.movePointTowards(
                    self.position,
                    self.ideal_path[nextWaypoint],
                    stepToComplete
                )
            print("Step {} completed".format(stepNum))
            stepNum += 1
        print("Error: move completed without finding an end")
        return False
