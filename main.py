from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Port, Color, Direction, Button, Side, Icon, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


motorLeft = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.C, Direction.CLOCKWISE)
 
smallMotorLeft = Motor(Port.A)
smallMotorRight = Motor(Port.B)
 
colorLeft = ColorSensor(Port.D)
colorRight = ColorSensor(Port.E)

# Initialize the hub
hub = PrimeHub(top_side=Axis.Y, front_side=Axis.X)
hub.light.on(Color.RED)
hub.imu.reset_heading(0)
hub.display.orientation(Side.RIGHT)
hub.system.set_stop_button(Button.BLUETOOTH)

# Initialize DriveBase
db = DriveBase(motorLeft, motorRight, wheel_diameter=56.2, axle_track=114) 
db.use_gyro(True)
db.settings(200, 210, 130, 130)



def straight(distance, speed=50, acceleration=300):
    """
    param distance: Distance to drive in mm
    param speed: Speed to drive at in %
    """
    # Max speed: 1000 deg/s
    db.settings(speed * 10, acceleration, 130, 130)
    db.straight(distance)


def turn(angle, speed=20, acceleration=200):
    """
    param angle: Angle to turn in degrees
    param speed: Speed to drive at in %
    """
    # Max speed: 1000 deg/s
    db.settings(200, 210, speed * 10, acceleration)
    db.turn(angle)

# Round functions
def roundOne(): #Größten Probleme:
    ...

def roundTwo():
    ...

def roundThree():
    ...


def roundFour():
    ...

def roundFive():
    ...

def roundSix():
    ...

def roundSeven():
    ...

def roundEight():
    ...


# Number matrices
NUMBER_MATRICES = {
    1: [
        [0, 100, 0, 0, 0],
        [100, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    2: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    3: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    4: [
        [100, 0, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0],
    ],
    5: [
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    6: [
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    7: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
    ],
    8: [
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
}

class UI:
    def __init__(self):
        self.currentRound = 1 
        self.ROUND_CYCLE = {
            1: roundOne,
            2: roundTwo,
            3: roundThree,
            4: roundFour,
            5: roundFive,
            6: roundSix,
            7: roundSeven,
            8: roundEight,
        }


    def start(self):
        """ Starts the user interface."""
        self.status()
        self.updateNumber(NUMBER_MATRICES[self.currentRound])

        while True:
            self.updateBattery()
            pressedButtons = hub.buttons.pressed()

            if Button.CENTER in pressedButtons:
                self.execute()

            if Button.RIGHT in pressedButtons:
                self.cycle(Direction.CLOCKWISE)

            if Button.LEFT in pressedButtons:
                self.cycle(Direction.COUNTERCLOCKWISE)

            wait(50)  # Reduce CPU usage


    def cycle(self, direction):
        """Cycles up or down."""
        if direction == Direction.CLOCKWISE:
            self.currentRound = self.currentRound % len(self.ROUND_CYCLE) + 1
        else:
            self.currentRound = len(self.ROUND_CYCLE) if self.currentRound == 1 else self.currentRound - 1

        self.updateNumber(NUMBER_MATRICES[self.currentRound])
        hub.speaker.beep(100, 50)
        wait(100)


    def execute(self):
        """Executes the current round."""
        hub.display.icon(Icon.ARROW_UP)  
        self.ROUND_CYCLE[self.currentRound]()  
        wait(200)

        self.cycle(Direction.CLOCKWISE) # Go to the next round


    def status(self):
        """ Print general information about the robot."""
        print("Battery: ", hub.battery.voltage(), " mV")
        print("Calibrated: ", hub.imu.ready())


    def updateBattery(self):
        """ Displays the battery level on the hub."""
        voltage = hub.battery.voltage()
        MAX_VOLTAGE = 8400
        for i in range(5): 
            if voltage >= MAX_VOLTAGE - (i + 1) * 100: # Each level equals 100 mV
                hub.display.pixel(i, 4, 40)


    def updateNumber(self, matrix):
        """ Updates only the left four columns"""
        for i in range(0, 5):
            for j in range(0, 4):
                hub.display.pixel(i, j, matrix[i][j])

ui = UI()
ui.start()